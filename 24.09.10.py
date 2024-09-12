import numpy as np
a = np.array([1,1,4,3])
b = np.arange(4)       #b=[0,1,2,3]
print(a==b)
m = np.array([[1,1],[0,1]])     #以行序为主序创建矩阵
n = np.arange(4).reshape((2,2)) #生成2*2矩阵
print(m)
print(n)