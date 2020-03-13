#进制表示
#0b表示二进制
print(0b10) # 2
print(0b11) # 3

#0o表示二进制
print(0o10) # 8
print(0o11) # 9

#0x表示二进制
print(0x1f) # 31

# 十进制直接不需要符号
print(101)  # 101


## 进制转换

# bin() : 其他进制转换成二进制
print(bin(10))  # 0b1010
print(bin(0o12)) # 0b1010
print(bin(0x1f))  # 0b11111

# int() : 其他进制转换成十进制
print(int(0b11111))  # 31
print(int(0o137))  # 95
print(int(0x1fac))  # 8108

# hex() : 其他进制转16进制
print(hex(888))  # 0x378
print(hex(0xffff1))  # 0xffff1
print(hex(0b1111))  # 0xf

# oct() : 其他进制转八进制
print(oct(1234))  # 0o2322
print(oct(0xff123))  # 0o3770443
print(oct(0b1111))  # 0o17
print(oct(0o1234))  # 0o1234
