#### 结合 set()

######## 特性1 ----------->  无序
#### 定义 {}

setValue = {1, 2, 3, 4, 5, 6}
print(type(setValue))  # <class 'set'>

## 因为set集合是无序的，所以一下操作肯定报错
# print(setValue[0])  # 报错 'set' object does not support indexing

######## 特性2 ----------->  不重复
setValue = {1, 1, 2, 3, 3, 4, 4, 5, 6}
# 通过打印结果可以看到，重复元素合并，所以集合里元素不重复
print(setValue)  ## {1, 2, 3, 4, 5, 6}


### 定义空集合错误
print(type({}))  # 这样定义是错误的,返回结果是字典（后面会讲）<class 'dict'>
## 正确定义空集合
print(type(set()))  # <class 'set'>

# ------------------------ set集合支持的操作-------------------

###1、长度
setValue = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6}
print(len(setValue))  # 6  结果也可以看到，集合获取长度，也是剔除了重复元素后的结果
###2、判断元素是否存在  in  not in
print(6 in setValue)  # True
print(10 not in setValue)  # True

#### 3、求多个集合的差集
setValue1 = {1, 2, 3, 4, 5, 6}
setValue2 = {3, 4}
setValue3 = {5}
print(setValue1 - setValue2)  # {1, 2, 5, 6}
print(setValue1 - setValue2 - setValue3)  # {1, 2, 6}

#### 5、多个集合交集

setValue1 = {1, 2, 3, 4, 5, 6}
setValue2 = {3, 4}

print(setValue1 & setValue2)  # {3, 4}

#### 6、多个集合 合集（并集） |
setValue1 = {1, 2, 3, 4, 5, 6}
setValue2 = {3, 4,7}
# 多个集合合并，并去除重复元素
print(setValue1 | setValue2)  # {1, 2, 3, 4, 5, 6, 7}