"""
类变量和实例变量


一、类变量
1、和类相关的变量

二、实例变量
1、和对象相关联
"""


class Student():
    # 一个班级所有学生的总数
    sum = 0
    # 类变量
    age = 0
    name = 'haha'

    # 定义构造函数
    # 构造函数，只能返回None,不能返回其他
    def __init__(self,name,age):
        # 可以在构造函数里面初始化值
        # 注意这里的赋值，还是要用self.name和self.age
        # self.name 定义了实例变量，一个和对象相关的实例变量  self.变量名字
        self.name = name
        self.age = age

    def do_homework(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

student1 = Student('evan', 10)
student2 = Student('玉皇大帝', 225)


print(student1.name)  # evan
print(student2.name)  # 玉皇大帝
print(Student.name)  # haha  这里打印的就是类的变量值
