## 好玩的东西
print(type((1)))  # <class 'int'>
print(type(("hello")))  # <class 'str'>

# 按照我们的想法，type应该是tuple，但是打印结果分别是int和str
# 我们再看这个问题,当我们运算的时候，通过()改变运算顺序

print((1 + 1) * 2)  # 4

# 所以如果括号里面只有一个元素，不会当成元组，而是当成运算符号的()

# 那么问题又来了，我们怎么表示只有一个元素的元组？
print((1))  # 数字1
print((1,))  # 元组(1,)

# 元组里面如果没有数据，是一个空元组
print(())
print(type(()))  # <class 'tuple'>

### 但是列表没有这种说法
print(type([1]))  # <class 'list'>
print(type([]))  # <class 'list'>

## str list tuple 我们都可以看成序列，
'hello world'
(1, 3, 4, 5, 6, 7)
[1, 2, 3, 4, 5]

## 序列里面每个元素都有编号

#####  获取序列长度  len()

print(len((1, 2, 3, 4, 5, 6)))  # 6
print(len(("1", 2, 3, 4, 5, 6)))  # 6
print(len(["1", 2, 3, 4, 5, 6]))  # 6
print(len("hello world"))  # 11

print("----------序列中最值获取")
##### 获取序列中最大值 max()
print(max((1, 2, 3, 4, 5, 6)))  # 6
# print(max(("1", 2, 3, 4, 5, 6)))  # '>' not supported between instances of 'int' and 'str'
# print(max(["1", 2, 3, 4, 5, 6]))  # 6
print(max("hello world"))  # w  根据字符的ascll表大小
##### 获取序列中最小值 min()
print(min((1, 2, 3, 4, 5, 6)))  # 1
print(min("hello world"))  # 返回空格


### 前面说了，字符串获取最值是根据字符的Ascll码来获取的，我们可以通过
### ord() 来获取字符对应的 ascll 码值
print("----------获取字符Ascll值")
print(ord("w"))  # 119
print(ord("d"))  # 100
print(ord(" "))  # 32
