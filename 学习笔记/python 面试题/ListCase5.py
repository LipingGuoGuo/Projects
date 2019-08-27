# 列表嵌套元组，分别按字母和数字排序
foo = [("zs",19),('ll',54),
       ("wa",17),("df",23)]

# 按年龄数字从大到小
a = sorted(foo,key=lambda x:x[1],reverse=True)
print(a)

# 按姓名字母从小到大
a = sorted(foo,key=lambda x:x[0])
print(a)