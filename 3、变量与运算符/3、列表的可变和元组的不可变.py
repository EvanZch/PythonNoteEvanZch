### 列表的可变和元组的不可变

### list 可变 和 tuple不可变

a = [1, 2, 3]
print(id(a))  # 1790783087176
print(a)
a[0] = "1"

print(id(a))  # 1790783087176
print(a)

print(a.append(4))

print(a)  # ['1', 2, 3, 4]


######### 元组

a = (1, 2, 3, 4)
# a[0] = "1"  报错，元组元素不可改变 'tuple' object does not support item assignment
print(a)

## 提一个问题，我们知道元组不可以修改，但是看下面
a = (1,2,3,[4,5,6])
# 我们知道 a[0] = "1" 会报错，但是下面没问题
print(a[3])  # [4, 5, 6]
print(a[3][0])   # 4
a[3][0] = "改变后"
print(a)  # (1, 2, 3, ['改变后', 5, 6])

#### 元组不可改变，上面例子中我们也只是改变了元组里面的列表
