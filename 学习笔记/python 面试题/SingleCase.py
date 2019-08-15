# 写一个单列模式
# 实例化一个单例


class SingleTon(object):
    __instance = None

    def __new__(cls,age,name):
        """
        如果类属性__instance的值为None
        那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时，能够知道之前已经创建过对象了，这样就保证了只有一个对象
        :param age:
        :param name:
        :return:
        """
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = SingleTon(18,"dongGe")
b = SingleTon(8,"dongGe")
print(id(a))
print(id(b))

# 给a指向的对象添加一个属性
a.age = 19
# 获取b指向的对象的age属性
print(b.age)
