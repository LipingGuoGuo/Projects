# 根据键对字典排序
dic = {"name":"zs","sex":"man","city":"bj"}
foo = zip(dic.keys(),dic.values())
foo = [i for i in foo]
print("字典转换成列表嵌套元祖",foo)
b = sorted(foo,key=lambda x:x[0])
print("根据键排序",b)
new_dic = {i[0]:i[1] for i in b}
print("字典推导式构造新字典",new_dic)