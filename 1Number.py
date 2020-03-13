
# 基本类型：数字 Number （大分类）
# 整数:int
# 浮点数:float
# type() ： 查看某个变量的基本类型
print(type(1))  # <class 'int'>
print(type(1.1))  # <class 'float'>
print(type(1.111111111111111111111))  # <class 'float'>
print(type(1+1))  # <class 'int'>
print(type(1+1.0))  # <class 'float'>
print(type(1+0.1))  # <class 'float'>

print(type(1*1))  #<class 'int'>
print(type(1*1.0))# <class 'float'>
print(type(1/1))# <class 'float'>
print(1/1) #1.0  除法，结果转为float
print(1//1)#1 整除，保留整数部分
print(type(1//1))#<class 'int'>

# bool ： 表示真假

print(True)
print(False)
# print(true) 错误写法
print(type(True))
print(type(False))

## 为什么把 bool划到 Number这个分类下？
# 把True和False转为十进制
print(int(True)) # 1
print(int(False)) # 0

print(bool(1)) # True
print(bool(0)) # False

print(bool(1213)) # True
print(bool(-1213)) # True
print(bool(-1.1)) # True
print('-----------')
print(bool('abc'))  # True
print(bool(''))  # False

print(bool(None)) # False

## complex 复数

# 数字后面用小写j表示
print(30j)  # 30j
print(type(30j))  # <class 'complex'>
