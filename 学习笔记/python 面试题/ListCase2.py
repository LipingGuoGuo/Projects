# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
# 展开列表
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)

# 将列表转成numpy矩阵，通过numpy的flatten()方法
import numpy as np

b = np.array(a).flatten().tolist()
print(b)