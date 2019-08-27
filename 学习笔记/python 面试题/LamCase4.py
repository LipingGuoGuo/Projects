# 最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
s = ["ab","abc","a","djkj"]
# sorted有返回值，不改变s本身
b = sorted(s,key=lambda x:len(x))
print(b,s)

# sort无返回值，在s自身修改
s.sort(key=len)
print(s)