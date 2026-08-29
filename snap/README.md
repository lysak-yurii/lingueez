# Snap packaging

The snap exists for one reason: **Ubuntu's App Center lists the Snap Store**, and
nothing else. It does not list Flathub, and its Debian support covers only packages
from the Ubuntu archive. Publishing here is the only way to appear in the store that
ships on every Ubuntu desktop.

Use the **full `PySide6` wheel**, not `PySide6-Essentials`: `app/ui/reader.py`
imports QtMultimedia at module scope and that module ships in PySide6-Addons.
Essentials builds and packs without complaint, then the app dies at startup with
`ModuleNotFoundError: No module named 'PySide6.QtMultimedia'`.

`snapcraft.yaml` builds from the local checkout (like the Flatpak's
`app.lingueez.Lingueez.yml`), reusing the repo-root `meson.build` install — the same
app tree, desktop entry, icon and AppStream metadata the Flatpak ships. Only the
launcher differs: the Flatpak's hardcodes `/app`, the snap's points at `$SNAP/usr`.

## Build locally

Releases are built by CI on the tag (below); build here to test confinement.

```bash
sudo snap install snapcraft --classic
sudo snap install lxd && sudo lxd init --auto   # build backend
snapcraft
```

Build from a **clean worktree**, not the working tree: `source: .` copies the whole
directory per part, and `ffmpeg/` plus `backups/` push that past 1.3 GB even though
both are gitignored. Tracked content is ~150 MB.

```bash
git worktree add /tmp/lingueez-snap v2.0.9 && cd /tmp/lingueez-snap && snapcraft
```

## Install and connect

`password-manager-service` is not auto-connected, so the keyring is unavailable
until the user connects it (the app falls back to its encrypted local session file
until then — see `app/core/secure_store.py`):

```bash
sudo snap install --dangerous ./lingueez_*.snap
sudo snap connect lingueez:password-manager-service
sudo snap connect lingueez:removable-media
```

`removable-media` is the second manual one: `home` grants only `$HOME`, so importing
or exporting against a drive mounted under `/media` or `/mnt` fails with EACCES
without it.

## Verify confinement

AppArmor denials are silent inside the app, so watch for them explicitly while
exercising every feature — add a word, read aloud, sync, log in, toggle autostart,
export, open the diagnostics bundle:

```bash
sudo snap install snappy-debug
snappy-debug        # in a second terminal, while the app runs
```

Test on **both a Wayland and an X11 session** — the hotkey and window-icon paths
differ between them.

## What the snap changes in the app

Snap-confined behaviour is detected at runtime via `package_env.is_snap()`, the same
shape as `is_msix()` / `is_flatpak()`. It is not enough to test `$SNAP`: child
processes inherit snapd's variables, so anything launched from a snapped terminal
(VS Code ships as a classic snap) sees them — an AppImage started that way would
have put its database under `~/snap/code/common`. `is_snap()` therefore also
requires the app tree to live inside that `$SNAP` mount, and **every** `SNAP_*`
read goes through it rather than reading the variable directly. Covered by
`tests/test_snap_env.py`, which fakes both snapd's environment and the leaked one —
no snapd needed.

| Area | Why it differs | Where |
| --- | --- | --- |
| Data dir | `XDG_DATA_HOME` points into the revisioned `$SNAP_USER_DATA`, which snapd copies on every refresh; the DB and `backups/` must not live there | `main.py`, `_user_data_dir` |
| Autostart | The `home` interface denies `~/.config`; snapd reads `$SNAP_USER_DATA/.config/autostart` and matches the filename against the app's `autostart:` key | `app/system/autostart.py` |
| Autostart command | `$SNAP` carries the revision and changes on refresh, so the entry records `/snap/bin/lingueez` | `app/system/autostart.py` |
| Global hotkey | Reported unavailable on Wayland (see below) | `app/system/hotkey_env.py` |
| Update affordances | snapd refreshes the app, so the GitHub update check and its toggle are hidden, as on the Microsoft Store build | `app/ui/main_window.py`, `settings_dialog.py` |
| Window icon | Snapcraft installs the desktop entry as `<instance>_lingueez.desktop`; Wayland matches windows to launchers by that name | `main.py` |

## Known follow-ups

- **Global hotkey on Wayland.** It is reported unavailable, exactly as under
  Flatpak, and Settings offers the AppImage as the remedy. The GNOME
  custom-keybinding fallback *may* actually work here — the `gnome` extension plugs
  `gsettings` — but that needs proving on a real build (dconf write access, plus a
  keybinding command of `/snap/bin/lingueez --add-word` rather than the in-snap
  path). Until it is proven, do not advertise it: the same rule the unimplemented
  GlobalShortcuts portal follows.
- **`password-manager-service` auto-connection.** Worth a store request at
  <https://forum.snapcraft.io/c/store-requests> so users don't need `snap connect`.
- **`python3-venv` in `stage-packages`.** There to guarantee an interpreter; drop it
  if a build shows core24 already provides python3.12.

## Publish

`release.yml` builds the snap on every `v*` tag and leaves it as the `linux-snap` CI
artifact, not a Release asset — same as the Store MSIX. Upload the artifact from the
tag's run:

```bash
snapcraft login
snapcraft register lingueez          # once
snapcraft upload --release=edge lingueez_*.snap
snapcraft release lingueez <rev> stable
```

Snapcraft's own build service (the Builds tab) triggers on a push to `main`, not on a
tag. Version comes from the metainfo via `adopt-info`, so edge would fill with
revisions all reporting the same version, differing only in what sat on `main` at the
time. Building on the tag avoids matching revisions back to commits by hand.

Then fill the store listing at <https://snapcraft.io/lingueez/listing> — App Center
renders it verbatim, including the screenshots (use the same set as the Flathub and
Store listings, `docs/assets/shots/`). Install counts are visible only to the
publisher: `snapcraft metrics lingueez --name weekly_installed_base --format table`.
