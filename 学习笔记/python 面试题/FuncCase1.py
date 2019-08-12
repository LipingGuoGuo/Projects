# 题目5：fun(*args,**kwargs)中的*args,**kwargs什么意思
def demo(args_f,*args_v):
    """
    *args和**kwargs主要用于函数定义
    可以将不定数量的参数传递给一个函数
    这里不定的意思是：预先并不知道，函数使用者会传递多少参数，在这个场景下使用这两个关键字
    *args 是用来发送一个非键值对的可变数量的参数列表给一个函数
    :param args_f:
    :param args_v:
    :return:
    """
    print(args_f)
    for x in args_v:
        print(x)

demo('a','b','c','d')




