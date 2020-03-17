"""
区别模块变量和类中的变量

模块中的变量位置  3章-1.1

类中的变量

类变量  实例变量


"""

class Student():
    # 类变量
    age = 0
    name = ''

    # 定义构造函数
    # 构造函数，只能返回None,不能返回其他
    def __init__(self):
        pass
    def __init__(self,name,age):
        # 可以在构造函数里面初始化值
        # 注意这里的赋值，还是要用self.name和self.age


        self.name = name
        self.age = age

    def do_homework(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


student1 = Student('evan', 25)
