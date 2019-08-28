# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import os


APP_KEY = ''
APP_SECRET = ''

try:
    from local_settings import *
except ImportError:
    pass
