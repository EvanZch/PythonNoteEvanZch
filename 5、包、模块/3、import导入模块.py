## 通过import导入模块



"""
方式一
import 包名.模块名字
使用 包名.模块名.xxxx
方式二、
如果包层级过多，会导致输入内容很长，我们可以通过
import 包名.模块名 as a   a为自定义参数，后续调用可以直接通过xx进行调用
使用： a.xxxx
"""
# 通过上面导入，获取数据时候，只能通过testpackage.test.xx
# 我们可以通过as xx 来讲前面的改成后者，后续使用模块里面内容可以直接使用as后面进行导入，简化