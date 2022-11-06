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

from styleSheets import *


class Font(Style):
    '''
    # 可设置的属性是（按顺序）: "font-style font-variant font-weight font-size/line-height font-family"
    # font-size和font-family的值是必需的。如果缺少了其他值, 默认值将被插入, 如果有默认值的话。
    '''
    font:str = ""
    '''
    # 指定文本的字体系列
    '''
    font_family:str = ""
    '''
    # medium: 默认值/xx-small,x-small,small,large,x-large,xx-large
    # smaller/larger
    # length: 把 font-size 设置为一个固定的值。
    # %: 把 font-size 设置为基于父元素的一个百分比值。
    '''
    font_size:str = ""
    '''
    # normal: 默认值。浏览器显示一个标准的字体样式。
    # italic: 浏览器会显示一个斜体的字体样式。
    # oblique: 浏览器会显示一个倾斜的字体样式。
    # inherit: 规定应该从父元素继承字体样式。
    '''
    font_style:str = ""
    '''
    # normal: 默认值。浏览器会显示一个标准的字体。
    # small-caps: 浏览器会显示小型大写字母的字体。
    '''
    font_variant:str = ""
    '''
    # normal: 默认值。定义标准的字符。bold/bolder/lighter
    # 100~900: 定义由细到粗的字符。400 等同于 normal，而 700 等同于 bold。
    '''
    font_weight:str = ""