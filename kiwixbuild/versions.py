# This file reference all the versions of the depedencies we use in kiwix-build.

main_project_versions = {
    'libzim': '8.1.0',
    'libkiwix': '12.0.0',
    'kiwix-tools': '3.4.0',
    'zim-tools': '3.1.3',
    'kiwix-desktop': '2.3.1' # Also change KIWIX_DESKTOP_VERSION and KIWIX_DESKTOP_RELEASE in appveyor.yml
}

# This dictionnary specify what we need to build at each release process.
# - Values are integer or None
# - If a project is not in the dict (or None), the project is not released.
# - If release_versions[project] == 0, this is the first time the project is
#   build for this release, so publish src and build archives.
# - If release_versions[project] > 0, release only the build archive with a
#   build postfix.
# To change this dictionnary, use the following algorithm:
# - If project version change, set release_versions[project] = 0
# - Else
#    - If project depedencies have not change, set it to None and update the
#     `(was ...)`.
#    - Else, increment the value. If no value was present, see `(was ...)`.

# For kiwix-desktop, if this is not None:
# - set KIWIX_DESKTOP_RELEASE to 1
# - set KIWIX_DESKTOP_VERSION to the version of the release (including release_versions)
# If this is None:
# - set KIWIX_DESKTOP_RELEASE to 0

release_versions = {
    'libzim': 1, # Depends of base deps (was 0)
    'libkiwix': None, # Depends of libzim (was 1)
    'kiwix-tools': None, # Depends of libkiwix and libzim (was 1)
    'zim-tools': None, # Depends of libzim (was 2)
    'kiwix-desktop': None # Depends of libkiwix and libzim (was 1)
}


# This is the "version" of the whole base_deps_versions dict.
# Change this when you change base_deps_versions.
base_deps_meta_version = '79'

base_deps_versions = {
  'zlib' : '1.2.12',
  'lzma' : '5.2.6',
  'zstd' : '1.5.2',
  'docoptcpp' : '0.6.2',
  'uuid' : '1.43.4',
  'xapian-core' : '1.4.18',
  'mustache' : '4.1',
  'pugixml' : '1.2',
  'libmicrohttpd' : '0.9.72',
  'gumbo' : '0.10.1',
  'icu4c' : '58.2',
  'libaria2' : '1.36.0',
  'libmagic' : '5.35',
  'android-ndk' : 'r21e',
  'qt' : '5.10.1',
  'qtwebengine' : '5.10.1',
  'org.kde' : '5.15-21.08',
  'io.qt.qtwebengine' : '5.15-21.08',
  'zim-testing-suite': '0.3',
}
