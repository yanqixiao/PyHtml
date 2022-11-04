#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   div.py
@Time    :   2022/11/04 14:30:19
@Author  :   Yqx 
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

from base import *


class Div(Base):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    d = Div()
    d._id = "123"
    d._class = "test"
    d1 = Div()
    d1._id="d1"
    d._content = [d1]
    print(d)
