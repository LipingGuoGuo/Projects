# python正则中search和match
import re


s = "小明年龄18岁  工资10000"
res = re.search(r"\d+",s).group()
print("search结果:search匹配到第一个匹配到的数据",res)


res = re.findall(r"\d+",s)
print("findall结果：满足正则，都匹配，不用加group",res)


res = re.match("小明",s).group()
print("match结果：匹配以“小明”开头的字符串，并匹配出小明",res)

# res = re.match(r"\d+",s)
# print("试错，不加group为none,匹配不到",res)

# res = re.match("工资",s).group()
# print("match结果",res)