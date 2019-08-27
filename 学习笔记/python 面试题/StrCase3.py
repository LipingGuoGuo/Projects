# 用两种方法去空格
str = "hello world ha ha"
res = str.replace(" ","")
print(res)

list = str.split(" ")
res = "".join(list)
print(res)