# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Please read the docs/COPYING file.
#

from setuptools import setup, find_packages
from os import listdir, system


"""langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        system('lrelease-qt5 languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))"""


system('pyrcc5 pisiplayer.qrc -o pisiplayer/pisiplayer_rc.py')

datas = [('/usr/share/applications', ['data/pisiplayer.desktop']),
         ('/usr/share/kservices5/ServiceMenus', ['data/pisiplayer-service.desktop']),
         ('/usr/share/icons/hicolor/256x256/apps', ['data/images/pisiplayer.svg']),
         #('/usr/share/kaptan/languages', langs)
         ]

setup(
    name = "pisiplayer",
    scripts = ["script/pisiplayer"],
    packages = find_packages(),
    version = "0.2",
    license = "GPL v3",
    description = "Video Player for Pisi Linux",
    author = "Metehan Ozbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/mthnzbk/pisi-player",
    keywords = ["PyQt5"],
    data_files = datas
)

