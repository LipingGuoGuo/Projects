# 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
print("A0",A0)
print(list(zip(("a","b","c","d","e"),(1,2,3,4,5))))
print(A2)
print(A3)