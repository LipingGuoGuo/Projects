class Reverse:
    """用于向后循环序列的迭代器"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    # 定义一个__iter__()方法来返回一个带有__next__()方法的对象
    # 如果类已定义了__next__()，则__iter__()可以简单地返回self
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        # self.index指序列元素的位置
        return self.data[self.index]


if __name__ == "__main__":
    rev = Reverse("spam")
    for char in rev:
        print(char)