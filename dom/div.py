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

from tag import *


class Div(Tag):
    def __init__(self) -> None:
        super().__init__()
        self._align:str = ""
        '''
        描述: 规定 <div> 元素中的内容的对齐方式 \n
            *left: 左对齐内容; \n
            *right: 右对齐内容; \n
            *center: 居中对齐内容; \n
            *justify: 对行进行伸展，这样每行都可以有相等的长度（就像在报纸和杂志中）\n
        例如: <div align="center">这是一些文本!</div>
        '''


if __name__ == "__main__":
    d = Div()
    d._accesskey = "c"
    d.id = "123"
    d._class = "test"
    d1 = Div()
    d1._id="d1"
    d1._text = "dfadsfasfsdf"
    d._tags = [d1]
    print(d)
