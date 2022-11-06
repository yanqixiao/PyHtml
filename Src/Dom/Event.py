# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   event.py
@Time    :   2022/11/06 07:28:55
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
        描述: 当文档执行再执行操作(redo)时运行脚本 \n
        例如: <body onredoNew="printmsg()">
        '''
        self._onresize:str = ""
        '''
        描述: 当调整窗口大小时运行脚本 \n
        例如: <body onresize="printmsg()">
        '''
        self._onstorageNew:str = ""
        '''
        描述: 当 Web Storage 区域更新时(存储空间中的数据发生变化时)运行脚本 \n
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
        描述: 当窗口失去焦点时运行脚本 \n
        例如: <input type="text" name="fname" id="fname" onblur="upperCase()">
        '''
        self._onchange:str = ""
        '''
        描述: 当元素改变时运行脚本 \n
        例如: <input type="text" name="txt" value="Hello" onchange="checkField(this.value)">>
        '''
        self._onfocus:str = ""
        '''
        描述: 当元素获得焦点时运行脚本 \n
        例如: <input type="text" id="fname" onfocus="setStyle(this.id)">
        '''
        self.onreset:str = ""
        '''
        描述: 当表单重置时运行脚本。 \n
        例如: <input type="text" id="fname" onreset="setStyle(this.id)">
        '''
        self.onselect:str = ""
        '''
        描述: 当选取元素时运行脚本 \n
        例如: <input type="text" onselect="showMsg() value="Hello world!">
        '''
        self.onsubmit:str = ""
        '''
        描述: 当提交表单时运行脚本 \n
        例如: <form action="demo_form.html" onsubmit="checkForm()">
        '''
        self.oncontextmenu:str = ""
        '''
        描述: 当触发上下文菜单时运行脚本 \n
        例如: <input type="text" id="fname" oncontextmenu="setStyle(this.id)">
        '''
        self.onformchange:str = ""
        '''
        描述: 当表单改变时运行脚本 \n
        例如: <input type="text" id="fname" onformchange="setStyle(this.id)">
        '''
        self.onforminput:str = ""
        '''
        描述: 当表单获得用户输入时运行脚本 \n
        例如: <input type="text" id="fname" onforminput="setStyle(this.id)">
        '''
        self.oninput:str = ""
        '''
        描述: 当元素获得用户输入时运行脚本 \n
        例如: <input type="text" id="fname" oninput="setStyle(this.id)">
        '''
        self.oninvalid:str = ""
        '''
        描述: 当元素无效时运行脚本 \n
        例如: <input type="text" id="fname" oninvalid="setStyle(this.id)">
        '''


class KeyboardEvent(Event):
    '''
    描述: 通过鼠标触发事件, 类似用户的行为
    '''
    def __init__(self) -> None:
        super().__init__()
        self._onkeydown:str = ""
        '''
        描述: 当按下按键时运行脚本
        例如: <input type="text" onkeydown="displayResult()">
        '''
        self._onkeypress:str = ""
        '''
        描述: 当按下并松开按键时运行脚本
        例如: <input type="text" onkeypress="displayResult()">
        '''
        self._onkeyup:str = ""
        '''
        描述: 当松开按键时运行脚本
        例如: <input type="text" onkeyup="displayResult()">
        '''


class MouseEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self._onclick:str = ""
        '''
        描述: 当单击鼠标时运行脚本 \n
        例如: <button onclick="copyText()">复制文本</button>
        '''
        self._ondblclick:str = ""
        '''
        描述: 当双击鼠标时运行脚本 \n
        例如: <button ondblclick="copyText()">复制文本</button>
        '''
        self._onmousedown:str = ""
        '''
        描述: 当按下鼠标按钮时运行脚本 \n
        例如: <p onmousedown="mouseDown()">Click the text!</p>
        '''
        self._onmousemove:str = ""
        '''
        描述: 当鼠标指针移动时运行脚本 \n
        例如: <img onmousemove="bigImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._onmouseout:str = ""
        '''
        描述: 当鼠标指针移出元素时运行脚本 \n
        例如: <img onmouseout="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._onmouseover:str = ""
        '''
        描述: 当鼠标指针移至元素之上时运行脚本 \n
        例如: <img onmouseover="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._onmouseup:str = ""
        '''
        描述: 当松开鼠标按钮时运行脚本 \n
        例如: <img onmouseup="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondrag:str = ""
        '''
        描述: 当拖动元素时运行脚本 \n
        例如: <img ondrag="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondragend:str = ""
        '''
        描述: 当拖动操作结束时运行脚本 \n
        例如: <img ondragend="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondragenter:str = ""
        '''
        描述: 当元素被拖动至有效的拖放目标时运行脚本 \n
        例如: <img ondragenter="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondragleave:str = ""
        '''
        描述: 当元素离开有效拖放目标时运行脚本 \n
        例如: <img ondragleave="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondragover:str = ""
        '''
        描述: 当元素被拖动至有效拖放目标上方时运行脚本 \n
        例如: <img ondragover="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondragstart:str = ""
        '''
        描述: 当拖动操作开始时运行脚本 \n
        例如: <img ondragstart="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._ondrop:str = ""
        '''
        描述: 当被拖动元素正在被拖放时运行脚本 \n
        例如: <img ondrop="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._onmousewheel:str = ""
        '''
        描述: 当转动鼠标滚轮时运行脚本 \n
        例如: <img onmousewheel="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''
        self._onscroll:str = ""
        '''
        描述: 当滚动元素的滚动条时运行脚本 \n
        例如: <img onscroll="normalImg(this)" src="smiley.gif" alt="Smiley">
        '''


class MediaEvent(Event):
    '''
    描述: 通过视频(videos)，图像(images)或者音频(audio) 触发该事件，多应用于 HTML 媒体元素比如 <audio>, <embed>, <img>, <object>, 和<video>:
    '''
    def __init__(self) -> None:
        super().__init__()
        self._onabort:str = ""
        '''
        描述: 当发生中止事件时运行脚本 \n
        '''
        self._oncanplay:str = ""
        '''
        描述: 当媒介能够开始播放但可能因缓冲而需要停止时运行脚本 \n
        '''
        self._oncanplaythrough:str = ""
        '''
        描述: 当媒介能够无需因缓冲而停止即可播放至结尾时运行脚本 \n
        '''
        self._ondurationchange:str = ""
        '''
        描述: 当媒介长度改变时运行脚本 \n
        '''
        self._onemptied:str = ""
        '''
        描述: 当媒介资源元素突然为空时(网络错误、加载错误等) 运行脚本 \n
        '''
        self._onended:str = ""
        '''
        描述: 当媒介已抵达结尾时运行脚本 \n
        '''
        self._onerror:str = ""
        '''
        描述: 当在元素加载期间发生错误时运行脚本 \n
        '''
        self._onloadeddata:str = ""
        '''
        描述: 当加载媒介数据时运行脚本 \n
        '''
        self._onloadedmetadata:str = ""
        '''
        描述: 当媒介元素的持续时间以及其他媒介数据已加载时运行脚本 \n
        '''
        self._onloadstart:str = ""
        '''
        描述: 当浏览器开始加载媒介数据时运行脚本 \n
        '''
        self._onpause:str = ""
        '''
        描述: 当媒介数据暂停时运行脚本 \n
        '''
        self._onplay:str = ""
        '''
        描述: 当媒介数据将要开始播放时运行脚本 \n
        '''
        self._onplaying:str = ""
        '''
        描述: 当媒介数据已开始播放时运行脚本 \n
        '''
        self._onprogress:str = ""
        '''
        描述: 当浏览器正在取媒介数据时运行脚本 \n
        '''
        self.onratechange:str = ""
        '''
        描述: 当媒介数据的播放速率改变时运行脚本 \n
        '''
        self.onreadystatechange:str = ""
        '''
        描述: 当就绪状态(ready-state)改变时运行脚本 \n
        '''
        self.onseeked:str = ""
        '''
        描述: 当媒介元素的定位属性 [1] 不再为真且定位已结束时运行脚本 \n
        '''
        self.onseeking:str = ""
        '''
        描述: 当媒介元素的定位属性为真且定位已开始时运行脚本 \n
        '''
        self.onstalled:str = ""
        '''
        描述: 当取回媒介数据过程中(延迟)存在错误时运行脚本 \n
        '''
        self.onsuspend:str = ""
        '''
        描述: 当浏览器已在取媒介数据但在取回整个媒介文件之前停止时运行脚本 \n
        '''
        self.ontimeupdate:str = ""
        '''
        描述: 当媒介改变其播放位置时运行脚本 \n
        '''
        self.onvolumechange:str = ""
        '''
        描述: 当媒介改变音量亦或当音量被设置为静音时运行脚本 \n
        '''
        self.onwaiting:str = ""
        '''
        描述: 当媒介已停止播放但打算继续播放时运行脚本 \n
        '''


class OtherEvent(Event):
    def __init__(self) -> None:
        super().__init__()
        self._onshow:str = ""
        '''
        描述: 当 <menu> 元素在上下文显示时触发
        例如: <menu type="context" id="mymenu" onshow="myFunction()">
                <menuitem label="刷新" onclick="window.location.reload();"></menuitem>
            </menu>
        '''
        self._ontoggle:str = ""
        '''
        描述: 当用户打开或关闭 <details> 元素时触发
        例如: <details ontoggle="myFunction()">
        '''


if __name__ == "__main__":
    we = WindowEvent()
    we._onload = "printmsg()"
    print(we)