# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Base.py
@Time    :   2022/11/06 07:24:35
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

import sys
sys.path.append( "" if hasattr(sys, "_MEIPASS") else __file__[0:__file__.index("Src")] )

from typing import Dict, List
from Src.Css.Base import *


class Dom:
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
        self._style:List[Style] = []
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
        self._translate:str = ""
        '''
        描述: 指定是否一个元素的值在页面载入时是否需要翻译 \n
            *yes: 规定元素内容需要翻译 \n
            *no: 规定元素内容不需要翻译 \n  
        例如: <p translate="no">这个段落不能翻译。</p>
        '''
        
        self._spellcheck:str = ""
        '''
        描述: 检测元素是否拼写错误 \n
            *true: 规定应当对元素的文本进行拼写检查。\n
            *false: 规定不应对元素的文本进行拼写检查。\n
        例如: <p contenteditable="true" spellcheck="true">这是可编辑的段落。请试着编辑文本。</p>
        '''
        self._hidden:str = ""
        '''
        描述: 规定对元素进行隐藏。 \n
        例如: <p hidden="hidden">这是一段隐藏的段落。</p>
        '''
        self._dropzone:str = ""
        '''
        描述: 指定是否将数据复制，移动，或链接，或删除 \n
            *copy: 拖动数据会导致被拖数据产生副本。\n
            *move: 拖动数据会导致被拖数据移动到新位置。\n
            *link: 拖动数据会生成指向原始数据的链接。\n
        例如: <div dropzone="copy"></div>
        '''
        self._draggable:str = ""
        '''
        描述: 指定某个元素是否可以拖动 \n
            *true: 规定元素是可拖动的。\n
            *false: 规定元素是不可拖动的。\n
            *auto: 使用浏览器的默认特性\n
        例如: <p draggable="true">这是一段可移动的段落。请把该段落拖入上面的矩形。</p>
        '''
        self._contextmenu:str = ""
        '''
        描述: 指定一个元素的上下文菜单。当用户右击该元素，出现上下文菜单 \n
            *menu_id: 要打开的 <menu> 元素的 id。\n
        例如: <div contextmenu="mymenu">
                <menu type="context" id="mymenu">
                <menuitem label="Refresh"></menuitem>
                <menuitem label="Twitter"></menuitem>
                </menu>
            </div>
        '''
        self._contenteditable:str = ""
        '''
        描述: 规定是否可编辑元素的内容。\n
            *true: 指定元素是可编辑的\n
            *false: 指定元素是不可编辑的\n
        例如: <p contenteditable="true">这是一个可编辑段落。</p>
        '''

        # 非html属性
        self._text:str = ""
        '''
        描述: 标签的文本内容 \n
        例如: <p id="d1">dfadsfasfsdf</p>
        '''
        self._tags:List[Dom] = []
        '''
        描述: 标签列表 \n
        例如: <div accesskey="c" class="test" id="123"><div id="d1">dfadsfasfsdf</div></div>
        '''
        

    def __str__(self) -> str:
        _tagName = type(self).__name__.lower()
        _specialKeys = ["_text", "_tags", "_style"]
        _attrDct = {_key.replace("_", ""): _value for _key, _value in self.__dict__.items() if _key not in _specialKeys}
        _content = self._text if self._text else "" + ''.join(str(_tag) for _tag in self._tags)
        _attr = " ".join([f'''{_key}="{_value}"''' for _key, _value in _attrDct.items() if len(_value) > 0])
        _attr = " " + _attr if len(_attr) > 0 else "" 
        _style = "".join(str(_s) for _s in self._style)
        _style = f''' style="{_style}" ''' if len(_style) > 0 else ""
        return f"<{_tagName}{_attr}{_style}>{_content}</{_tagName}>"