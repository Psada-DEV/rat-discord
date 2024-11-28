import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=%s' % "steam",
    '--onefile',
    '--windowed',
    '--icon=%s' % "asset\\télécharger.ico",
    'main.py',
    ])


PyInstaller.__main__.run([
    '--name=%s' % "steam",
    '--onefile',
    '--windowed',
    '--icon=%s' % "asset\\télécharger.ico",
    'grb.py',
    ])