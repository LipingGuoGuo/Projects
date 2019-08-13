import re
str = '<div class="nam">中国</div>'
# .代表可有可无
# *代表任意字符 ，满足类名可以变化
# (.*？)提取文本

res = re.findall(r'<div class=".*">(.*?)</div>',str)
print(res)