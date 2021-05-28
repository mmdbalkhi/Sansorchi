from __future__ import unicode_literals
from os import system

__VERSION__ = str(system ("git describe --exact-match --abbrev=0"))
