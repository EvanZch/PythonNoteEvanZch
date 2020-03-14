### 列表 list
## 列表定义 eg：[1,2,3,4,5,6]

print(type([1, 2, 3, 4, 5]))  # <class 'list'>

# 列表里面可以混合基本类型数据
print(type(["hello", 1, 2, "world"]))  # <class 'list'>
print(type(["hello", 1, 2, "world", True, False]))  # <class 'list'>

## 列表里面的元素可以是列表
### 嵌套列表
print(type([[1, 2, 3], [4, 5], 6, "hello"]))  # <class 'list'>
