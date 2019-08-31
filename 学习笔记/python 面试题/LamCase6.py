# lambda表达式
# 可以用lambda关键字创建一个小的匿名函数，可使用lambda表达式来返回一个函数，另一个用法是传递一个小函数作为参数

pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)