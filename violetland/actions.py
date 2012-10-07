#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "violetland-v%s" % get.srcVERSION()

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")
    pisitools.dosym("/usr/share/violetland/icon-light.png", "/usr/share/pixmaps/violetland.png")

    pisitools.dodoc("CHANGELOG", "README*")