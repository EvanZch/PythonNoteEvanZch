"""
 判断用户登录
"""

# 常量（形式上的）最好使用大写
# account = "evan"
# password = '123456'
ACCOUNT = 'evan'
PASSWORD = '123456'


# input()  接收用户输入
print('请输入用户名:')
user_account = input()
print('请输入密码:')
user_password = input()

# 逻辑运算符号 and 且 ： 二者同时为真即为真
if (ACCOUNT == user_account) and (PASSWORD == user_password):
    print('登录成功')
else:
    print('登录失败')
