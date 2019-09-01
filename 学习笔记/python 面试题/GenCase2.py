# 生成器
# Generator是一个用于创建迭代器的简单而强大的工具
# 写法类似于标准函数，但当他们要返回数据时会使用yield语句
# 每次对生成器调用next（）时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）
# 可以用生成器来完成的操作同样可以用案例Iter.doc描述的基于类的迭代器来完成，但生成器的写法更为紧凑，，因为会自动创建__iter__()和__next__()方法
# 另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存
# 生成器终结时，会自动引发Stop Iteration

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]


if __name__ == "__main__":
    for char in reverse("golf"):
        print(char)

