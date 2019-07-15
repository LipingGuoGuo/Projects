#### 一、数据结构及算法
##### 1.解压序列赋值给多个变量
###### 1.1解压序列赋值给多个变量
> 任何的序列（或者可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的数量一样    
> 如果变量个数和序列元素的个数不匹配，会产生一个异常 
> 保证选用的那些占位变量名在其他地方没被使用到    
```
>>> data = [1, 64, 445,(1, 3)]
>>> _,shares,price,_ = data
>>> shares
64
>>> price
445
```
###### 1.2利用可迭代对象赋值给多个变量
> 一个可迭代对象的元素个数超过变量个数时，利用星号表达式解决；扩展的迭代解压语法时专门为解压不确定个数或任意个数元素的可迭代对象而设计的   
> 星号表达式在迭代元素为可变长元组的序列时是有用的
```
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
foo 1 2
bar hello
foo 3 4
```
> 星号解压语法在字符串操作的时候有用，比如字符串的分割
---
#### python星号（*）操作符
> 1.函数的可变参数：当函数的参数前面一个`*`表示这是一个可变的位置参数；两个`**`表示是可变的关键字参数
```
def foo(*args,**kwarg):
    for item in args:
        print(item)
    
    for k,v in kwarg.items():
        print(k,v)
    # 输出30个等号做分隔符
    print(30*'=')
    
if __name__ == "__main__":
    foo(1, 2, 3, a=4, b=5)
    foo(2, 3, a=4, b=5,c=1)
   
1
2
3
a 4
b 5
==============================
2
3
a 4
b 5
c 1
==============================
```    
> unpack参数：`*`把序列/集合解包成位置参数，两个`**`把字典解包成关键字参数
```
def foo(*args, **kwarg):
    for item in args:
        print item
    for k,v in kwarg.items():
        print k,v
    print 30*'='

if __name__ == '__main__':
    v = (1, 2, 4)
    v2 = [11, 15, 23]
    d = {'a':1, 'b':12}
    foo(v, d)
    foo(*v, **d)
    foo(v2, d)
    foo(*v2, **d)
```
> 注意点：可变位置参数`*args`是一个元组，是不可修改的；对于字典类型的如果只使用一个`*`，那么传入的只是字典的键
---
##### 1.3保留最后N个元素
> 迭代操作或者其他操作的时候，保留有限历史记录正是`collections.deque`;collections模块在python3库中自带
> 查询元素的代码时，通常使用包含`yield`表达式的生成器函数;使用`deque(maxlen=N)`构造函数会新建一个固定大小的队列   
----
> yield用法！！！！！！！！！！！！！！！
----
```
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
>>> q.append(5)
>>> q
deque([3, 4, 5], maxlen=3)
------------------
>>> a = deque()
>>> a.append(1)
>>> a.append(2)
>>> a.append(3)
>>> a
deque([1, 2, 3])
>>> a.appendleft(7)
>>> a
deque([7, 1, 2, 3])
>>> a.pop()
3
>>> a
deque([7, 1, 2])
>>> a.popleft()
7
>>> a
deque([1, 2])
```
> deque类可以被用在任何简单队列数据结构，不设置最大队列大小，则可得到一个无限大小队列  
> 在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N)
####### 1.4查找最大或最小的N个元素
> 堆数据结构重要特征是最小的或者最大的在堆顶 

