

a = [[1,2,3,4,5],(6,7,8)]
for x in a:

    for y in x:
        if y == 4:
            break
        print(y)
else:
    print("end")

"""
1
2
3
6
7
8
end
"""

#这里要分析一个问题，我们前面说，break会直接退出，这里break执行了，4及后面的数据没有打印
# 为啥这里还执行了else中的代码，而且还打印了 6，7，8这三个参数

# 原因，这里使用了两个嵌套循环，我们break是结束了内部的一个循环，else配对的是外部的一个for


# 我们简单改一改代码

a = [[1, 2, 3, 4, 5], (6, 7, 8)]
for x in a:
    print(x,end=",")
    for y in x:
        if y == 4:
            break
        print(y)
else:
    print("end")

"""
结果

[1, 2, 3, 4, 5],1
2
3
(6, 7, 8),6
7
8
end
"""

# 可以看到break只是结束了内部一次循环，但是外部的循环还在继续，所以后面的数据仍然有打印