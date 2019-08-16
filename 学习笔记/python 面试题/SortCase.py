# 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
# 列表排序
list = [0,-1,3,-10,5,9]
list.sort(reverse=False)
print("list.sort()在list基础上修改，无返回值",list)

list = [0,-1,3,-10,5,9]
res = sorted(list,reverse=False)
print("sorted有返回值是新的list",list)
print("返回值",res)