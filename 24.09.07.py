import numpy as np
# 一维array
a = np.array([2,23,4], dtype=np.int32) # np.int默认为int32
print(a)
print(a.dtype)
a = np.array([[2,3,4],
              [3,4,5]])
print(a) # 生成2行3列的矩阵
a = np.zeros((3,4))
print(a) # 生成3行4列的全零矩阵
