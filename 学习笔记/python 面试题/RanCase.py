# 题目7：python中生成随机整数、随机小数、0--1之间小数方法
# 随机整数：random.randiant(a,b),生成区间内的整数
# 随机小数：用numpy库，利用np.random.randn(5)生成5个随机小数，0-1随机小数：random.random(),括号中不传参
import random
import numpy as np

# 设置正整数区间
result = random.randint(10,20)
# 设置生成随机小数的个数
res = np.random.randn(5)
# 括号中不能传参
ret = random.random()
print("正整数",result)
print("5个随机小数",res)
print("0-1随机小数",ret)
