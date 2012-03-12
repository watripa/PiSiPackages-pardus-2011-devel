#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir  = "bsddb3-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install("--berkeley-db=/usr")

