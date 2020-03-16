## 在循环操作中，我们可能会经常用到


# break : 强行终于当前循环，且后续循环都不执行。

# continue : 继续，跳出本次循环，继续后面的循环


# 重点：如果for循环不是正常结束（比如使用了break强行终止），不会执行else后面代码

a = [2,3,4,5,6]
for x in  a:
    if x == 4:
        break
    print(x,end=",")
else:
    print("end")


print()
# 结果:2,3, 这里因为使用了break强行终止了程序，所以else中的代码并没有执行

# continue会继续执行
a = [2,3,4,5,6]
for x in  a:
    if x == 4:
        continue
    print(x,end=",")
else:
    print("end")

# 2,3,5,6,end   我们看到出了4没有打印，其他都执行了，且走了else方法