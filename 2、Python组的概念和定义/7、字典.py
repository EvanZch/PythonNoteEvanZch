##### 字典  dict

### 不是序列
## 特性  key value
## 定义 同样使用花括号 {key1:value1,key2:value2}

print(type({1: 1, 2: 2}))  # <class 'dict'>

dictValue = {"射手": "后羿", "法师": "安琪拉", "坦克": "程咬金", "刺客": "猴子", "辅助": "蔡文姬"}

print(type(dictValue))  # <class 'dict'>

## 不是序列，所以不能进行下面的操作，比如

# print(dictValue[0]) 执行报错。


### 空的字典
print(type({}))  # <class 'dict'>

### 字典正确访问方式：通过key来获取Value

print(dictValue["射手"])  # 后羿
print(dictValue["辅助"])  # 蔡文姬

## 如果字典出现两个相同的Key（不会存在的）
dictValue1 = {"射手": "后羿", "射手": "伽罗", "法师": "安琪拉", "坦克": "程咬金", "刺客": "猴子", "辅助": "蔡文姬"}

print(dictValue1["射手"])  # 伽罗

# 为什么打印会是伽罗，我们直接打印数据看
# 从结果看，当出现两个key相同的时候，字典会自动把前面相同key
print(dictValue1)  # {'射手': '伽罗', '法师': '安琪拉', '坦克': '程咬金', '刺客': '猴子', '辅助': '蔡文姬'}


#### key可以是不同类型的(可以是任意一种类型)
dictValue2 = {1:"后羿","1":"伽罗"}
print(dictValue2)  # {1: '后羿', '1': '伽罗'}

#### value 也可以是字典
dictValue3 = {1:dictValue2,2:"云中君"}
print(dictValue3)  # {1: {1: '后羿', '1': '伽罗'}, 2: '云中君'}



#### key 是不可变类型