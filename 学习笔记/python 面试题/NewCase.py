class A(object):
    """
    cls和类ID一样，说明指向同一个类，也就是cls就是创建的实例类
    init方法中的self和new方法返回值地址一样，说明返回值是对象
    这是cls的ID 2753743352488
    这是new方法 <__main__.A object at 0x000002811F749828>
    这是init方法 <__main__.A object at 0x000002811F749828>
    这是类A的ID 2753743352488
    """
    def __init__(self):
        print("2这是init方法",self)

    def __new__(cls):
        print("1这是cls的ID",id(cls))
        print("2这是new方法",object.__new__(cls))
        return object.__new__(cls)


A()
print("1这是类A的ID",id(A))