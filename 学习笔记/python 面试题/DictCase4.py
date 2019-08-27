# 根据键对字典排序（不用zip)
dic = {"name":"zs","sex":"man","city":"bj"}

foo = dic.items()
foo = [i for i in foo]
print("字典转换成列表嵌套元祖",foo)

b = sorted(dic.items(),key=lambda x:x[0])
print("根据键排序",b)

new_dic = {i[0]:i[1] for i in b}
print("字典推导式构造新字典",new_dic)