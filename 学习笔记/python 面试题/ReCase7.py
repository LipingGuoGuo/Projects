# 正则匹配不是以4和7结尾的手机号
import re
tels = ["13100001234","18390901212","10086","18700007777"]
for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]",tel)
    if ret:
        print("想要的结果",ret.group())
    else:
        print("%s 不是想要的手机号" % tel)