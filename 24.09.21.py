import numpy as np
print(np.arange(12))
data = np.arange(12).reshape(3, 4)
print(data)
print(type(data))
print(data.ndim)    #Note: dimension(维度)
print(data.shape)   #Note: shape（形状）
print(data.size)    #Note: size （元素个数）
print(data.dtype)   #Note: dtype（数据类型）
