# -*- coding: utf-8 -*-
import os.path

with open(os.path.join(os.path.dirname(__file__), "VERSION"), 'r') as vf:
    __version__ = vf.read().strip()
