import PyInstaller.__main__


def r():
    PyInstaller.__main__.run([
        '--name=%s' % "steam",
        '--onefile',
        '--windowed',
        '--icon=%s' % "asset\\télécharger.ico",
        'main.py',
        ])
r()


def rs():
    PyInstaller.__main__.run([
        '--name=%s' % "gb",
        '--onefile',
        '--windowed',
        '--icon=%s' % "asset\\télécharger.ico",
        'grb.py',
        ])

