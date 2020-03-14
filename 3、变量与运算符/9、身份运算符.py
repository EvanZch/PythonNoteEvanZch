######### 身份运算符

#### is
#### is not

### 定义：

#### 返回结果 bool

###### 区分is 和 == 区别

## 关系运算符 == 比较值是否相等
## is  比较两个变量身份是否相等  ----> 内存地址

## 通过id判断


a = 1
b = 1.0
print(a == b)  # True
print(a is b)  # False

c = 1
print(a is c)  # True
print(a == c)  # True
## 可以看到id,is 判断内存地址是否相同 == 只是判断值是否相等

print(id(c))  # 140704948474912
print(id(a))  # 140704948474912
print(id(b))  # 2868034449792


#set 集合
a = {1, 2, 3}
b = {2, 1, 3}
print(a == b)  # True
print(a is b)  # False

# 元组
a = (1, 2, 3)
b = (2, 1, 3)
print(a == b)  # False
print(a is b)  # False

################  为什么结果不相同  ###########

## 因为元组属于序列，元素顺序是有关系的，顺序不一样值就不一样
## 集合无序，顺序没有关系

## 关于is为啥不清楚，后续会讲