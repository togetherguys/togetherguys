import numpy as np
from numpy import array
a = array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = array([0,1,2])
print(a+b)  #Note:实现按列广播加法操作
b = np.tile([0,1,2],(4,1)) #Note:将数组[0, 1, 2]重复四次，
#Note:并将其沿垂直方向（行方向）排列，形成一个4行3列的二维数组。简言之，它创建了一个形状为(4, 3)的矩阵，每行都是 [0, 1, 2]。
print(a+b)
x = np.array([1, 2, 3, 3, 0, 1, 4])
print(np.bincount(x))   #Note:统计数组中每个元素的出现次数
w = np.array([0.3,0.5,0.7,0.6,0.1,-0.9,1])
print(np.bincount(x,weights=w))
# Note:对x中的元素进行权重求和，按照元素值0~4的顺序排列。
print(np.bincount(x,weights=w,minlength=7)) #Note:后面没有的用0进行补位。


