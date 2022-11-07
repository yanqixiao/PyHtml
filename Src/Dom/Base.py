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


class Title(Dom):
    '''
    描述: 为文档定义一个标题
    例如: <title>文档标题</title>
    '''
    def __init__(self) -> None:
        super().__init__()


class Body(Dom):
    '''
    描述: 定义文档的主体
    '''
    def __init__(self) -> None:
        super().__init__()


class H(Dom):
    '''
    描述: 定义 HTML 标题
    例如: <h1>这是标题 1</h1>
    '''
    def __init__(self, _num:int) -> None:
        '''
        描述: _num: 取值1~6, 对应h1~h6
        '''
        super().__init__()
        if _num not in list(range(1, 7)):
            raise ValueError(f"{_num}不在取值范围[1~6]内!")
        self._num = _num
        '''
        描述: 取值1~6, 对应h1~h6
        '''
        self._align:str = ""
        '''
        描述: 规定标题中文本的排列。\n
            *left/center/right/justify \n
        例如: <h1 align="center">这是标题 1</h1>
        '''
        self._specialKeys.append("_num")

    def __str__(self) -> str:
        _str = super().__str__()
        _tagName = type(self).__name__.lower()
        _tagNameNew = f"{type(self).__name__.lower()}{self._num}"
        return _str.replace(f"</{_tagName}>", f"</{_tagNameNew}>").replace(f"<{_tagName}>", f"<{_tagNameNew}>")


class P(Dom):
    '''
    描述: 标签定义段落
    例如: <p>这是一个段落。</p>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._align:str = ""
        '''
        描述: 规定标题中文本的排列。\n
            *left/center/right/justify \n
        例如: <p align="center">这是标题 1</p>
        '''


class Br(Dom):
    '''
    描述: 定义简单的折行。
    例如: <p> 使用 br 元素<br>在文本中<br>换行。 </p>
    '''
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        _str = super().__str__()
        _tagName = type(self).__name__.lower()
        return _str.replace(f"</{_tagName}>", "")
        

class Hr(Dom):
    '''
    描述: 定义水平线
    例如: 
        <h1>HTML</h1>
        <p>HTML 是用于描述 web 页面的一种语言。</p>
        <hr>
        <h1>CSS</h1>
        <p>CSS 定义如何显示 HTML 元素。</p>
    '''
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        _str = super().__str__()
        _tagName = type(self).__name__.lower()
        return _str.replace(f"</{_tagName}>", "")


if __name__ == "__main__":
    body = Body()
    et = WindowEvent()
    et._onafterprint = "showMsg()"
    et._onfocus = "alert()"
    body._events.append(et)
    print(body)

    br = Br()
    print(br)

    hr = Hr()
    print(hr)

    h1 = H(1)
    h1._text = "test h1"
    print((h1._class).__annotations__)

    p = P()
    p._text = "test p"
    print(p)