# 生成1-100的随机数
import random

# 随机小数
res1 = 100*random.random()

# 随机整数
res2 = random.choice(range(0,101))
# 随机整数
res3 = random.randint(1,100)
print(res1)
print(res2)
print(res3)