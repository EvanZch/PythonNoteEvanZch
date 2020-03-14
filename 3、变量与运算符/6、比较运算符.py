##### 比较（关系）运算符


####  == != > < >= <=


#### 同java差不多


print(1 == 1)  # True
print(1 > 1)  # False

a = 1
b = 2
print(a != b)  # True

b = 1
b += b >= 1
print(b)  # 2

# 这里涉及到运算符的顺序，先执行了 b>=1  True ，而True结果为1
# 所以最后结果就变成了 b + = True  而True实际值为1，所以最后结果为2


################  不只是数字才能做比较运算   #########


a = '1'
b = 'b'

print(ord(a))  # 49
print(ord((b)))  # 98
print(a > b)  # False  这里比较的其实是ascii 码值

a = 'abc'
b = 'abd'

print(a < b)  # True 从左到右依次比较

## 列表

print([1, 2, 3] < [2, 3, 4])  # True

## 元组
print((1, 2, 3) < (1, 3, 2))  # True
