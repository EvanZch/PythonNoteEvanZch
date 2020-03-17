# 局部变量不会覆盖全局变量


# 局部变量跟函数生命周期一致


c= 50  # 全局变量

def add(x,y):
    c = x + y  # c 局部变量
    print(c)
    return c

add(1,2)  # 3
print(c)  # 50


c= 100  # 全局变量

def add(x,y):

    ## 重点，这里的代码
    global c
    c = x + y  # c 局部变量
    print(c)
    return c

add(5,5)  # 10
print(c)  # 10  可以看到，我们加了一个 global
# 这里的全局变量值100也改变了局部变量的值10