########## 类型判断

##### 对象三特征  id,value,type

a = 1
print(isinstance(a, int))  # True

print(isinstance(a, str))  # False

print(isinstance(a, (int, str, float)))  # True
