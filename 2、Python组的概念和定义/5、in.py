#### in 对序列的操作，用来判断某个字符是否在序列中
str = "hello world"
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)

print('e' in str)  # True
print('eo' in str)  # False
print('el' in str)  # True
print(7 in list)  # False
print([1, 2] in list)  # False
print(2 in tuple)  # True

# 如果要判断是不是<不在>序列中，not in
print("-------------------------")
print('e' not in str)  # False
print('eo' not in str)  # True
print('el' not in str)  # False
print(7 not in list)  # True
print([1, 2] not in list)  # True
print(2 not in tuple)  # False
