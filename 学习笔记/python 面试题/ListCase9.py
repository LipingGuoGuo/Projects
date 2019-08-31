# 列表作为栈使用
# 列表方法使得列表作为堆栈非常容易，最后一个插入，最先取出（后进先出）
# 要添加一个元素到堆栈的顶端，使用append()
# 要从堆栈顶部取出一个元素，使用pop（），不用指定索引
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

# 列表作为队列使用
# 先添加的元素最先取出（先进先出），然后列表用作这个目的相当低效，因为在列表的末尾添加和弹出非常快，但是在列表的开头插入或弹出元素却慢(因为所有的其他元素都必须移动一位）
# 要实现一个对列，collections.deque被设计用于快速从两端操作
from collections import deque
quque = deque(["Eric","John","Michael"])
quque.append("Terry")
quque.append("Graphm")
print(quque.popleft())
print(quque)

# 列表推导式
# 列表推导式提供了一个更简单的创建列表的方法、
# 常见的方法是某种用于序列或可迭代的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件来创建子序列
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x:x**2,range(10)))
print(squares)

# 列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个for子句，然后是零个或多个for或if子句
squares = [x**2 for x in range(10)]
print(squares)

list = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list)

# 等价于
list = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list.append((x,y))
print(list)