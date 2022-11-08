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
        描述: 规定服务器接收到的文件的类型。（文件是通过文件上传提交的)\n
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
                *绝对 URL - 指向另一个网站（比如 action="http://www.example.com/example.htm")\n
                *相对 URL - 指向网站内的一个文件（比如 action="example.htm")\n
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
        描述: 规定在向服务器发送表单数据之前如何对其进行编码。（适用于 method="post" 的情况)\n
            *application/x-www-form-urlencoded: 默认。在发送前对所有字符进行编码（将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值)。\n
            *multipart/form-data: 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。\n
            *text/plain: 将空格转换为 "+" 符号，但不编码特殊字符。\n
        例如: <form action="demo_post_enctype.html" method="post" enctype="multipart/form-data"></form>
        '''
        self._method:str = ""
        '''
        描述: 规定用于发送表单数据的 HTTP 方法 \n
            *get: 默认。将表单数据（form-data)以名称/值对的形式附加到 URL 中：URL?name=value&name=value。\n
            *post: 以 HTTP post 事务的形式发送表单数据（form-data)。\n
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
            *_self: 在同一框架中打开。（默认)\n
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
            *left: 左对齐图像（默认)\n
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
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: <input type="text" name="fname" autofocus="true">
        '''
        self._checked:str = ""
        '''
        描述: checked 属性规定在页面加载时应该被预先选定的 <input> 元素。 (只针对 type="checkbox" 或者 type="radio")\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: <input type="checkbox" name="vehicle" value="Car" checked="true"> I have a car<br>
        '''
        self._disabled:str = ""
        '''
        描述: disabled 属性规定应该禁用的 <input> 元素。\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: Last name: <input type="text" name="lname" disabled="true"><br>
        '''
        self._form:str = ""
        '''
        描述: form 属性规定 <input> 元素所属的一个或多个表单。\n
            *form_id: 规定 <input> 元素所属的一个或多个表单的 id 列表，以空格分隔。\n
        例如: <form action="demo-form.php" id="form1"></form>
             Last name: <input type="text" name="lname" form="form1">
        '''
        self._formaction:str = ""
        '''
        描述: 属性规定当表单提交时处理输入控件的文件的 URL。(只针对 type="submit" 和 type="image")\n
            *URL: 规定当表单提交时处理输入控件的文件的 URL。\n
                *绝对 URL - 某个页面的完整地址（比如 href="http://www.example.com/formresult.html")\n
                *相对 URL - 指向当前站点内的一个文件（比如 href="formresult.html")\n
        例如: <input type="submit" formaction="demo-admin.php" value="提交">
        '''
        self._formenctype:str = ""
        '''
        描述: 属性规定当表单数据提交到服务器时如何编码(只适合 type="submit" 和 type="image")。\n
            *application/x-www-form-urlencoded: 默认。在发送前对所有字符进行编码（将空格转换为 "+" 符号，特殊字符转换为 ASCII HEX 值)。\n
            *multipart/form-data: 不对字符编码。当使用有文件上传控件的表单时，该值是必需的。\n
            *text/plain: 将空格转换为 "+" 符号，但不编码特殊字符。\n
        例如: <input type="submit" formenctype="multipart/form-data" value="以 Multipart/form-data 提交">
        '''
        self._formmethod:str = ""
        '''
        描述: 定义发送表单数据到 action URL 的 HTTP 方法。 (只适合 type="submit" 和 type="image")。\n
            *get: 默认。将表单数据（form-data)以名称/值对的形式附加到 URL 中：URL?name=value&name=value。\n
            *post: 以 HTTP post 事务的形式发送表单数据（form-data)。\n
        例如: <input type="submit" formmethod="post" formaction="demo-post.php" value="使用 POST 提交">
        '''
        self._formnovalidate:str = ""
        '''
        描述: formnovalidate 属性覆盖 <form> 元素的 novalidate 属性。\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: <input type="submit" formnovalidate="formnovalidate" value="不验证提交">
        '''
        self._formtarget:str = ""
        '''
        描述: 规定表示提交表单后在哪里显示接收到响应的名称或关键词。(只适合 type="submit" 和 type="image")\n
            *_blank: 在新窗口/选项卡中打开。\n
            *_self: 在同一框架中打开。（默认)\n
            *_parent: 在父框架中打开。\n
            *_top: 在整个窗口中打开。\n
            *framename: 在指定的 iframe 中打开。\n
        例如: <input type="submit" formtarget="_blank" value="提交到一个新的页面上">
        '''
        self._height:str = ""
        '''
        描述: 规定 <input>元素的高度。(只针对type="image")\n
            *pixels: 以像素计的高度（比如 height="100"）\n
        例如: <input type="image" src="img_submit.gif" alt="Submit" width="48" height="48">
        '''
        self._list:str = ""
        '''
        描述: 属性引用 <datalist> 元素，其中包含 <input> 元素的预定义选项。\n
            *datalist_id: 规定绑定到 <input> 元素的 datalist 的 id。
        例如: <input list="browsers">
             <datalist id="browsers">
                <option value="Internet Explorer">
                <option value="Firefox">
                <option value="Google Chrome">
                <option value="Opera">
                <option value="Safari">
             </datalist>
        '''
        self._max:str = ""
        '''
        描述: 属性规定 <input> 元素的最大值。\n
            *number: 数字值。规定输入字段允许的最大值。\n
            *date: 日期。规定输入字段允许的最大值。\n
        例如: <input type="number" name="quantity" min="1" max="5">
        '''
        self._maxlength:str = ""
        '''
        描述: 属性规定 <input> 元素中允许的最大字符数。
            *number: 在 <input> 元素中允许的最大字符数。
        例如: Username: <input type="text" name="usrname" maxlength="10"><br>
        '''
        self._min:str = ""
        '''
        描述: 属性规定 <input> 元素的最小值。\n
            *number: 数字值。规定输入字段允许的最小值。\n
            *date: 日期。规定输入字段允许的最小值。\n
        例如: <input type="number" name="quantity" min="1" max="5">
        '''
        self._multiple:str = ""
        '''
        描述: 属性规定允许用户输入到 <input> 元素的多个值。\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: 选择图片: <input type="file" name="img" multiple="true">
        '''
        self._name:str = ""
        '''
        描述: name 属性规定 <input> 元素的名称。\n
            *text: 规定 <input> 元素的名称。\n
        例如: Name: <input type="text" name="fullname"><br>
        '''
        self._pattern:str = ""
        '''
        描述: pattern 属性规定用于验证 <input> 元素的值的正则表达式。\n
            *regexp: 规定用于验证 <input> 元素的值的正则表达式。\n
        例如: Country code: <input type="text" name="country_code" pattern="[A-Za-z]{3}" title="Three letter country code">
        '''
        self._placeholder:str = ""
        '''
        描述: placeholder 属性规定可描述输入 <input> 字段预期值的简短的提示信息 。\n
            *text: 规定可描述输入字段预期值的简短的提示信息。\n
        例如: <input type="text" name="fname" placeholder="First name"><br>
        '''
        self._readonly:str = ""
        '''
        描述: readonly 属性规定输入字段是只读的。\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: Country: <input type="text" name="country" value="Norway" readonly="true"><br>
        '''
        self._required:str = ""
        '''
        描述: 属性规定必需在提交表单之前填写输入字段。\n
            *不为空: 开启。\n
            *为空则关闭 \n
        例如: Username: <input type="text" name="usrname" required="true">
        '''
        self._size:str = ""
        '''
        描述: size 属性规定以字符数计的 <input> 元素的可见宽度。\n
            *number:规定以字符数计的 <input> 元素的宽度。默认值是 20。\n
        例如: PIN: <input type="text" name="pin" maxlength="4" size="4"><br>
        '''
        self._src:str = ""
        '''
        描述: src 属性规定显示为提交按钮的图像的 URL。 (只针对 type="image")\n
            *URL: 规定作为提交按钮来使用的图像的 URL。\n
                *绝对 URL - 某个页面的完整地址（比如 href="http://www.example.com/formresult.html")\n
                *相对 URL - 指向当前站点内的一个文件（比如 href="formresult.html")\n
        例如: <input type="image" src="submit.gif" alt="Submit">
        '''
        self._step:str = ""
        '''
        描述: step 属性规定 <input> 元素的合法数字间隔。\n
            *number: 规定输入字段的合法数字间隔。\n
        例如: <input type="number" name="points" step="3">
        '''
        self._type:str = ""
        '''
        描述: type 属性规定要显示的 <input> 元素的类型。\n
            *button: 定义可点击的按钮（通常与 JavaScript 一起使用来启动脚本）。\n
            *checkbox: 定义复选框。\n
            *color: 定义拾色器。\n
            *date: 定义 date 控件（包括年、月、日，不包括时间）。\n
            *datetime: 定义 date 和 time 控件（包括年、月、日、时、分、秒、几分之一秒，基于 UTC 时区）。\n
            *datetime-local: 定义 date 和 time 控件（包括年、月、日、时、分、秒、几分之一秒，不带时区）。\n
            *email: 定义用于 e-mail 地址的字段。\n
            *file: 定义文件选择字段和 "浏览..." 按钮，供文件上传。\n
            *hidden: 定义隐藏输入字段。\n
            *image: 定义图像作为提交按钮。\n
            *month: 定义 month 和 year 控件（不带时区）。\n
            *number: 定义用于输入数字的字段。\n
            *password: 定义密码字段（字段中的字符会被遮蔽）。\n
            *radio: 定义单选按钮。\n
            *range: 定义用于精确值不重要的输入数字的控件（比如 slider 控件）。\n
            *reset: 定义重置按钮（重置所有的表单值为默认值）。\n
            *search: 定义用于输入搜索字符串的文本字段。\n
            *submit: 定义提交按钮。\n
            *tel: 定义用于输入电话号码的字段。\n
            *text: 默认。定义一个单行的文本字段（默认宽度为 20 个字符）。\n
            *time: 定义用于输入时间的控件（不带时区）。\n
            *url: 定义用于输入 URL 的字段。\n
            *week: 定义 week 和 year 控件（不带时区）。\n
        例如: <input type="submit" value="提交">
        '''
        self._value:str = ""
        '''
        描述: 指定 <input> 元素 value 的值。\n
            *text: 规定 <input> 元素的值。\n
        例如: Last name: <input type="text" name="lname" value="Doe"><br>
        '''
        self._width:str = ""
        '''
        描述: 规定 <input>元素的宽度。(只针对type="image")\n
            *pixels: 以像素计的宽度（比如 height="100"）\n
        例如: <input type="image" src="img_submit.gif" alt="Submit" width="48" height="48">
        '''

    def __str__(self) -> str:
        _str = super().__str__()
        _tagName = type(self).__name__.lower()
        return _str.replace(f"</{_tagName}>", "")


if __name__ == "__main__":
    _form = Form()
    _form._action = "www.baidu.com"
    _form._method = "get"

    _input = Input()
    _input._type = "submit"
    _input._value = "提交"
    _input._disabled = "true"
    
    _form._tags.append(_input)
    print(_form)

