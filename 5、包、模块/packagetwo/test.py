
import testpackage



print(testpackage.sys.path)

# 输出：['F:\\PythonWorkSpace\\PythonNoteEvanZch\\5、包、模块\\packagetwo', 'F:\\PythonWorkSpace\\PythonNoteEvanZch', 'E:\\Android\\IDEA\\PyCharm 2019.2.6\\helpers\\pycharm_display', 'E:\\软件安装包\\python\\python37.zip', 'E:\\软件安装包\\python\\DLLs', 'E:\\软件安装包\\python\\lib', 'E:\\软件安装包\\python', 'E:\\软件安装包\\python\\lib\\site-packages', 'E:\\Android\\IDEA\\PyCharm 2019.2.6\\helpers\\pycharm_matplotlib_backend']
# 这里能打印出结果是因为，在testpackage  _init_ module里面批量导入了sys等module,所以可以
# 在这里通过包名.module名.变量或者函数
a = "测试数据"
