# Microsoft Store (MSIX) packaging

MSIX package manifest and assets for the Microsoft Store build of Lingueez. The
package wraps the same PyInstaller onedir output (`dist\Lingueez\`, `Lingueez.exe`
at its root) as the Inno Setup `.exe` installer — the two are independent
consumers of one build, and the `.exe` path is unchanged. CI builds the `.msix`
in the `build-windows` job of `.github/workflows/release.yml` (and
`test-build.yml`) after the installer step.

## Files

- `AppxManifest.xml` — the package manifest. Package identity is fixed (see
  below); only the `{{VERSION}}` token is substituted at build time.
- `Assets/` — **committed** visual assets (tiles and logos) referenced by the
  manifest.
- `generate_assets.py` — Pillow script that derives `Assets/` from
  `assets/icons/icon.png`. Rerun after changing the master icon.

## Package identity

`Identity` must match the reserved product in Partner Center (Product management →
Product identity) or the Store rejects the upload. These values are set directly
in `AppxManifest.xml`:

| Manifest field                    | Value                                     |
| --------------------------------- | ----------------------------------------- |
| `Identity/Name`                   | `Lingueez.Lingueez`                       |
| `Identity/Publisher`              | `CN=28779F39-F4FA-4661-B226-BEFACD1E833B` |
| `Properties/PublisherDisplayName` | `Lingueez`                                |

`Identity/Version` is templated: CI substitutes `{{VERSION}}` with `APP_VERSION`
from `app/version.py` as a 4-part `x.y.z.0` string (the Store requires the
revision component to be `0`).

## Signing

CI produces the `.msix` **unsigned**; the Store re-signs it on submission, so no
code-signing certificate is required. Signing is only needed to install the
package locally for testing (see below).

## Build

CI stages a layout beside the PyInstaller output and packs it with `makeappx`
from the Windows SDK. To reproduce locally on Windows after `pyinstaller
lingueez.spec`:

```powershell
$ver = "2.0.4"
$layout = "msix_layout"
Remove-Item -Recurse -Force $layout -ErrorAction Ignore
New-Item -ItemType Directory $layout | Out-Null
Copy-Item dist\Lingueez\* $layout -Recurse
Copy-Item packaging\msix\Assets $layout\Assets -Recurse
(Get-Content packaging\msix\AppxManifest.xml) `
  -replace '\{\{VERSION\}\}', "$ver.0" | Set-Content $layout\AppxManifest.xml
makeappx pack /d $layout /p "Lingueez-$ver.msix" /o
```

## Local install test

An unsigned package won't install outside the Store. To smoke-test on a dev
machine, sign it with a self-signed certificate whose subject exactly equals
`Identity/Publisher`, trust it, then install:

```powershell
$pub = "CN=28779F39-F4FA-4661-B226-BEFACD1E833B"
$cert = New-SelfSignedCertificate -Type Custom -Subject $pub `
  -KeyUsage DigitalSignature -CertStoreLocation Cert:\CurrentUser\My `
  -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3")
Export-Certificate -Cert $cert -FilePath test.cer
Import-Certificate -FilePath test.cer -CertStoreLocation Cert:\LocalMachine\TrustedPeople
signtool sign /fd SHA256 /a /sha1 $cert.Thumbprint "Lingueez-2.0.4.msix"
Add-AppxPackage "Lingueez-2.0.4.msix"
```

## Remaining submission tasks

- Justify the `runFullTrust` restricted capability: the global Add-Word shortcut
  installs a system-wide low-level keyboard hook, available only to a full-trust
  desktop app.
