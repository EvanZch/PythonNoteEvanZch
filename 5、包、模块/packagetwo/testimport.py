import test
import testpackage.test  # 这里导入包下的包中的模块

# 通过上面导入，获取数据时候，只能通过testpackage.test.xx
# 我们可以通过as xx 来讲前面的改成后者，后续使用模块里面内容可以直接使用as后面进行导入，简化，避免太长了
import testpackage.test as evan   # 使用 print(evan.b)

print(test.a) # "测试数据"
print(testpackage.test.b) # 这是pakagetwo下testpackage包下test.py模块


print(evan.b) # 这是pakagetwo下testpackage包下test.py模块
