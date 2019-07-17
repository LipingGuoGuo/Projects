from Priority.PriorityQueue import PriorityQueue


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    # 第一个pop()返回优先级最高的元素
    print(q.pop())
    print(q.pop())
    # 相同优先级的元素（foo和grok），pop操作按照被插入的顺序返回
    print(q.pop())
    print(q.pop())