#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile", "(cat pogo.py) \| \$\(CONFIGURE_IN\)( > pogo;)", r"\1\2")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("NEWS", "COPYING", "README")
