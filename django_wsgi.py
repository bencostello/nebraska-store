#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

# В проекте используется версия Django, установленная в Virtualenv.

# Добавьте нужные вам пути поиска.
# Если вы получаете ошибку 500 Internal Server Error,
# скорее всего проблема именно в путях поиска.

sys.path.insert(0, '/home/hosting_lumberjack85/projects/nebraska-store/app')
sys.path.insert(0, '/home/hosting_lumberjack85/projects/nebraska-store')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# ------ Ниже этой линии изменения скорее всего не нужны --------

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
