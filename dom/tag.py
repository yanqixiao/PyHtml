#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dom.py
@Time    :   2022/11/04 14:22:44
@Author  :   Yqx 
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib


from typing import Dict, List


class Tag:

    def __init__(self) -> None:
        self._accesskey = ""
        '''
        描述: 设置访问元素的键盘快捷键 \n
            *IE浏览器 \n
                按住Alt键, 点击accesskey定义的快捷键(焦点将移动到链接)，再按回车.\n
            *FireFox浏览器\n
                按住Alt+Shift键, 点击accesskey定义的快捷键.\n
            *Chrome浏览器\n
                按住Alt键, 点击accesskey定义的快捷键.\n
            *Opera浏览器\n
                按住Shift键, 点击esc, 出现本页定义的accesskey快捷键列表可供选择.\n
            *Safari浏览器\n
                按住Alt键, 点击accesskey定义的快捷键.\n
        例如: <a href="//www.runoob.com/html/html-tutorial.html" accesskey="h">HTML 教程</a>
        '''
        self._class:str = ""
        '''
        描述: 规定元素的类名 (classname) \n
        例如: <p class="important">注意：这是一个很重要的段落。 :)</p>    
        '''
        self._dir:str = ""
        '''
        描述: 设置元素中内容的文本方向。\n
            *ltr: 默认。从左向右的文本方向。\n
            *rtl: 从右向左的文本方向。\n
            *auto: 让浏览器根据内容来判断文本方向。仅在文本方向未知时推荐使用。 \n
        例如: <bdo dir="rtl">文本方向从右到左!</bdo>
        '''
        self._lang:str = ""
        '''
        描述: 设置元素中内容的语言代码。 \n
            *language_code: 规定元素内容的语言代码。语言代码参考手册。 语言代码参考手册 \n
        例如: <p lang="fr">这是一个段落。</p>
        '''
        self._id:str = ""
        '''
        描述: 规定元素的唯一 id \n
            *id: 规定元素的唯一 id \n
            命名规则：\n
                *必须以字母 A-Z 或 a-z 开头 \n
                *其后的字符：字母(A-Za-z)、数字(0-9)、连字符("-")、下划线("_")、冒号(":") 以及点号(".") \n
                *值对大小写敏感 \n
        例如: <h1 id="myHeader">Hello World!</h1>
        '''
        self._style:str = ""
        '''
        描述: 规定元素的行内样式(inline style) \n
        例如: <h1 style="color:blue;text-align:center">这是一个标题</h1>
        '''
        self._tabindex:str = ""
        '''
        描述: 设置元素的 Tab 键控制次序。\n
            *number: 规定元素的 tab 键控制顺序(1 是第一）\n
        例如: <a href="//www.microsoft.com/" tabindex="3">Microsoft</a>
        '''
        self._title:str = ""
        '''
        描述: 规定元素的额外信息（可在工具提示中显示）\n
            *text: 规定元素的工具提示文本(tooltip text) \n
        例如: <p><abbr title="世界卫生组织">WHO</abbr> 成立于 1948。</p>
        '''
        self._text:str = ""
        '''
        描述: 标签的文本内容 \n
        例如: <p id="d1">dfadsfasfsdf</p>
        '''
        self._tags:List[Tag] = []
        '''
        描述: 标签列表 \n
        例如: <div accesskey="c" class="test" id="123"><div id="d1">dfadsfasfsdf</div></div>
        '''

    def __str__(self) -> str:
        _tag = type(self).__name__.lower()
        _arg = {_key.replace("_", ""): _value for _key, _value in self.__dict__.items() if _key != "_text" and _key != "_tags"}
        _sub = self._text if self._text else ""
        _sub += ''.join(str(_tag) for _tag in self._tags)
        _ret = " ".join([f'''{_key}="{_value}"''' for _key, _value in _arg.items() if len(_value) > 0])
        return f"<{_tag} {_ret}>{_sub}</{_tag}>"

    @property
    def id(self):\
        return self._id

    @id.setter
    def id(self, value):
        self._id = value