######### 成员运算符


### 用来判断某个元素是否在一组元素里

### in  在
### not in  不在

a = [1, 2, 3, 4, 5]
print(1 in a)  # True
print(6 in a)  # False

print(1 not in a )  # False
print(6 not in a)  #True


b = 'a'
c = 'hello'

print(b in c)  #False



################  字典

#### 通过key值判断
x = 'a'
z = 1
d = '1'
y = {'1':1}

print(x in y)  # False
print(d in y)  # True
print(z in y)  # False


