# _init_.py 模块的使用

# 前面说了，这个模块是包的标识


# 作用：当一个包被导入的时候，这个文件的代码会自动执行

# 可以在这里限制moudle的引入，通过_all_= ['module 名字']
# 指定的module才可以被导入


# 可以在_init_module里面进行module的批量导入
# 在_init_里面对module批量导入后，可以在其他module直接导入包，通过包使用里面导入的模块

# import t   print(t.sys.path)