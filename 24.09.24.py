import numpy as np
arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(arr2d[:2,:])
print(arr2d[:,0:2]) #Note:打印前两页。
print(arr2d[1, :2]) #Note:打印第二行的前两列。
demo_arr = np.empty((4, 4))               # 创建一个空数组
for i in range(4):
    demo_arr[i] = np.arange(i, i + 4)
print(demo_arr) #Note:按行来看的话是四个等差数列。
student_name = np.array(['Tom', 'Lily', 'Jack', 'Rose'])
print(student_name.shape)