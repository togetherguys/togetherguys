import numpy as np
# `=`赋值方式会带有关联性
a = np.arange(4)
print(a) #Note: [0 1 2 3]
b = a
c = a
d = b
a[0] = 11
print(a)
print(b,c,d) # [11  1  2  3] #值会随着a进行改变
print(d is a)
# 如果使用copy的话二者将不再有联系。
A = np.arange(4)
print(a) # [0 1 2 3]
B=A.copy()
A[3]=44
print(A,B)
