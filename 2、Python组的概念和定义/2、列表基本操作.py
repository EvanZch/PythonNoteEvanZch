list = ["我", "是", "Evan", "zch"]


## 列表元素获取
# 单个截取是元素
print(list[0])  # 我
print(list[-1])  # zch
# 两端截取还是一个列表
print(list[0:3])  # ['我', '是', 'Evan']
print(list[-1:])  # ['zch']

#### 列表元素改变
### 拼接 +
list2 = ["人生苦短", "我用Python"]
print(list+list2)  # ['我', '是', 'Evan', 'zch', '人生苦短', '我用Python']
### * 叠加
print(list2*2) # ['人生苦短', '我用Python', '人生苦短', '我用Python']


print(type([1]))  # <class 'list'>