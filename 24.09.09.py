import numpy as np
# 一维矩阵运算
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
c=a-b
print(c)
print(a*b)  #分别相乘
d=b**2  #乘方运算
print(d)
e = np.sin(a) #三角函数
print(e)
print(b<2)