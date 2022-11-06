#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   background.py
@Time    :   2022/11/04 09:30:19
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


class Background(Style):
    def __init__(self) -> None:
        super().__init__()
        self.background:str = ""
        '''
        描述: 简写属性，作用是将背景属性设置在一个声明中。
            bg-color bg-image position/bg-size bg-repeat bg-origin bg-clip bg-attachment initial|inherit;
        例如: body
            { 
                background: #00ff00 url('smiley.gif') no-repeat fixed center; 
            }
        '''
        self.background_color:str = ""
        '''
        描述: 设置元素的背景颜色
            *color: 指定背景颜色。在CSS颜色值近可能的寻找一个颜色值的完整列表。
            *transparent: 指定背景颜色应该是透明的。这是默认
            *inherit: 指定背景颜色，应该从父元素继承
        例如: p {background-color:#e0ffff;}
        '''
        self.background_image:str = ""
        '''
        描述: 把图像设置为背景。
            *url('URL'): 图像的URL
            *none: 无图像背景会显示。这是默认
            *linear-gradient(): 创建一个线性渐变的 "图像"(从上到下)
            *radial-gradient(): 用径向渐变创建 "图像"。 (center to edges)
            *repeating-linear-gradient(): 创建重复的线性渐变 "图像"
            *repeating-radial-gradient(): 创建重复的径向渐变 "图像"
            *inherit: 指定背景图像应该从父元素继承
        例如: body{ background-image:url('gradient2.png'); }
        '''
        self.background_repeat:str = ""
        '''
        描述: 设置背景图像是否及如何重复。
            *repeat: 背景图像将向垂直和水平方向重复。这是默认
            *repeat-x: 只有水平位置会重复背景图像
            *repeat-y: 只有垂直位置会重复背景图像
            *no-repeat: background-image 不会重复
            *inherit: 指定 background-repeat 属性设置应该从父元素继承
        例如: body{ background-image:url('img_tree.png'); background-repeat:no-repeat; }
        '''
        self.background_attachment:str = "" 
        '''
        描述: 背景图像是否固定或者随着页面的其余部分滚动。
            *scroll: 背景图片随着页面的滚动而滚动，这是默认的。
            *local: 背景图片会随着元素内容的滚动而滚动。
            *initial: 设置该属性的默认值。
            *fixed: 背景图片不会随着页面的滚动而滚动。 
            *inherit: 指定 background-attachment 的设置应该从父元素继承。
        例如: body
            { 
                background-image:url('smiley.gif');
                background-repeat:no-repeat;
                background-attachment:fixed;
            }
        '''
        self.background_position:str = ""
        '''
        描述: 设置背景图像的起始位置。
            *水平方向: left, right, center; 垂直方向: top, center, bottom, 如果仅指定一个关键字，其他值将会是"center"
            *x% y%: 第一个值是水平位置, 第二个值是垂直。左上角是(0%, 0%)。右下角是(100%, 100%), 如果仅指定了一个值, 其他值将是50%。 。默认值为: (0%, 0%)
            *xpos ypos: 第一个值是水平位置, 第二个值是垂直。左上角是0。单位可以是像素(0px, 0px)或任何其他 CSS单位。如果仅指定了一个值, 其他值将是50%。你可以混合使用%和positions
            *inherit: 指定background-position属性设置应该从父元素继承   
        例如: body
            {
                background-image:url('smiley.gif');
                background-repeat:no-repeat;
                background-attachment:fixed;
                background-position:center;
            }
        '''


if __name__ == "__main__":
    print("*****************")
    b = Background()
    b.background_color = "#b0c4de"
    b.background_image = 'url("paper.gif")'
    print(b)
    print(str(b))
