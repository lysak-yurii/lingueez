"""PDF / Excel / CSV / TXT exporters, GUI-free.

All functions take a list of row dicts (keys: ID, RowNumber, Status,
Language1, Word1, Language2, Word2, Source, created_at) plus settings,
and write straight to the chosen path. Raise on failure.
"""
import logging
import os
import sqlite3

import pandas as pd
from openpyxl.styles import PatternFill
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image as RepImage
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

from app.config import get_bool, get_float, get_int

# Display headers in the same column order as the table
EXPORT_COLUMNS = ["ID", "RowNumber", "Status", "Language1", "Word1", "Language2", "Word2", "Source", "created_at"]
EXPORT_HEADERS = {
    "ID": "ID", "RowNumber": "№", "Status": "Status", "Language1": "Language",
    "Word1": "Word", "Language2": "Translation", "Word2": "Word",
    "Source": "Source", "created_at": "Created at",
}


def register_fonts(font_folder='fonts'):
    """Register every .ttf in fonts/ with reportlab; returns their names."""
    names = []
    if not os.path.isdir(font_folder):
        return names
    for font_file in os.listdir(font_folder):
        if not font_file.endswith('.ttf'):
            continue
        font_name = os.path.splitext(font_file)[0]
        try:
            pdfmetrics.registerFont(TTFont(font_name, os.path.join(font_folder, font_file)))
            names.append(font_name)
        except Exception as exc:
            logging.error(f"Failed to register font {font_name}: {exc}")
    return names


def _rows_to_table(rows, exclude_columns):
    exclude = {c.strip() for c in exclude_columns}
    included = [c for c in EXPORT_COLUMNS if c not in exclude]
    headers = [EXPORT_HEADERS[c] for c in included]
    data = [[("" if row.get(c) is None else row.get(c)) for c in included] for row in rows]
    return headers, data, included


def export_to_excel_file(rows, file_path, settings):
    sheet_name = settings.get("sheet_name", "Sheet1")
    start_row = get_int(settings, "start_row", 0)
    start_column = get_int(settings, "start_column", 0)
    exclude_columns = settings.get("exclude_columns_excel", "ID,Source").split(',')
    alternate_row_color = settings.get("alternate_row_color", "#e0e0e0")
    auto_column_width = get_bool(settings, "auto_column_width", True)
    freeze_panes = get_bool(settings, "freeze_panes", False)

    headers, data, _ = _rows_to_table(rows, exclude_columns)
    df = pd.DataFrame(data, columns=headers)

    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, startrow=start_row,
                    startcol=start_column, index=False)
        worksheet = writer.sheets[sheet_name]

        if alternate_row_color:
            color = alternate_row_color.replace('#', '')
            for row_idx in range(start_row + 2, len(df) + start_row + 2):
                if (row_idx - start_row - 1) % 2 == 0:
                    for col_idx in range(start_column, len(headers) + start_column):
                        cell = worksheet.cell(row=row_idx, column=col_idx + 1)
                        cell.fill = PatternFill(start_color=color, end_color=color, fill_type='solid')

        if auto_column_width:
            for column in worksheet.columns:
                max_length = max((len(str(cell.value)) for cell in column if cell.value is not None), default=0)
                worksheet.column_dimensions[column[0].column_letter].width = max_length + 2

        if freeze_panes:
            worksheet.freeze_panes = worksheet['A2']


def export_to_csv_file(rows, file_path, settings):
    delimiter = settings.get("csv_delimiter", ",")
    exclude_columns = settings.get("exclude_columns_excel", "ID,Source").split(',')
    headers, data, _ = _rows_to_table(rows, exclude_columns)
    pd.DataFrame(data, columns=headers).to_csv(file_path, sep=delimiter, index=False)


def export_to_txt_file(rows, file_path, settings):
    delimiter_setting = settings.get("txt_delimiter", "\\t")
    delimiter = "\t" if delimiter_setting in ("\\t",) or delimiter_setting.lower() == "tab" else delimiter_setting
    exclude_columns = [c.strip() for c in settings.get("exclude_columns_txt", "ID,Source").split(',')]
    include_headers = get_bool(settings, "txt_include_headers", True)
    header_lines = settings.get("txt_header_lines", "#separator:tab\\n#html:true\\n").replace('\\n', '\n')

    _, data, _ = _rows_to_table(rows, exclude_columns)

    with open(file_path, 'w', encoding='utf-8') as txt_file:
        if include_headers:
            txt_file.write(header_lines)
            if not header_lines.endswith('\n'):
                txt_file.write('\n')
        for row in data:
            txt_file.write(delimiter.join(str(v) for v in row) + "\n")


