"""
for与range

类比java

for(int x= 0,x<=10;x++){
  ....
}
"""

"""
Demo1、让程序执行十次
"""

for x in range(0, 10):
    print(x, end=",")
else:
    print('end')

# 结果：0,1,2,3,4,5,6,7,8,9,end

"""
Demo2、第三个参数，标识间隔多少
"""
for x in range(0, 10, 2):
    print(x, end=",")
else:
    print('end')

# 0,2,4,6,8,end


"""
Demo3、递减，注意第三个参数是负数，
"""
for x in range(10, 0, -2):
    print(x, end=",")
else:
    print('end')

# 10,8,6,4,2,end


"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
Demo4、练习，打印出1，3，5，7
"""

# for 循环实现
a = [1, 2, 3, 4, 5, 6, 7, 8]

for x in a:
    if (x % 2) ==1:
        print(x,end=',')
else:
    print('end')

# 1,3,5,7,end

# 方式二  for  range实现

for x in range(0,len(a),2):
    print(a[x],end=',')
else:
    print('end')
# 1,3,5,7,end


## 切片实现

b = a[0:len(a):2]
print(b)

#结果： [1, 3, 5, 7]