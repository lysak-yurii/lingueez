# Vendored Inno Setup wizard translations

`lingueez.iss` gives the Windows installer a wizard language for every locale the
app ships (`locales/<code>.py`). Inno Setup bundles most of them in its own
`Languages\` folder, referenced as `compiler:Languages\<Name>.isl`. The eight
here are not in the `Languages\` folder of the Inno version pinned in
`.github/workflows/release.yml`, so they are vendored from the
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
| `zh` | `ChineseSimplified.isl` | 6.5.0+ | complete |

Chinese is the one to watch: it *is* an official translation on `issrc` `main`,
but it was promoted into `Files/Languages/` only after 6.7.1, so
`compiler:Languages\ChineseSimplified.isl` does not resolve against the pinned
compiler and the build fails outright. This copy is taken from the `is-6_7_1`
tag's `Unofficial/` folder, so its message set matches that compiler exactly.
When the pinned Inno version moves past the release that ships Chinese
officially, this file can be dropped for `compiler:Languages\`.

"Missing" means the file predates messages added in later Inno releases. This is
not a build failure: ISCC emits `A message named "X" has not been defined for the
"Y" language. Will use the English message from Default.isl.` and substitutes the
English text, so those wizards are partly English. The versions here are the
newest published at <https://jrsoftware.org/files/istrans/>.

`hi` (Hindi) has no Inno translation, official or unofficial — that wizard is
English.

## Updating

These are plain text files; keep their original encoding and do not reformat
them. Like the .isl files Inno itself ships, they are UTF-8 *without* a BOM and
declare their `LanguageCodePage`; store them with CRLF endings, as upstream
does. Re-download from the `Unofficial` folder linked above — pinning the URL to
the `is-<version>` tag matching the pinned compiler — then compare the
`[Messages]` key set against that version's `Default.isl` to see what is
missing. A key the pinned `Default.isl` does *not* have is a compile error, not
a warning, so never take a file from a newer Inno than the one CI installs.

Upstream is licensed under the Inno Setup license, which permits redistribution;
see `THIRD-PARTY-LICENSES.md`.
