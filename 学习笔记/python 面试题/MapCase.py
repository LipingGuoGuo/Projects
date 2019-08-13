# 题目6：列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list = [1,2,3,4,5]
def fn(x):
    """
    map()函数第一个参数是fun ，第二个参数一般是list,第三个参数可以写list，也可以不写(ctrl+b)
    :param x:
    :return:
    """
    return x**2

res = map(fn,list)
res = [i for i in res if i >10]
print(res)
