import numpy as np
a = np.array([1,1,4,3])
b = np.arange(4)    # b=[0,1,2,3]
c = a.dot(b)        # 数值乘法
print(c)
d = np.dot(a,b)     #作用相同
print(d)
e = np.random.random((2,4)) # 两行四列矩阵，元素值范围是[0,1)
print(np.sum(e))
print(np.min(e)) 
print(np.max(e))