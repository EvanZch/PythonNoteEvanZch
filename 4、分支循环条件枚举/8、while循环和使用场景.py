"""
循环语句
while  while else


使用场景:通过判断条件来执行确定循环语句的执行。
"""

############## while 循环


########################
# demo1
########################
# while循环基本结构
# while xxx :
#     pass

# CONDITION = True
#
# while CONDITION:
#     print('while 无限循环')

# 上面程序程序会无限死循环

########################
# demo2
# 2
# 3
# 4
# 5
# 6
########################

# counter = 1
# while counter <= 5:
#     counter += 1
#     print(counter)


########################
# demo3  while  else
# 当while返回结果为False时候，会走else
# 2
# 3
# 4
# 5
# 6
# 执行结束
########################

counter = 1
while counter <= 5:
    counter += 1
    print(counter)
else:
    print('执行结束')






