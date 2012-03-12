#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "SymbolType-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

