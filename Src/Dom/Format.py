# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Format.py
@Time    :   2022/11/07 05:31:52
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


class Abbr(Dom):
    '''
    描述: 定义一个缩写 \n
    例如: The<abbr title="World Health Organization">WHO</abbr> was founded in 1948.
    '''
    def __init__(self) -> None:
        super().__init__()


class Address(Dom):
    '''
    描述: 定义文档作者或拥有者的联系信息。\n
    例如: 
        <address>
            Written by <a href="mailto:webmaster@example.com">Jon Doe</a>.<br> 
            Visit us at:<br>
            Example.com<br>
            Box 564, Disneyland<br>
            USA
        </address>
    '''
    def __init__(self) -> None:
        super().__init__()


class B(Dom):
    '''
    描述: 定义粗体文本。\n
    例如: <p>这是一个普通的文本- <b>这是一个加粗文本</b>。</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Bdo(Dom):
    '''
    描述: 定义文本的方向。\n
    例如: <p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._dir:str = ""
        '''
        描述: 规定 <bdo> 元素内的文本方向。
            *ltr: 从左至右(默认)
            *rtl: 从右至左
        例如: <p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>
        '''


class Big(Dom):
    '''
    描述: 定义大号文本。\n
    例如: <p><big>这个文本比较大。</big></p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Blockquote(Dom):
    '''
    描述: 定义块引用。\n
    例如: <blockquote cite="http://www.worldwildlife.org/who/index.html">
            For 50 years, WWF has been protecting the future of nature. ...
        </blockquote>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._cite:str = ""
        '''
        描述: 规定引用的来源。\n
            ^URL: 引用的来源的 URL。\n
                ^绝对 URL - 指向另一个站点(比如 href="http://www.example.com/song.ogg")\n
                *相对 URL - 指向网站内的文件(比如 href="song.ogg")\n
        例如: <blockquote cite="http://www.worldwildlife.org/who/index.html"><p>这是一个长引用，这是一个长引用。</p></blockquote>
        '''


class City(Dom):
    '''
    描述: 定义引用(citation)。\n
    例如: <p><cite>The Scream</cite> by Edward Munch. Painted in 1893.</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Code(Dom):
    '''
    描述: 定义计算机代码文本。\n
    例如: <code>一段电脑代码 print("Hello World")</code>
    '''
    def __init__(self) -> None:
        super().__init__()


class Del(Dom):
    '''
    描述: 定义被删除文本。\n
    例如: <p>My favorite color is <del>blue</del> <ins>red</ins>!</p>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._cite:str = ""
        '''
        描述: 规定引用的来源。\n
            ^URL: 引用的来源的 URL。\n
                ^绝对 URL - 指向另一个站点(比如 href="http://www.example.com/song.ogg")\n
                *相对 URL - 指向网站内的文件(比如 href="song.ogg")\n
                *锚 URL - 指向页面内的一个锚(比如 href="#page")\n
        例如: <p><del cite="del_demo_cite.htm">这是一个被删除了的文本</del></p>
        '''
        self._datetime:str = ""
        '''
        描述: 规定文本被删除的日期和时间。\n
            *YYYY-MM-DDThh:mm:ssTZD: 文本被删除的日期和时间()\n
                *YYYY - 年(例如 2009)\n
                *MM - 月(例如 01 for January)\n
                *DD - 月中的日 (例如 08)\n
                *T - 必需的分隔符\n
                *hh - 小时 (例如 22 for 10.00pm)\n
                *mm - 分钟 (例如 55)\n
                *ss - 秒 (例如 03)\n
                *TZD - 时区标志符(Z 表示祖鲁，同时也是格林威治时间)\n
        例如: <p><del datetime="2011-11-15T22:55:03Z">这是一个被删除了的文本</del></p>
        '''


class Dfn(Dom):
    '''
    描述: 定义定义项目。\n
    例如: <dfn>定义项目</dfn>
    '''
    def __init__(self) -> None:
        super().__init__()


class Em(Dom):
    '''
    描述: 定义强调文本。\n
    例如: <em>强调文本</em>
    '''
    def __init__(self) -> None:
        super().__init__()


