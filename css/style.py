#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   style.py
@Time    :   2022/11/04 09:42:10
@Author  :   Yqx 
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

from typing import Dict


class Style:
    def __str__(self) -> str:
        _cls = type(self)
        _annotation: Dict = _cls.__annotations__
        _errTypeStr = ",".join(_key for _key, _type in _annotation.items() if _type is not str)
        if len(_errTypeStr) > 0:
            raise ValueError(f"{_cls}中属性{_errTypeStr}类型错误!")
        _dct = {_key.replace('_', '-'): getattr(self, _key) for _key in _annotation.keys()}
        _ret = [f'''{_key}:{_value.replace('"', "'")}''' for _key, _value in _dct.items() if len(_value) > 0]
        return "; ".join(_ret)