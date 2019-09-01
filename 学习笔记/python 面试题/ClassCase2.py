# 类对象
# 类对象支持两种操作：属性引用和实例化
# 属性引用使用python中所有属性引用所使用的标准语法：obj.name
# 有效的属性名称是类对象被创建时存在与类命名空间中的所有名称


class MyClass:
    """A aimple example class"""
    i = 12345

    def f(self):
        return "hello world"

# MyClass.i和MyClass.f就是有效的属性引用，分别返回一个整数和一个函数对象

# 类的实例化使用函数表达法，可以将类对象视为是返回该类的一个新实例的不带参数的函数
x = MyClass()

# 类永远不会被作为全局作用域

# python有两个内置函数可被用于继承机制
# 使用isinstance（）来检查一个实例的类型：isinstance(obj,int)仅会在obj.__class__为int或某个派生自int的类时为True
# 使用issubclass()来检查类的继承关系：issubclass(bool,int)为True,因为bool是int的子类，但是issubclass（float,int)为False,因为float不是int的子类
