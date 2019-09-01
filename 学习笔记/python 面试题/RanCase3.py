import random
ran_choice = random.choice(['apple','pear','banana'])
print(ran_choice)

# 取样无需更换？？
ran_sample = random.sample(range(100),10)
print(ran_sample)

# 选择随机小数
ran_random = random.random()
print(ran_random)

# 从范围中选择随机整数
ran_randrange = random.randrange(6)
print(ran_randrange)