class I(Dom):
    '''
    描述: 定义斜体文本。\n
    例如: <p>He named his car <i>The lightning</i>, because it was very fast.</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Ins(Del):
    '''
    描述: 定义被插入文本。\n
    例如: <p>My favorite color is <del>blue</del> <ins>red</ins>!</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Kbd(Dom):
    '''
    描述: 定义键盘文本。\n
    例如: <kbd>键盘输入</kbd>
    '''
    def __init__(self) -> None:
        super().__init__()


class Pre(Dom):
    '''
    描述: 定义预格式文本\n
    例如: <pre>Do not forget to buy <mark>milk</mark> today.</pre>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._width:str = ""
        '''
        描述: 定义每行的最大字符数(通常是 40、80 或 132)。\n
        例如: <pre width="30">Do not forget to buy <mark>milk</mark> today.</pre>
        '''


class Q(Blockquote):
    '''
    描述: 定义短的引用。\n
    例如: <q>Build a future where people live in harmony with nature.</q>
    '''
    def __init__(self) -> None:
        super().__init__()


class S(Dom):
    '''
    描述: 定义加删除线的文本。\n
    例如: <p><s>My car is blue.</s></p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Samp(Dom):
    '''
    描述: 定义计算机代码样本。\n
    例如: <samp>计算机样本</samp>
    '''
    def __init__(self) -> None:
        super().__init__()


class Small(Dom):
    '''
    描述: 定义小号文本。\n
    例如: <small>计算机样本</small>
    '''
    def __init__(self) -> None:
        super().__init__()
        

class Strike(Dom):
    '''
    描述: 定义加删除线的文本。\n
    例如: <p>Version 2.0 is <strike>not yet available!</strike> now available!</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Strong(Dom):
    '''
    描述: 定义语气更为强烈的强调文本。\n
    例如: <strong>计算机样本</strong>
    '''
    def __init__(self) -> None:
        super().__init__()


class Sub(Dom):
    '''
    描述: 定义下标文本。\n
    例如: <p>这个文本包含 <sub>下标</sub>文本。</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Sup(Dom):
    '''
    描述: 定义上标文本。\n
    例如: <p>这个文本包含 <sup>上标</sup>文本。</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class U(Dom):
    '''
    描述: 定义下划线文本。\n
    例如: <p>This is a <u>parragraph</u>.</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Var(Dom):
    '''
    描述: 定义文本的变量部分。\n
    例如: <var>变量</var>
    '''
    def __init__(self) -> None:
        super().__init__()

'''Html5 新增标签'''
class Bdi(Dom):
    '''
    描述: 允许您设置一段文本，使其脱离其父元素的文本方向设置。\n
    例如: <ul>
            <li>用户 <bdi>hrefs</bdi>: 60 分</li>
            <li>用户 <bdi>jdoe</bdi>: 80 分</li>
            <li>用户 <bdi>إيان</bdi>: 90 分</li>
         </ul>
    '''
    def __init__(self) -> None:
        super().__init__()


class Mark(Dom):
    '''
    描述: 定义带有记号的文本。\n
    例如: <p>Do not forget to buy <mark>milk</mark> today.</p>
    '''
    def __init__(self) -> None:
        super().__init__()


