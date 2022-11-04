#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dom.py
@Time    :   2022/11/04 14:22:44
@Author  :   Yqx 
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib


from typing import Dict


class Base:

    def __init__(self) -> None:
        self._id:str = ""
        self._lang:str = ""
        self._style:str = ""
        self._title:str = ""
        self._dir:str = ""
        self._class:str = ""
        self._content = None

    def __str__(self) -> str:
        _tag = type(self).__name__.lower()
        _arg = {_key.replace("_", ""): _value for _key, _value in self.__dict__.items() if _key != "_content"}
        _sub = ""
        if self._content:
            if isinstance(self._content, list):
                for _it in self._content:
                    _sub += str(_it)
            else:
                _sub = self._content
        _ret = " ".join([f'''{_key}="{_value}"''' for _key, _value in _arg.items() if len(_value) > 0])
        return f"<{_tag} {_ret}>{_sub}</{_tag}>"