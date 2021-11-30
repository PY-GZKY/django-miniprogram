#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from .base_setting import *

ENV = os.getenv('ENV', '')
if ENV:
    print("正式环境启动")
    DEBUG = False
    # 生产模式建议把  SECRET_KEY 存环境变量 或者服务器固定目录文件读取
    SECRET_KEY = 'qw^23423f+0=-23(!@#523^))*)*'
    from .production import *
else:
    print("开发环境启动")
    DEBUG = True
    SECRET_KEY = 'z%-==3kv(&k%(@)%f@9e8h9^z*goa$urn$6)z6sh'
    from .dev import *
