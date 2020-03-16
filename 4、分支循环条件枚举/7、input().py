# input()

# 接受用户的输入数据，都是字符串，就算你输入的是1，也会被当做字符串1

# 可以自己转换


# int(xx)


print("请输入一个数字")
a = input()  # 123
print(type(a))  # <class 'str'>

a = int(a)  # <class 'int'>

print(type(a))
