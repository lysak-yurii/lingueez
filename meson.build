project('lingueez', version: '2.0.3', meson_version: '>= 0.59.0')

# Pure-Python app; no build step, install only.
app_id = 'app.lingueez.Lingueez'
pkgdir = get_option('prefix') / 'lingueez'
datadir = get_option('datadir')

install_subdir('app', install_dir: pkgdir)
install_subdir('locales', install_dir: pkgdir)
install_subdir('assets', install_dir: pkgdir)
install_data('main.py', install_dir: pkgdir)

install_data(
  'packaging/flatpak/lingueez.sh',
  install_dir: get_option('bindir'),
  rename: 'lingueez',
  install_mode: 'rwxr-xr-x',
)

install_data('packaging/flatpak/app.lingueez.Lingueez.desktop', install_dir: datadir / 'applications')
install_data('packaging/flatpak/app.lingueez.Lingueez.metainfo.xml', install_dir: datadir / 'metainfo')
install_data('packaging/flatpak/app.lingueez.Lingueez.png', install_dir: datadir / 'icons' / 'hicolor' / '512x512' / 'apps')
install_data('LICENSE.txt', install_dir: datadir / 'licenses' / app_id)
install_data('NOTICE', install_dir: datadir / 'licenses' / app_id)
