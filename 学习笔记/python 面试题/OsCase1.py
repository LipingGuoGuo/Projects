# 标准库简介
# 操作系统接口
# os模块提供了许多与操作系统交互的函数
# 一定要使用import os 而不是from os import *,避免内建的open()函数被os.open()隐式替换掉，使用方式大不相同
import os
# 返回当前的工作目录
os.getcwd()
# 改变当前工作目录
# os.chdir('/NewCase.py')


# 内置的dir()和help()函数可用作交互式辅助工具，用于处理大型模块，如os
# 返回所有模块函数的列表
print(dir(os))

# 返回从模块的文档字符串创建的扩展手册页
print(help(os))

# 文件通配符
# glob模块提供了一个在目录中使用通配符搜索创建文件列表的函数
import glob
list = glob.glob('*.py')
print(list)