import time


class Animal(object):
    # 创建完对象后会自动被调用
    def __init__(self,name):
        print("__init__方法被调用")
        self.__name = name

    # 当对象被删除时，会自动被调用
    def __del__(self):
        """
        del方法只有在对象真正被删除时才调用打印（cat3被删除时）
        """
        print("__del__方法被调用")
        print("%s对象马上被干掉了..." % self.__name)


cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print(id(cat),id(cat2),id(cat3))
print("---马上删除cat对象")
del cat
print("---马上删除cat2对象")
del cat2
print("---马上删除cat3对象")
del cat3
print("程序2秒钟后结束")
time.sleep(2)

