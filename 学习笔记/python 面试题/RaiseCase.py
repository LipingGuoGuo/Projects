# 写一段自定义异常代码
# raise自定义异常
def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)


fn()