def export_to_pdf_file(rows, file_path, settings, db_path='dictionary.db'):
    """Render rows into a styled PDF table, optionally with definitions."""
    left_margin = get_float(settings, "left_margin", 10)
    right_margin = get_float(settings, "right_margin", 10)
    top_margin = get_float(settings, "top_margin", 10)
    bottom_margin = get_float(settings, "bottom_margin", 10)
    page_size = settings.get("page_size", "Letter")
    font_name = settings.get("font_name", "Helvetica")
    font_size = get_float(settings, "font_size", 10)
    leading = get_float(settings, "leading", 12)
    alignment = settings.get("alignment", "CENTER")
    header_bg_color = settings.get("header_bg_color", "grey")
    bg_color = settings.get("bg_color", "beige")
    text_color = settings.get("text_color", "whitesmoke")
    grid_color = settings.get("grid_color", "black")
    bg_image = settings.get("bg_image", "")
    exclude_columns = [c.strip() for c in
                       settings.get("exclude_columns", "ID,Source,created_at,Definition,Definition2").split(',')]

    col_widths = [get_float(settings, f"col_width_{i}", w) * inch
                  for i, w in [(1, 0.5), (2, 1), (3, 1), (4, 2.4), (5, 1), (6, 2.5)]]

    alignment_code = {"LEFT": 0, "CENTER": 1, "RIGHT": 2}.get(alignment, 1)
    pagesize = {"Letter": letter, "A4": A4}.get(page_size, letter)

    headers, data_rows, included = _rows_to_table(rows, exclude_columns)

    include_def1 = "Definition" not in exclude_columns
    include_def2 = "Definition2" not in exclude_columns
    if include_def1:
        headers.append("Definition")
    if include_def2:
        headers.append("Definition2")

    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(name='CustomFontStyle', fontName=font_name,
                                  fontSize=font_size, leading=leading, alignment=alignment_code)
    styles.add(custom_style)

    definitions = {}
    if include_def1 or include_def2:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        for row in rows:
            cursor.execute("SELECT Definition, Definition2 FROM words WHERE id = ?", (row["ID"],))
            result = cursor.fetchone()
            definitions[row["ID"]] = result if result else ("", "")
        connection.close()

    data = [headers]
    for source_row, table_row in zip(rows, data_rows):
        cells = [Paragraph(str(v), custom_style) for v in table_row]
        if include_def1 or include_def2:
            d1, d2 = definitions.get(source_row["ID"], ("", ""))
            if include_def1:
                cells.append(Paragraph(str(d1 or ""), custom_style))
            if include_def2:
                cells.append(Paragraph(str(d2 or ""), custom_style))
        data.append(cells)

    pdf = SimpleDocTemplate(file_path, pagesize=pagesize, rightMargin=right_margin,
                            leftMargin=left_margin, topMargin=top_margin, bottomMargin=bottom_margin)
    elements = []

    if bg_image and os.path.isfile(bg_image):
        try:
            bg = RepImage(bg_image)
            page_width, page_height = pagesize
            scale = min((page_width - left_margin - right_margin) / bg.imageWidth,
                        (page_height - top_margin - bottom_margin) / bg.imageHeight)
            bg.drawWidth = bg.imageWidth * scale
            bg.drawHeight = bg.imageHeight * scale
            elements.append(bg)
        except Exception as exc:
            logging.error(f"Error loading background image: {exc}")

    table = Table(data, colWidths=col_widths[:len(headers)], repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), header_bg_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), text_color),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), font_name),
        ('FONTNAME', (0, 1), (-1, -1), font_name),
        ('FONTSIZE', (0, 1), (-1, -1), font_size),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), bg_color),
        ('GRID', (0, 0), (-1, -1), 1, grid_color),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(table)
    pdf.build(elements)
