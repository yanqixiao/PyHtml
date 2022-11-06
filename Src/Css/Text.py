#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text.py
@Time    :   2022/11/04 09:32:16
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


class Text(Style):
    color:str = "" # 设置文本颜色
    '''
    # 设置文本方向
    # ltr: 默认。文本方向从左到右
    # rtl: 文本方向从右到左。
    # inherit: 规定应该从父元素继承 direction 属性的值。
    '''
    direction:str = "" 
    '''
    # 设置字符间距
    # normal: 默认。规定字符间没有额外的空间。
    # length: 定义字符间的固定空间（允许使用负值）例如: 2px, 3px
    # inherit: 规定应该从父元素继承 letter-spacing 属性的值。
    '''
    letter_spacing:str = ""
    '''
    # 设置行高
    # normal: 默认。设置合理的行间距。
    # number: 设置数字，此数字会与当前的字体尺寸相乘来设置行间距。
    # length: 设置固定的行间距。
    # %: 基于当前字体尺寸的百分比行间距。
    # inherit: 规定应该从父元素继承 line-height 属性的值。
    '''
    line_height:str = ""
    '''
    # 对齐元素中的文本
    # left: 把文本排列到左边。默认值：由浏览器决定。
    # right: 把文本排列到右边。
    # center: 把文本排列到中间。
    # justify: 实现两端对齐文本效果。
    # inherit: 规定应该从父元素继承 text-align 属性的值。
    '''
    text_align:str = ""
    '''
    # 向文本添加修饰
    # none: 默认。定义标准的文本。
    # underline: 定义文本下的一条线。
    # overline: 定义文本上的一条线。
    # line-through: 定义穿过文本下的一条线。
    # blink: 定义闪烁的文本。
    # inherit: 规定应该从父元素继承 text-decoration 属性的值。
    '''
    text_decoration:str = ""
    '''
    # 缩进元素中文本的首行
    # length: 定义固定的缩进。默认值: 0。
    # %: 定义基于父元素宽度的百分比的缩进。
    # inherit: 规定应该从父元素继承 text-indent 属性的值
    '''
    text_indent:str = ""
    '''
    # 设置文本阴影
    # h-shadow: 必需。水平阴影的位置。允许负值。
    # v-shadow: 必需。垂直阴影的位置。允许负值。
    # blur: 可选。模糊的距离。
    # color: 可选。阴影的颜色。参阅 CSS 颜色值。
    '''
    text_shadow:str = ""
    '''
    # 控制元素中的字母
    # none: 默认。定义带有小写字母和大写字母的标准的文本。
    # capitalize: 文本中的每个单词以大写字母开头。
    # uppercase: 定义仅有大写字母。
    # lowercase: 定义无大写字母，仅有小写字母。
    # inherit: 规定应该从父元素继承 text-transform 属性的值。
    '''
    text_transform:str = ""
    '''
    # 设置或返回文本是否被重写 
    # normal: 默认。不使用附加的嵌入层面。
    # embed: 创建一个附加的嵌入层面。
    # bidi-override: 创建一个附加的嵌入层面。重新排序取决于 direction 属性。
    # initial: 设置该属性为它的默认值。
    # inherit: 从父元素继承该属性。
    '''
    unicode_bidi:str = ""
    '''
    # 设置元素的垂直对齐
    # baseline: 默认。元素放置在父元素的基线上。
    # super: 垂直对齐文本的上标
    # top: 把元素的顶端与行中最高元素的顶端对齐。
    # text-top: 把元素的顶端与父元素字体的顶端对齐
    # middle: 使元素及其后代元素的底部与整行的底部对齐。
    # bottom: 把此元素放置在父元素的中部。
    # text-bottom: 把元素的底端与父元素字体的底端对齐。
    # length: 将元素升高或降低指定的高度，可以是负数。
    # %: 使用 "line-height" 属性的百分比值来排列此元素。允许使用负值。
    # inherit: 从父元素继承该属性。
    '''
    vertical_align:str = ""
    '''
    # 设置元素中空白的处理方式
    # normal: 默认。空白会被浏览器忽略。
    # pre: 空白会被浏览器保留。其行为方式类似 HTML 中的 <pre> 标签。
    # nowrap: 文本不会换行，文本会在在同一行上继续，直到遇到 <br> 标签为止。
    # pre-wrap: 保留空白符序列，但是正常地进行换行。
    # pre-line: 合并空白符序列，但是保留换行符。
    # inherit: 从父元素继承该属性。
    '''
    white_space:str = ""
    '''
    # 设置字间距
    # normal: 默认。定义单词间的标准空间。
    # length: 定义单词间的固定空间。
    # inherit: 从父元素继承该属性。
    '''
    word_spacing:str = ""