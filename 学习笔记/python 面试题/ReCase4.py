# a="张明 98分"，用re.sub，将98替换为100
import re
a = "张明 98分"
ret = re.sub(r"\d+","100",a)
print(ret)