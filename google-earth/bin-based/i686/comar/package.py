#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system ("/usr/bin/download-googleearth")

def preRemove():
    os.system ("/usr/lib/googleearth/uninstall")
