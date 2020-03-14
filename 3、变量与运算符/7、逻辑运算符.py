########## 逻辑运算符

### and or not
# 主要操作bool类型，返回结果也是bool类型

### and 与  ,同时为真才为True

print(True and True)  # True
print(False and True)  # False

### or 或  有一个为真就为真

print(True or True)  # True
print(False or True)  # True

### not 非  取反

print(not True)  # False
print(not False)  # True
print(not not True)  # True

###################  其他
print(1 and 1)  # 1   ---->  True and True
print('a' and 'b')  # b
print('a' or 'b')  # a

# int float 0 : 被用于 False 非零 表示True
# 字符串  空字符串 False  非空 True

# 空的列表  []  False 非空 True

## 其他类似

print([1] or [])  # [1]
print([] or [1])  # [1]

##### 由于且必须要两个为真才为真，所以一定是要判断到第二个才知道真假
### 所以当结果为真的时候，这里输出后面的结果
print(1 and 2)  # 2
print(2 and 1)  # 1

##### 由于或有一个为真就是真，所以，第一个是真的时候，就直接返回了
print(1 or 2)  # 1
print(2 or 1)  # 2

print(0 or 1)  # 1
