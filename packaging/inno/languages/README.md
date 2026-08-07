# Vendored Inno Setup wizard translations

`lingueez.iss` gives the Windows installer a wizard language for every locale the
app ships (`locales/<code>.py`). Inno Setup bundles most of them in its own
`Languages\` folder, referenced as `compiler:Languages\<Name>.isl`. The seven
here have no official Inno translation, so they are vendored from the
[`Unofficial`](https://github.com/jrsoftware/issrc/tree/main/Files/Languages/Unofficial)
folder of `jrsoftware/issrc` and referenced by relative path instead.

| App locale | File | Targets | Notes |
|---|---|---|---|
| `el` | `Greek.isl` | 6.5.0+ | complete |
| `hr` | `Croatian.isl` | 6.5.0+ | complete |
| `id` | `Indonesian.isl` | 6.5.0+ | complete |
| `ms` | `Malaysian.isl` | 5.1.0+ | 83 of 281 messages missing |
| `ro` | `Romanian.isl` | 6.1.0+ | 23 of 281 messages missing |
| `sr` | `SerbianCyrillic.isl` | 6.5.0+ | complete |
| `vi` | `Vietnamese.isl` | 6.5.0+ | complete |

"Missing" means the file predates messages added in later Inno releases. This is
not a build failure: ISCC emits `A message named "X" has not been defined for the
"Y" language. Will use the English message from Default.isl.` and substitutes the
English text, so those wizards are partly English. The versions here are the
newest published at <https://jrsoftware.org/files/istrans/>.

`hi` (Hindi) has no Inno translation, official or unofficial — that wizard is
English.

## Updating

These are plain text files; keep their original encoding (UTF-8 with BOM) and do
not reformat them. Re-download from the `Unofficial` folder linked above, then
compare the `[Messages]` key set against the `Default.isl` of the Inno version
pinned in `.github/workflows/release.yml` to see what is still missing.

Upstream is licensed under the Inno Setup license, which permits redistribution;
see `THIRD-PARTY-LICENSES.md`.
