# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Format.py
@Time    :   2022/11/07 05:31:52
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


class Abbr(Dom):
    '''
    描述: 定义一个缩写 \n
    例如: The<abbr title="World Health Organization">WHO</abbr> was founded in 1948.
    '''
    def __init__(self) -> None:
        super().__init__()


class Address(Dom):
    '''
    描述: 定义文档作者或拥有者的联系信息。\n
    例如: 
        <address>
            Written by <a href="mailto:webmaster@example.com">Jon Doe</a>.<br> 
            Visit us at:<br>
            Example.com<br>
            Box 564, Disneyland<br>
            USA
        </address>
    '''
    def __init__(self) -> None:
        super().__init__()


class B(Dom):
    '''
    描述: 定义粗体文本。\n
    例如: <p>这是一个普通的文本- <b>这是一个加粗文本</b>。</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Bdo(Dom):
    '''
    描述: 定义文本的方向。\n
    例如: <p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._dir:str = ""
        '''
        描述: 规定 <bdo> 元素内的文本方向。
            *ltr: 从左至右(默认)
            *rtl: 从右至左
        例如: <p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
        '''


class Big(Dom):
    '''
    描述: 定义大号文本。\n
    例如: <p><big>这个文本比较大。</big></p>
    '''
    def __init__(self) -> None:
        super().__init__()

