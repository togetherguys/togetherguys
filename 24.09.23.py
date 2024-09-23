import numpy as np
data1 = np.array([[1, 2, 3], [4, 5, 6]])
data2 = np.array([[1, 2, 3], [4, 5, 6]])
print(data1 + data2,data1-data2)
print(data1/data2)
print(data1*data2)
arr1 = np.array([[0], [1], [2], [3]])
arr2 = np.array([[1, 2, 3]])
print(arr1+arr2)
#Note:arr1的每个数与arr2的每个数相加。
arr=np.arange(8)
print(arr[1:6:2])   #Note:从索引1到索引6，步长为2。