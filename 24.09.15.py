import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
print(np.vstack((A,B)))     # Note:上下分别用括号匹配。
C = np.vstack((A,B))
print(C)    # Note:和上面的输出一样。
print(A.shape,B.shape,C.shape)
D = np.hstack((A,B))
print(D)    # Note:左右分别用括号匹配。
print(A.shape,B.shape,D.shape)
print(A[np.newaxis,:]) # Note:[1 1 1]变为[[1 1 1]]。
print(A[np.newaxis,:].shape) #Note: (3,)变为(1, 3)。
print(A[:,np.newaxis])  # Note:[1 1 1]变为[[1] [1] [1]]。