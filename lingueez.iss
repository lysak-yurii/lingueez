; Inno Setup script for Lingueez — wraps the PyInstaller onedir build
; (dist\Lingueez\) into a Windows installer with a Start Menu shortcut and an
; uninstaller. Built in CI by ISCC; pass the version with /DAppVersion=X.Y.Z.
;
;   iscc /DAppVersion=2.0.1 lingueez.iss   ->  installer_output\Lingueez-2.0.1-Setup.exe

#define AppName "Lingueez"
#define AppPublisher "Yurii Lysak"
#define AppExe "Lingueez.exe"
#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
; A fixed AppId ties upgrades and the uninstaller to the same product across versions.
AppId={{8F3A6E2C-1B4D-4C9A-9E7F-2A5B6C7D8E90}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
; Per-user install: no admin/UAC prompt (important for an unsigned installer).
; The app keeps its data in %APPDATA%\Lingueez regardless of install location.
PrivilegesRequired=lowest
DefaultDirName={localappdata}\Programs\{#AppName}
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
OutputDir=installer_output
OutputBaseFilename=Lingueez-{#AppVersion}-Setup
SetupIconFile=assets\icons\icon.ico
UninstallDisplayIcon={app}\{#AppExe}
WizardStyle=modern
; With 30 wizard languages the default (always show a Select Language picker)
; would greet everyone with a 30-item list. "auto" shows it only when Windows'
; UI language matches none of them — everyone else goes straight to the wizard
; in their own language, mirroring the app's own first-run OS detection.
ShowLanguageDialog=auto
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

; Wizard UI languages, one per locale the app itself ships (locales\<code>.py),
; so the installer speaks the same language the app will start in. Inno picks
; the entry matching the user's Windows UI language automatically and falls back
; to English, so the language dialog stays out of the way.
;
; Most come from the compiler's own Languages\ folder. Seven have no official
; Inno translation and are vendored under packaging\inno\languages\ from
; jrsoftware/issrc's Unofficial folder — see the README there before updating.
; Malaysian (5.1.0+) and Romanian (6.1.0+) predate some messages 6.7 added;
; ISCC warns and falls back to the English text for those, which is expected.
; Hindi has no Inno translation in any form, so `hi` users get an English wizard.
;
; Thai became official in Inno Setup 6.7.1 — the pinned CI version. Building
; with an older ISCC fails on that line; drop it or upgrade.
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "bulgarian"; MessagesFile: "compiler:Languages\Bulgarian.isl"
Name: "czech"; MessagesFile: "compiler:Languages\Czech.isl"
Name: "danish"; MessagesFile: "compiler:Languages\Danish.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "greek"; MessagesFile: "packaging\inno\languages\Greek.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "finnish"; MessagesFile: "compiler:Languages\Finnish.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "croatian"; MessagesFile: "packaging\inno\languages\Croatian.isl"
Name: "hungarian"; MessagesFile: "compiler:Languages\Hungarian.isl"
Name: "indonesian"; MessagesFile: "packaging\inno\languages\Indonesian.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "korean"; MessagesFile: "compiler:Languages\Korean.isl"
Name: "malaysian"; MessagesFile: "packaging\inno\languages\Malaysian.isl"
Name: "norwegian"; MessagesFile: "compiler:Languages\Norwegian.isl"
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "romanian"; MessagesFile: "packaging\inno\languages\Romanian.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "slovak"; MessagesFile: "compiler:Languages\Slovak.isl"
Name: "serbiancyrillic"; MessagesFile: "packaging\inno\languages\SerbianCyrillic.isl"
Name: "swedish"; MessagesFile: "compiler:Languages\Swedish.isl"
Name: "thai"; MessagesFile: "compiler:Languages\Thai.isl"
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"
Name: "ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"
Name: "vietnamese"; MessagesFile: "packaging\inno\languages\Vietnamese.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\Lingueez\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExe}"
Name: "{userdesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExe}"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent
