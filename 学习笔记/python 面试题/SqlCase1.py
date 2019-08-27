# 举例说明SQL注入和解决办法
# 当以字符串格式化书写方式的时候，如果用户输入的有；+SQL语句，后面的SQL语句会执行
# SQL注入
imput_name = "zs"
sql = 'select * from demo where name="%s"' % imput_name
print("正常SQL语句",sql)

input_name = "zs;drop database demo"
sql = 'select * from demo where name="%s"' % imput_name
print("SQL注入语句",sql)

# 通过参数化方式解决??????
params = [input_name]
count = cs1.execute('select * from goods where name="%s"',params)