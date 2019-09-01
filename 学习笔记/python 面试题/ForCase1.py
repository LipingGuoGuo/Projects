# 循环的技巧
# 当在字典中循环时，用items()方法可将关键字和对应的值同时取出
knights = {'gallahad':'the pure','robin':'the brave'}
for k,v in knights.items():
    print(k,v)

# 当在序列中循环时，用enumerate()函数可以将索引位置和其对应的值同时取出
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

# 当同时在两个或更多序列中循环时，可以用zip()函数将其内元素一一匹配
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print('What is your {0}?  It is {1}.'.format(q,a))


# 当逆向循环一个序列时，先正向定位序列，然后调用reversed()函数
for i in reversed(range(1,10,2)):
    print(i)

# 如果按照某个指定顺序循环一个序列，可以用sorted()函数，可以在不改动原序列的基础上返回一个新的排好序的序列
basket = ['apple','orange','pear','banana']
for f in sorted(set(basket)):
    print(f)

# 有时可以在循环时修改列表内容，一般来说改为创建一个新列表是比较简单安全的
import math
raw_data = [56.2,float('nan'),33.3,90,4.4,float('nan')]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)    