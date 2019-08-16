# copy和deepcopy深浅复制
import copy

list = [1,2,[3,4]]
a = copy.copy(list)
b = copy.deepcopy(list)
print(list,id(list))
print(a,id(a))
print(b,id(b))

# 测试修改外层列表的简单子对象
# 结果修改原始list之后，a和b并没有改变，因为是三个不同的对象
list[0] = 10
print(list,id(list))
print(a,id(a))
print(b,id(b))

# 测试内层列表的值的修改，也就是测试复杂子对象的值的修改
# 结果表明copy浅拷贝并没有真正将内层列表（字典）独立拷贝出来，导致修改了list内层列表（字典）后的内层列表（字典）值也变化
# 结果表明deepcopy深拷贝可以将内层列表和字典独立拷贝出来，所以b的内层列表（字典）值不变
list[2][0] = 5
print(list,id(list))
print(a,id(a))
print(b,id(b))