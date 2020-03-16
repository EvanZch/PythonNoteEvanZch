"""
流程控制语句之条件判断三

snippet
多层判断
代码块

"""

################# snippet 片段演示
# 左右，快速构建代码片段
# snippet pycharm 可以配置
#----------------------------------
# pass 空语句，占位语句，保持代码的完整性

# 这样不会报错，但是没有什么执行
if True:
    pass

# 这样会报错，if里面没有语句 unexpected EOF while parsing
# if True:

###################### 多层判断

a = 90
if a >= 80:
    print("优秀")
elif a >= 60:
    print("良")
elif a >= 40:
    print("差")
else:
    print("渣渣")

# 代码块
# 伪代码：用代码表示思想，但是并不是真正的执行

# 其中codexx就是代码块，这里用伪代码表示

# if True:
#     code1
#     code2
#     code3
# else:
#     code4
#     code5

# if True:
#     code1
#     code2
#         code22
#         code23
#             code231
#             code232
#     code3
# else:
#     code4
#     code5






