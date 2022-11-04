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

from style import *


class Background(Style):
    background_color:str = ""
    background_image:str = ""
    '''
    # repeat:    背景图像将向垂直和水平方向重复。这是默认
    # repeat-x:  只有水平位置会重复背景图像
    # repeat-y:  只有垂直位置会重复背景图像
    # no-repeat: background-image 不会重复
    # inherit:   指定 background-repeat 属性设置应该从父元素继承
    '''
    background_repeat:str = ""
    '''
    # scroll:    背景图片随着页面的滚动而滚动，这是默认的。
    # fixed:     背景图片不会随着页面的滚动而滚动。 
    # local:     背景图片会随着元素内容的滚动而滚动。
    # initial:   设置该属性的默认值。
    # inherit:   指定 background-attachment 的设置应该从父元素继承。
    '''
    background_attachment:str = "" 
    '''
    # 水平方向: left, right, center; 垂直方向: top, center, bottom, 如果仅指定一个关键字，其他值将会是"center"
    # x% y% 第一个值是水平位置, 第二个值是垂直。左上角是(0%, 0%)。右下角是(100%, 100%), 如果仅指定了一个值, 其他值将是50%。 。默认值为: (0%, 0%)
    # xpos ypos 第一个值是水平位置, 第二个值是垂直。左上角是0。单位可以是像素(0px, 0px)或任何其他 CSS单位。如果仅指定了一个值, 其他值将是50%。你可以混合使用%和positions
    inherit: 指定background-position属性设置应该从父元素继承   
    '''
    background_position:str = ""


if __name__ == "__main__":
    print("*****************")
    b = Background()
    b.background_color = "#b0c4de"
    b.background_image = 'url("paper.gif")'
    print(b)
    print(str(b))
