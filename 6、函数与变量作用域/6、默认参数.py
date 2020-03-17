"""
默认参数

def add(a =1,b=10):

"""

# 我们这里指定了默认参数
def add(a =1,b=10):
    return a+b

result = add()  # 如果都不传，就直接返回默认参数结果
print(result)  # 11

result = add(10) # 传入一个参数，根据顺序
print(result) #20

result = add(b=100)  # 关键字参数
print(result) # 101

result = add(2,9) # 指定参数
print(result) # 11


##################### 坑整理
"""
1、非默认参数不能放在默认参数后面
2、可以通过关键字参数只改变某一个参数或者某多个参数的值
3、默认值参数和实参不能混合传入

# 错误
# def add(a=1,b):  # 报错 SyntaxError: non-default argument follows default argument
#     return a+b
# add(10)

# 只要有一个参数定义了默认值，后续参数必须也要设置默认值
# 错误
# def add(a,b=1,c):
#     return a+b


# 验证三

def add(a ,b=10,c=11,d=12):
    return a+b+c+d

add(1,b=11,12,d=13)  # 12报错 positional argument follows keyword argument
"""


