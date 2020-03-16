# import test
# # from module import xxx  导入某个模块下的变量或函数，使用的时候直接使用xx即可
# from test import a



from test import *

# 这里通过import导入模块
# 再通过文件名.参数获取数据
# print(test.a) # 10


print(a) # 10 这里时因为通过from test import a直接导入，所以可以直接打印a
print(c) # 12
print(b) # 11

