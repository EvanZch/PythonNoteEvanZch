### 基本类型字符串 str
## 如何表示？
# 单引号，双引号，三引号

# hello world
print('hello world')
print("hello world")
print('''hello world''')

print(type(1))  # <class 'int'>
print(type('1'))  # <class 'str'>

## 为啥要用这么多种方式来摆表示字符串
## let's go  打印这个字符串如果用单引号就有问题
# 单引号 print('let's go')  报错
print("let's go")  # let's go
# 使用转移字符
print('let\'s go') # let's go

### 三引号
## 三引号内内容完全输出，包括换行
print("这是双引号aaaaaaaaaaaaaaaaaaaaaaaaaa"
      "aaaaaaaaaaaaaaaaaaa"
      "aaaaaaaaaa")
print('''这是三引号aaaaaaaaaaaaaaaaaaaaaaaaaa
      aaaaaaaaaaaaaaaaaaa"
      aaaaaaaaaa''')
print('''这是换行转移字符aaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaa''')

