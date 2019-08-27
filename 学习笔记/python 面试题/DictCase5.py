# python 字典和json字符串相互转换方法
import json

dic = {"name":"zs"}
# 字典转化成json字符串
res = json.dumps(dic)
print(res,type(res))

# json字符串转化成字典
ret = json.loads(res)
print(res,type(ret))