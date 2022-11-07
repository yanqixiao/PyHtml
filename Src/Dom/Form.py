# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Form.py
@Time    :   2022/11/06 20:11:30
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


class Form(Dom):
    '''
    描述: 定义一个 HTML 表单，用于用户输入。\n
    例如: <form action="demo_form.php" method="get">
            First name: <input type="text" name="fname"><br>
            Last name: <input type="text" name="lname"><br>
            <input type="submit" value="提交">
        </form>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._accept:str = ""
        '''
        描述: 规定服务器接收到的文件的类型。（文件是通过文件上传提交的）\n
            *MIME_type: 允许被提交/被上传的一个或多个 MIME 类型。如需规定多个 MIME 类型，请使用逗号分隔它们。\n
        例如: <form action="form_action.html" accept="image/gif,image/jpeg"></form>
        '''
        self._accept_charset:str = ""
        '''
        描述: 规定服务器可处理的表单数据字符集。\n
            *表单提交时使用的字符编码列表，多个字符编码使用空格分隔。\n
                *UTF-8 - Unicode 字符编码 \n
                *ISO-8859-1 - 拉丁字母表的字符编码 \n
        例如: <form action="demo_form.html" accept-charset="ISO-8859-1"></form>
        '''
        self._action:str = ""
        '''
        描述: 规定当提交表单时向何处发送表单数据。\n
            *URL: 当表单提交时向何处发送表单数据.\n
                *绝对 URL - 指向另一个网站（比如 action="http://www.example.com/example.htm"）\n
                *相对 URL - 指向网站内的一个文件（比如 action="example.htm"）\n
        例如: <form action="demo_form.html" method="get"></form>
        '''
        self._autocomplete:str = ""
        '''
        描述: 规定是否启用表单的自动完成功能。\n
            *on: 默认。规定启用自动完成功能。浏览器会基于用户之前键入的值自动完成值。\n
            *off: 规定禁用自动完成功能。用户必须在每次使用时输入值到每个字段中，浏览器不会自动完成输入。\n
        例如: <form action="demo_form.html" method="get" autocomplete="on"></form>
        '''
        self._enctype:str = ""
        '''
        描述: 规定在向服务器发送表单数据之前如何对其进行编码。（适用于 method="post" 的情况）\n
            *application/x-www-form-urlencoded: 默认。在发送前对所有字符进行编码（将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值）。\n
            *multipart/form-data: 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。\n
            *text/plain: 将空格转换为 "+" 符号，但不编码特殊字符。\n
        例如: <form action="demo_post_enctype.html" method="post" enctype="multipart/form-data"></form>
        '''
        self._method:str = ""
        '''
        描述: 规定用于发送表单数据的 HTTP 方法 \n
            *get: 默认。将表单数据（form-data）以名称/值对的形式附加到 URL 中：URL?name=value&name=value。\n
            *post: 以 HTTP post 事务的形式发送表单数据（form-data）。\n
        例如: <form action="demo_post_enctype.html" method="post" enctype="multipart/form-data"></form>
        '''
        self._name:str = ""
        '''
        描述: 规定表单的名称。\n
            *text: 规定表单的名称。\n
        例如: <form action="demo_post_enctype.html" method="post" enctype="multipart/form-data" name="myform"></form>
        '''
        # self._novalidate:str = ""
        # '''
        # 描述: 如果使用该属性，则提交表单时不进行验证。\n
        # 例如: <form action="demo_form.html" novalidate></form>
        # '''
        self._target:str = ""
        '''
        描述: 规定在何处打开 action URL。\n
            *_blank: 在新窗口/选项卡中打开。\n
            *_self: 在同一框架中打开。（默认）\n
            *_parent: 在父框架中打开。\n
            *_top: 在整个窗口中打开。\n
            *framename: 在指定的 iframe 中打开。\n
        例如: <form action="demo_form.html" method="get" target="_blank"></form>
        '''



class Input(Dom):
    '''
    描述: 定义一个输入控件
    例如: <input type="text" name="fname"><br>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._accept:str = ""
        '''
        描述: 规定通过文件上传来提交的文件的类型。 (只针对type="file")\n
            *audio/*: 接受所有的声音文件。\n
            *video/*: 接受所有的视频文件。\n
            *image/*: 接受所有的图像文件。\n
            *MIME_type: 一个有效的 MIME 类型，不带参数。\n
        例如: <input type="file" name="pic" accept="image/*">
        '''
        self._align:str = ""
        '''
        描述: 规定图像输入的对齐方式。 (只针对type="image")\n
            *left: 左对齐图像（默认）\n
            *right: 右对齐对象。\n
            *top: 上对齐图像。\n
            *middle: 居中对齐图像。\n
            *bottom: 下对齐图像。\n
        例如: <input type="image" src="submit.gif" alt="Submit" align="right" width="48" height="48">
        '''
        self._alt:str = ""
        '''
        描述: 定义图像输入的替代文本。 (只针对type="image")\n
            *text: 规定图像的替代文本。\n
        例如: <input type="image" src="submit.gif" alt="Submit" align="right" width="48" height="48">
        '''
        self._autocomplete:str = ""
        '''
        描述: 规定是否启用表单的自动完成功能。\n
            *on: 默认。规定启用自动完成功能。浏览器会基于用户之前键入的值自动完成值。\n
            *off: 规定禁用自动完成功能。用户必须在每次使用时输入值到每个字段中，浏览器不会自动完成输入。\n
        例如: <form action="demo_form.html" autocomplete="on">
                First name:<input type="text" name="fname"><br>
                Last name: <input type="text" name="lname"><br>
                E-mail: <input type="email" name="email" autocomplete="off"><br>
                <input type="submit">
             </form>
        '''
        self._autofocus:str = ""
        '''
        描述: 属性规定当页面加载时 <input> 元素应该自动获得焦点。\n
            *true: 开启。\n
            *不定义则关闭 \n
        例如: <input type="text" name="fname" autofocus>
        '''
        self._checked:str = ""
        self._disabled:str = ""
        self._form:str = ""
        self._formaction:str = ""
        self._formenctype:str = ""
        self._formmethod:str = ""
        self._formnovalidate:str = ""
        self._formtarget:str = ""
        self._height:str = ""
        self._list:str = ""
        self._max:str = ""
        self._maxlength:str = ""
        self._min:str = ""
        self._multiple:str = ""
        self._name:str = ""
        self._pattern:str = ""
        self._placeholder:str = ""
        self._readonly:str = ""
        self._required:str = ""
        self._size:str = ""
        self._src:str = ""
        self._step:str = ""
        self._type:str = ""
        self._value:str = ""
        self._width:str = ""


