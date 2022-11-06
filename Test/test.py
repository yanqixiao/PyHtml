# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/11/05 08:37:39
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

import os, sys
sys.path.append( "" if hasattr(sys, "_MEIPASS") else __file__[0:__file__.index("test")] )

from Src.Dom.Div import *

if __name__ == "__main__":
    
    d = Div()
    d._accesskey = "c"
    d.id = "123"
    d._class = "test"
    d1 = Div()
    d1._id="d1"
    d1._text = "dfadsfasfsdf"
    d._tags = [d1]
    print(d)
    os.system("pause")
