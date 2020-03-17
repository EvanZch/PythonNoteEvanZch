# 函数定义通过 def

"""

一、基本定义
def funcname(parameter_list):
    pass

1、参数可以没有
2、可以通过return返回结果

二、函数的调用


"""


# 1、编写一个函数实现两个数字相加
def add(x, y):
    result = x + y
    return result


# 2、打印输入的参数,这里命名导致重复调用了,就是递归

# def print(code):
#     print(code)

# 在python中对递归有次数限制
# 我们可以通过如下方式来设置递归的次数限制，设置允许的最大递归长度

# import sys
# sys.setrecursionlimit(1000000)  虽然合理设置了很大，但是实际应该也打不到这个次数限制

def print_log(code):
    print("log", code)


a = add_result = add(1, 2)
b = print_log(add_result)  # log 3

# print_log 没有return,所以这里获取的返回结果就是None
print(a, b)  # 3 None
