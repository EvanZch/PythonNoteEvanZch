"""
循环语句
for和for-else 循环
"""

"""
代码结构
for target_list in expression_list:
    press

和while使用场景区别：
for:用来遍历/循环序列、集合、字典等

"""

"""
Demo1
结果：
1
2
3
4
5
6
"""
a = [1, 2, 3, 4, 5, 6]

for x in a:
    print(x)

"""
Demo2
结果
apple
2
red
"""
a = ["apple",2,"red"]

for x in a:
    print(x)




### 上面可以看到打印结果是竖直一列，我们想要一行打印可以使用 print(x,end='')
# end 里面参数就是我们希望通过什么字符进行拼接，默认是换行符号

"""
Demo3
"""
a = ["apple",2,"red"]

for x in a:
    print(x,end=",")  # 结果  apple,2,red,
    print(x, end="-")

print('----------')
for x in a:
    print(x, end="-")  # 结果：apple-2-red-


######################### for else

"""
for x in y:
    print(xx)
else:
    print(yyy)
    
当y中元素全部解析出来之后，就会走到else中
"""

print()
a = [1,2,3,4,5,6,7]
for x in a:
    print(x,end=',')
else:
    print('end')
# 执行结果： 1,2,3,4,5,6,7,end

print()
a = [[1,2,3,4],(5,6,7,8)]
for x in a:
    for y in x:
        print(y,end=',')
else:
    print('end')

# 结果：1,2,3,4,5,6,7,8,end