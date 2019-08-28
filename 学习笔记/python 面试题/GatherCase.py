a = [1,2,3,4]
b = [4,3,5,6]
jj1 = [i for i in a if i in b]
jj2 = list(set(a).intersection(set(b)))

bj1 = list(set(a).union(set(b)))

# 在b中有而a中没有
cj1 = list(set(b).difference(set(a)))
# 在a中有而b中没有
cj2 = list(set(a).difference(set(b)))

print("交集",jj1)
print("交集",jj2)

print("并集",bj1)
print("差集",cj1)
print("差集",cj2)