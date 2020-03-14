### 字符串运算

## +  字符串拼接

print("hello"+"world")  # helloworld

## *

print("hello"*3)  # hellohellohello
print("hi"*2)  # hihi
#print("hell0"*"world")  # 错误 can't multiply sequence by non-int of type 'str'

##### 字符串截取
#### 截取单个字符
## 正数，从头到尾 0开始
print("hello world"[0])  # h
print("hello world"[1])  # e
print("hello world"[2])  # l
print("hello world"[5])  # 输出 空格
# print("hello world"[100])    # 报错，越界 IndexError: string index out of range
## 负数，从尾到头  -1开始
# [-n] 从尾到头第n个字符
print("hello world"[-1])  # d
print("hello world"[-3])  # r

#### 截取一段字符
###  [a:b] 取头不取尾

print("hello world"[0:4]) # hell
print("hello world"[0:-1]) # hello worl
print("hello world"[0:-2]) # hello wor
print("hello world"[1:-2]) # ello wor
# 输入大于字符串长度的时候，不报错，截取到最后一个字符串
print("hello world"[1:100])  # ello world

## 不输入，就是直接取到字符串头或者尾
print("hello world"[6:]) # world
print("hello world"[:5]) # hello
print("-----------------------")
print("hello world"[-1:5]) # 输出空 ？

## [-a:b] 负数在前面，倒着数第几位开始
print("hello world"[-5:])  # world
