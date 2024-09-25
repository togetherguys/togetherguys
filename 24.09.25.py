import numpy as np
student_name = np.array(['Tom', 'Lily', 'Jack', 'Rose'])
student_score = np.array([[79, 88, 80], [89, 90, 92], [83, 78, 85], [78, 76, 80]])
print(student_score[student_name=='Jack'])  #Note:成绩查询。
print(student_name == 'Jack')   #Note: True or False,判断名字与成绩是否对应。
arr = np.arange(16).reshape((2, 2, 4))
arr1=np.array([4,9,16])
print(arr)
print(arr.transpose(1, 2, 0)) #Note: 轴的交换。
print(arr.swapaxes(2, 1))   #Note: 轴的交换（根据里面输入的轴编号进行转置，只能是0/1/2。）
print(np.sqrt(arr1))
print(np.square(arr1)) 
