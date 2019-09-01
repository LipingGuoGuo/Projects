# 生成器表达式
# 某些简单的生成器可以写成简洁的表达式代码
# 所用语法类似列表推导式，外层为圆括号而非方括号
# 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存
print(sum(i*i for i in range(10)))

xvec = [10,20,30]
yvec = [7,5,3]
print(sum(x*y for x,y in zip(xvec,yvec)))

# from math import pi,sin
# sine_table = {x:sin(x*pi/180) for x in range(0,91)}
# unique_words = set(word for line in page for word in line.spilt())
# valedictorian = max((student.gpa,student.name) for student in graduates)
data = "golf"
list = list(data[i] for i in range(len(data)-1,-1,-1))
print(list)