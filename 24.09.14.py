import numpy as np
A = np.arange(3,15)
print(A)
print(A[3])     #Note: index starts from 0
B = A.reshape(3,4)
print(B)
print(B[2])    #Note:默认第一个是行，第二个是列。
print(B[2,1])
print(B[1,1:3])
for row in B:
    print(row)
for column in B.T:
    print(column)   #Note:借助转置实现行列互换功能。
A = np.arange(3,15).reshape((3,4))
A = np.arange(3,15).reshape((3,4))
# print(A)
print(A.flatten())  #Note:将矩阵拉平。
for item in A.flat:
    print(item)