# axis=0:  行  ； axis=1:列 。
import numpy as np
a = np.array([1,1,4,3])
print("sum=",np.sum(a,axis=0))
print("min=",np.min(a,axis=0))
A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A)) # 0(最小元素的索引)
print(np.argmax(A)) # 11(最大元素的索引)
print(np.mean(A)) # 7.5（求均值）
# print(np.average(A)) # 7.5
# print(A.mean()) # 7.5
print(np.median(A)) # 7.5（求中值）
print(np.cumsum(A)) #求前n项和（类似于斐波那契数列）