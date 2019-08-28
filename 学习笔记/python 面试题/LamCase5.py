# lambda匿名函数好处
# 精简代码，lambda省去了定义函数，map省去了写for循环过程
a = ["苏州","中国","哈哈","","","日本","","","德国"]
res = list(map(lambda x:"填充值" if x=="" else x,a))
print(res)