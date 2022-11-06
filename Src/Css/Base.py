# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Base.py
@Time    :   2022/11/06 07:21:35
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib


class Style:
    def __str__(self) -> str:
        _ret = [f'''{_key.replace('_', '-')}:{_value.replace('"', "'")}''' for _key, _value in self.__dict__.items() if len(_value) > 0]
        return "; ".join(_ret) + ";"