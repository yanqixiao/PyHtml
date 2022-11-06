# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2022/11/05 10:13:04
@Author  :   Yqx
@Version :   1.0
@Contact :   yanqixiao@163.com
@License :   (C)Copyright 2020-2120, OLE Technology Co., Ltd
@Desc    :   None
'''

# here put the import lib

import os, sys
from PyInstaller.__main__ import run

'''
-F, --onefile 打包一个单个文件,如果你的代码都写在了一个py文件的话,可以使用这个命令,如果是多个py文件,就别用；
-D, --onedir 打包多个文件,在dist中生成很多依赖文件,适合以框架的形式编写工具代码,代码易于维护；
-a, --ascii 不包含unicode编码的支持(包括默认值:如果可用)
-c, --console 使用控制台子系统执行(默认),只对windows有效
-w, --windowed, --noconsole 使用windows子系统执行,当程序启动的时候不会打开命令行(只对windows有效)
-i , --icon=<File.ico>将file.ico添加为打包的exe文件的图表,只对windows系统有效
--icon=<File.exe,n>将file.exe的第n个图标添加为可执行文件的资源,只对windows系统有效
-n Name,--name=Name 可选的项目,生成的.spec文件的名字和exe名字
-p 设置导入路径(和使用PYTHONPATH效果相似),可以使用路径分隔符(windows使用分好,linux使用冒号),制定多个目录的时候可以指定多个-p参数来设置,让pyinstaller自己去找程序的资源
--key KEY 用于加密Python字节码的密钥
--add-data 可以将一些非二进制文件添加到exe文件中进行打包,参数为格式为static;static
--distpath 指定打包后的程序存放目录,exe文件默认存放在当前目录下的dist目录中
--workpath 为输出的所有临时文件指定存放目录,默认为当前目录下的build目录
'''

if __name__ == "__main__":
    _dir = os.path.dirname(sys.argv[0])
    _root = os.path.join(_dir, "bin")
    _distpath = f"--distpath={_root}"
    _specpath = f"--specpath={_root}"
    _workpath = f"--workpath={os.path.join(_dir, 'Build')}"
    _target = os.path.join(_dir, "test/test.py")
    _name = "--name=pyhtmltest"
    run([_target, _name, '-F', "--noupx", _distpath, _workpath, _specpath])