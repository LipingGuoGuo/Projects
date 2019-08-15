# 字典根据键从小到大排序
dic = {
    "name": "zs",
    "age": 18,
    "city": "深圳",
    "tel": "13456567676"
}
# 根据键排序
list = sorted(dic.items(),
              key=lambda i: i[0],
              reverse=False)
print(list)
# dict函数
print(dict(list))