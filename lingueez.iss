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
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\Lingueez\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExe}"
Name: "{userdesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExe}"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent
