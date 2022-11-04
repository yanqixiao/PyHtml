# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   event.py
@Time    :   2022/11/04 21:35:39
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

class Event:
    def __str__(self) -> str:
        _arg = {_key.replace("_", ""): _value for _key, _value in self.__dict__.items()}
        _ret = " ".join([f'''{_key}="{_value}"''' for _key, _value in _arg.items() if len(_value) > 0])
        return _ret


class WindowEvent(Event):
    '''
    描述: 由窗口触发该事件 (适用于 <body> 标签)
    '''
    def __init__(self) -> None:
        self._onafterprint:str = ""
        '''
        描述: 在打印文档之后运行脚本 \n
        例如: <body onafterprint="printmsg()">
        '''
        self._onbeforeprint:str = ""
        '''
        描述: 在文档打印之前运行脚本 \n
        例如: <body onbeforeprint="printmsg()">
        '''
        self._onbeforeonloadNew:str = ""
        '''
        描述: 在文档加载之前运行脚本
        例如: <body onbeforeonloadNew="printmsg()">
        '''
        self._onblur:str = ""
        '''
        描述: 当窗口失去焦点时运行脚本
        例如: <body onblur="printmsg()">
        '''
        self._onerror:str = ""
        '''
        描述: 当错误发生时运行脚本
        例如: <body onerrorNew="printmsg()">
        '''
        self._onfocus:str = ""
        '''
        描述: 当窗口获得焦点时运行脚本 \n
        例如: <body onfocus="printmsg()">
        '''
        self._onhashchangeNew:str = ""
        '''
        描述: 当文档改变时运行脚本 \n
        例如: <body onhashchangeNew="printmsg()">
        '''
        self._onfocus:str = ""
        '''
        描述: 当窗口获得焦点时运行脚本 \n
        例如: <body onfocus="printmsg()">
        '''
        self._onload:str = ""
        '''
        描述: 当文档加载时运行脚本 \n
        例如: <body onload="printmsg()">
        '''
        self._onmessageNew:str = ""
        '''
        描述: 当触发消息时运行脚本 \n
        例如: <body onmessageNew="printmsg()">
        '''
        self._onofflineNew:str = ""
        '''
        描述: 当文档离线时运行脚本 \n
        例如: <body onofflineNew="printmsg()">
        '''
        self._ononlineNew:str = ""
        '''
        描述: 当文档上线时运行脚本 \n
        例如: <body ononlineNew="printmsg()">
        '''
        self._onpagehideNew:str = ""
        '''
        描述: 当窗口隐藏时运行脚本 \n
        例如: <body onpagehideNew="printmsg()">
        '''
        self._onpageshowNew:str = ""
        '''
        描述: 当窗口可见时运行脚本 \n
        例如: <body onpageshowNew="printmsg()">
        '''
        self._onpopstateNew:str = ""
        '''
        描述: 当窗口历史记录改变时运行脚本 \n
        例如: <body onpopstateNew="printmsg()">
        '''
        self._onredoNew:str = ""
        '''
        描述: 当文档执行再执行操作（redo）时运行脚本 \n
        例如: <body onredoNew="printmsg()">
        '''
        self._onresize:str = ""
        '''
        描述: 当调整窗口大小时运行脚本 \n
        例如: <body onresize="printmsg()">
        '''
        self._onstorageNew:str = ""
        '''
        描述: 当 Web Storage 区域更新时（存储空间中的数据发生变化时）运行脚本 \n
        例如: <body onstorageNew="printmsg()">
        '''
        self._onundoNew:str = ""
        '''
        描述: 当文档执行撤销时运行脚本 \n
        例如: <body onundoNew="printmsg()">
        '''
        self._onunload:str = ""
        '''
        描述: 当用户离开文档时运行脚本 \n
        例如: <body onunload="printmsg()">
        '''


class FormEent(Event):
    '''
    描述: 表单事件在HTML表单中触发 (适用于所有 HTML 元素, 但该HTML元素需在form表单内)
    '''
    def __init__(self) -> None:
        super().__init__()
        self._onblur:str = ""
        '''
        描述: 当窗口失去焦点时运行脚本
        例如: <input type="text" name="fname" id="fname" onblur="upperCase()">
        '''
        self._onchange:str = ""
        '''
        描述: 当元素改变时运行脚本
        例如: <input type="text" name="txt" value="Hello" onchange="checkField(this.value)">>
        '''


if __name__ == "__main__":
    we = WindowEvent()
    we._onload = "printmsg()"
    print(we)