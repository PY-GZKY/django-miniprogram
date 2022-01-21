# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 15:48
import bson
import json
import decimal
import datetime
from typing import Union

from django.db.models.fields.files import ImageFieldFile


def _alchemy_encoder(obj):
    """
    处理序列化中的时间和小数
    """
    if isinstance(obj, datetime.date):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, bson.ObjectId):
        return str(obj)
    elif isinstance(obj, ImageFieldFile):
        return str(obj)


def serialize_sqlalchemy_obj(obj) -> Union[dict, list]:
    """
    序列化对象
    """
    if isinstance(obj, list):
        return json.loads(json.dumps([dict(r) for r in obj], default=_alchemy_encoder))
    else:
        return json.loads(json.dumps(dict(obj), default=_alchemy_encoder))