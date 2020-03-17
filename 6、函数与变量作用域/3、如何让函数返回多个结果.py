"""
如果让函数返回多个结果

python对函数返回类型没有任何的限制


def 函数名(x,y):
    return xxx,yyy,.....

二、多个返回结果的获取


通过前面指定具有意义的变量名字来接收对应的返回结果
a1,a2,a3 = 函数()
"""


def change_name(x, y):
    return "改变后" + x, "改变后" + y


a = change_name("evan", "zch")
print(a)  # ('改变后evan', '改变后zch')

print(type(a))  # <class 'tuple'> 返回类型是一个元组

# 既然返回是元组，我们可以这样获取值
# 但是这样的方式，极其不推荐
print(a[0], a[1])  # 改变后evan 改变后zch


## 最好的方式获取 ,序列解包，让有意义的变量名称来接收

x_change_name,y_change_name = change_name("evan", "zch")

print(x_change_name,y_change_name) #改变后evan 改变后zch
