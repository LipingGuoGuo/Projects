# 正则表达式匹配中，（.*）和（.*?）匹配区别？
s = "<a>哈哈</a><a>呵呵</a>"

# （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
# （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
import re
res1 = re.findall("<a>(.*)</a>",s)
print("贪婪匹配",res1)
res2 = re.findall("<a>(.*?)</a>",s)
print("非贪婪匹配",res2)