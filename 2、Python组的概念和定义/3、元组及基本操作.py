#### 元组  tuple

# 定义 （1,2,3,4,5）
tuple = (1, 2, 3, 4, 5)
print(type(tuple))  # <class 'tuple'>

## 元组元素基本类型一样可以混合

#### 元组操作
## 元素获取
print(tuple[3])  # 4
print(tuple[1:3])  # (2, 3)
print(tuple[-1])  # 5
print(tuple[-1:]) # (5,)

## 元素拼接
tuple2 = (6, 7, 8)

print(tuple+tuple2)  # (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple2 * 3) # (6, 7, 8, 6, 7, 8, 6, 7, 8)

