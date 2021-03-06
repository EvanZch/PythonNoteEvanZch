
########################## 变量操作  #################
a = 1
b = a
a = 3
print(a)  # 3
print(b)  # 1

a = [1, 2, 3, 4, 5]
b = a
a[0] = "1"


# 按我们的理解，这个时候b还是 [1, 2, 3, 4, 5] 但是？
print(a)  # ['1', 2, 3, 4, 5]
print(b)  # ['1', 2, 3, 4, 5]

# 为什么会出现这种现象？？？？

# int ： 值类型  不可改变
# 如果使用上面的来讲，a = 3 的时候，由于int是不可变的，所以只能重新生成将3这个值赋予a
# 但是b还是指向以前的1

# list : 引用类型  可变的
# list属于可变的，当对数据进行 更改的时候，直接对元数据进行更新，而不是从新生成一个数
# 所以，只要有改动，所有指向引用类型的数据值都要改变。


# 值类型：int str 元组(tuple)
# 引用类型：list set dict

########## 我们再看一个Demo
a = "hello"
a = a + "Python"
print(a)  # helloPython
# 我们前面不是说了，str也是不可变类型，为什么这里就没问题呢？
# 其实这里后面的一个a是生成了一个新的字符串，可以通过id()来判断

a = "hello"
print(id(a)) # 2737526759696
a = a + "Python"
print(id(a)) # 2737527119088

# 可以看到两个a的id值并不一样了，说明后者a其实是生成了一个新的字符串




