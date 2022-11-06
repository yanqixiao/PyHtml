# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Base.py
@Time    :   2022/11/06 20:18:05
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

import sys
sys.path.append( "" if hasattr(sys, "_MEIPASS") else __file__[0:__file__.index("Src")] )

from Src.Dom.Dom import *
from Src.Dom.Event import WindowEvent


class Body(Dom):
    def __init__(self) -> None:
        super().__init__()
        self._events:List[WindowEvent] = []

    def __str__(self) -> str:
        _tag = type(self).__name__.lower()
        _arg = {_key.replace("_", ""): _value for _key, _value in self.__dict__.items() if _key not in ["_text", "_tags", "_events"]}
        _sub = self._text if self._text else ""
        _sub += ''.join(str(_tag) for _tag in self._tags)
        _vnt = " ".join(str(_event) for _event in self._events)
        _ret = " ".join([f'''{_key}="{_value}"''' for _key, _value in _arg.items() if len(_value) > 0])
        return f"<{_tag} {_ret} {_vnt}>{_sub}</{_tag}>"
