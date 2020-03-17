"""
构造函数


名字固定为 __init__
   def __init__(self):
        pass

"""


# 模板
class Student():
    #
    age = 0
    name = ''

    # 定义构造函数
    # 构造函数，只能返回None,不能返回其他
    def __init__(self):
        print("student")

    def __init__(self,name,age):
        print("student")
        # 可以在构造函数里面初始化值
        # 注意这里的赋值，还是要用self.name和self.age
        self.name = name
        self.age = age

    def do_homework(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


# 实例化  在实例化的时候就会自动调用构造函数

# student1.__init__()  所以基本没有必要通过方法去调用构造函数
student1 = Student('evan', 25)
# student2 = Student()
# student3 = Student()

# a = student1.__init__()  # 基本没有这样操作，因为在实例化的时候，就会去自动去调用这个方法
# print(a, type(a))  # None <class 'NoneType'>

student1.do_homework()

# print(id(student1), id(student2), id(student3))  # 1832771859512 1832771861416 1832771892448


# 构造函数作用：对参数进行赋值等等