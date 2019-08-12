def demo1(**args_v):
    """
    **kwags允许你将不定长度的键值对，作为参数传递给一个函数
    如果想要在一个函数里处理带名字的参数，应该使用**kwargs？？？
    :param args_v:
    :return:
    """
    for k,v in args_v.items():
        print(k.v)

demo1(name ="'njcx")