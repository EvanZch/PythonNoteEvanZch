"""

面向对象
有意义的

类
对象


一、类的定义 class

作用：最基本的作用就是封装

class Student():
    pass


最基本的原则，类只负责去描述和定义，但是不负责去执行代码，比如定义了一个方法，
不能再类中调用这个方法

类的使用：要对类进行实例化

1、类名第一个大写,采用驼峰命名 StudentHomework
2、类里面能做啥？
    定义若干个变量
"""

# 类的定义
class Student():
    # 类里面定义变量
    age = 0
    name = ''

    # 类里面的方法和模块函数的区别
    # 类里面定义方法
    # 参数里面必须要有self关键字
    def print_file(self):
        # 这里不能直接用name,需要用self.name
        print('name:'+ self.name)
        print('age:'+ str(self.age))

class StudentHomework():
    homework_name = ''

# 类的实例化(演示)
student = Student()
student.print_file()



