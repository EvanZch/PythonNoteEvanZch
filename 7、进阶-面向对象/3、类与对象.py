"""
类与对象


什么是类：
行为与特征：变量理解成特征，方法理解成行为
面向对象设计：行为要找对主体

区别：


关系：
通过实例化关联
"""

# 模板
class Student():
    #  这个可以理解成特征
    age = 0
    name = ''

    # 理解成行为
    def print_file(self):
        # 这里不能直接用name,需要用self.name
        print('name:'+ self.name)
        print('age:'+ str(self.age))

    # 在面向对象里面，类的设计：行为要和主体对应
    # 比如这里的打印和Student类没有太多关系，这个行为可以单独一个类来处理

    # 下面这个做作业的行为就跟Student相关，这里没啥问题
    def do_homework(self):
        print('name:'+ self.name)
        print('age:'+ str(self.age))

# 类实例化后表示一个具体的对象
student  = Student()