# 列表嵌套列表排序，年龄数字相同怎么办？
foo = [["zs",19],["ll",54],
        ["wa",23],["df",23],
        ["xf",23]]

# 年龄相同，添加参数，按照字母排序
a = sorted(foo,key=lambda x:(x[1],x[0]))
print(a)
a = sorted(foo,key=lambda x:x[0])
print(a)