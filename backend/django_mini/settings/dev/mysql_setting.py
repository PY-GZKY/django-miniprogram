#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# 暂时用和测试一样的redis
# 报错: mysqlclient 1.3.13 or newer is required; you have 0.9.3
# 解决办法:
https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required

"""

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_miniprogram',
        'HOST': os.getenv('MYSQL_HOST', None),
        'PORT': os.getenv('MYSQL_PORT', 3306),
        'USER': os.getenv('MYSQL_USERNAME', None),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', None),
    },
}
