#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   font
@Time    :   2022/11/04 09:33:32
@Author  :   Yqx 
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

import sys
sys.path.append( "" if hasattr(sys, "_MEIPASS") else __file__[0:__file__.index("Src")] )

from Src.Css.Base import *


class Font(Style):
    def __init__(self) -> None:
        super().__init__()
        self.font:str = ""
        '''
        描述: 可设置的属性是（按顺序）: "font-style font-variant font-weight font-size/line-height font-family" \n
        例如: font-size和font-family的值是必需的。如果缺少了其他值, 默认值将被插入, 如果有默认值的话。
        '''
        self.font_family:str = ""
        '''
        描述: 指定文本的字体系列 \n
        例如: p { font-family:"Times New Roman",Georgia,Serif; }
        '''
        self.font_size:str = ""
        '''
        描述: 指定文本的字体大小 \n
            *medium: 默认值/xx-small,x-small,small,large,x-large,xx-large \n
            *smaller/larger \n
            *length: 把 font-size 设置为一个固定的值。\n
            *%: 把 font-size 设置为基于父元素的一个百分比值。\n
        例如: h1 { font-size:250% } \n
             h2 { font-size: larger; } \n
             h3 { font-size: xx-large; } \n
             h4 { font-size: 12px; }
        '''
        self.font_style:str = ""
        '''
        描述: 指定文本的字体样式 \n
            *normal: 默认值。浏览器显示一个标准的字体样式。\n
            *italic: 浏览器会显示一个斜体的字体样式。\n
            *oblique: 浏览器会显示一个倾斜的字体样式。\n
            *inherit: 规定应该从父元素继承字体样式。\n
        例如: p.italic {font-style:italic}
        '''
        self.font_variant:str = ""
        '''
        描述: 以小型大写字体或者正常字体显示文本。\n
            *normal: 默认值。浏览器会显示一个标准的字体。\n
            *small-caps: 浏览器会显示小型大写字母的字体。\n
        例如: p.small { font-variant:small-caps; }
        '''
        self.font_weight:str = ""    
        '''
        描述: 指定字体的粗细。\n
            *normal: 默认值。定义标准的字符。bold/bolder/lighter \n
            *100~900: 定义由细到粗的字符。400 等同于 normal,而 700 等同于 bold。\n
        例如: p.thicker { font-weight:900; }
        '''