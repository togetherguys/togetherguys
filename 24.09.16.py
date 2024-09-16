import numpy as np
A = np.arange(12).reshape((3,4))
print(A)
print(np.split(A, 2, axis=1))   # Note:split along axis 1,沿列方向切割。（2个子矩阵）
print(np.split(A,3,axis=0)) # Note:split along axis 0,沿行方向切割。（3个子矩阵）
print(np.array_split(A,3,axis=1))   # Note:array_split along axis 1,沿列方向切割。（3个子矩阵）
print(np.vsplit(A,3)) # Note:vsplit along axis 0,沿行方向切割。（3个子矩阵）
print(np.hsplit(A,2))   # Note:hsplit along axis 1,沿列方向切割。（2个子矩阵）  [737]