class Meter(Dom):
    '''
    描述: 定义度量衡。仅用于已知最大和最小值的度量。\n
    例如: <meter value="2" min="0" max="10">2 out of 10</meter><br>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._form:str = ""
        '''
        描述: 规定 <meter> 元素所属的一个或多个表单。\n
        例如: <meter form="form1" name="x1" min="0" low="40" high="90" max="100" value="95"></meter>
        '''
        self._high:str = ""
        '''
        描述: 规定被界定为高的值的范围。\n
            *number: 规定一个被界定为高的值的浮点数。\n
        例如: <meter min="0" low="40" high="90" max="100" value="95"></meter>
        '''
        self._low:str = ""
        '''
        描述: 规定被界定为低的值的范围。\n
            *number: 规定一个被界定为低的值的浮点数。\n
        例如: <meter min="0" low="40" high="90" max="100" value="95"></meter>
        '''
        self._max:str = ""
        '''
        描述: 规定范围的最大值。\n
            *number: 规定一个表示度量的最大值的浮点数。默认值是 "1"。\n
        例如: <meter min="0" low="40" high="90" max="100" value="95"></meter>
        '''
        self._min:str = ""
        '''
        描述: 规定范围的最小值。\n
            *number: 规定一个表示度量的最小值的浮点数。默认值是 "0"。\n
        例如: <meter min="0" low="40" high="90" max="100" value="95"></meter>
        '''
        self._optimum:str = ""
        '''
        描述: 规定度量的最优值。\n
            *number: 规定一个表示度量的最优值的浮点数。\n
        例如: <meter value="0.3" high="0.9" low="0.1" optimum="0.5"></meter>
        '''
        self._value:str = ""
        '''
        描述: 必需。规定度量的当前值。\n
            *number: 必需。规定一个表示度量的当前值的浮点数。\n
        例如: <meter min="0" low="40" high="90" max="100" value="95"></meter>
        '''


class Progress(Dom):
    '''
    描述: 定义运行中的任务进度（进程)。\n
    例如: <progress value="22" max="100"></progress>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._max:str = ""
        '''
        描述: 规定需要完成的值。\n
            *number: 一个规定任务总共需要多少工作的浮点数。\n
        例如: <progress value="22" max="100"></progress>
        '''
        self._value:str = ""
        '''
        描述: 规定进程的当前值。\n
            *number: 一个规定已经完成多少任务的浮点数。\n
        例如: <progress value="22" max="100"></progress>
        '''


class Rp(Dom):
    '''
    描述: 定义不支持 ruby 元素的浏览器所显示的内容。\n
    例如: <ruby>
            漢 <rp>(</rp><rt>han</rt><rp>)</rp>
            字 <rp>(</rp><rt>zi</rt><rp>)</rp>
        </ruby>
    '''
    def __init__(self) -> None:
        super().__init__()


class Rt(Dom):
    '''
    描述: 定义字符（中文注音或字符）的解释或发音。\n
    例如: <ruby>
            漢 <rp>(</rp><rt>han</rt><rp>)</rp>
            字 <rp>(</rp><rt>zi</rt><rp>)</rp>
        </ruby>
    '''
    def __init__(self) -> None:
        super().__init__()


class Ruby(Dom):
    '''
    描述: 定义 ruby 注释（中文注音或字符）。\n
    例如: <ruby>
            漢 <rp>(</rp><rt>han</rt><rp>)</rp>
            字 <rp>(</rp><rt>zi</rt><rp>)</rp>
        </ruby>
    '''
    def __init__(self) -> None:
        super().__init__()


class Time(Dom):
    '''
    描述: 定义一个日期/时间。\n
    例如: <p>我在 <time datetime="2016-02-14">情人节</time> 有个约会。</p>
    '''
    def __init__(self) -> None:
        super().__init__()
        self._datetime:str = ""
        '''
        描述: 规定日期/时间。另一种方式，则是由元素的内容给定日期/时间。\n
            *YYYY-MM-DDThh:mm:ssTZD: 文本被删除的日期和时间()\n
                *YYYY - 年(例如 2009)\n
                *MM - 月(例如 01 for January)\n
                *DD - 月中的日 (例如 08)\n
                *T - 必需的分隔符\n
                *hh - 小时 (例如 22 for 10.00pm)\n
                *mm - 分钟 (例如 55)\n
                *ss - 秒 (例如 03)\n
                *TZD - 时区标志符(Z 表示祖鲁，同时也是格林威治时间)\n
        例如: <p>我在<time datetime="2008-02-14">情人节</time>有个约会。</p>
        '''
        self._pubdate:str = ""
        '''
        描述: 指示 <time> 元素中的日期 / 时间是文档（或最近的前辈 <article> 元素）的发布日期
        例如: ----
        '''


class Wbr(Dom):
    '''
    描述: 规定在文本中的何处适合添加换行符。\n
    例如: <p>学习 AJAX ,您必须熟悉 <wbr>Http<wbr>Request 对象。</p>
    '''
    def __init__(self) -> None:
        super().__init__()