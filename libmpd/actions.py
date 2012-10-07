#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
WorkDir = "libmpd-0.19.96"
def setup():
    autotools.configure( "--prefix=/usr")
def build():
    autotools.make()

def install():
  autotools.install()
 
  pisitools.dodoc("NEWS", "COPYING", "README", "AUTHORS")
