import numpy as np
x = np.array([12, 9, 13, 15])
y = np.array([11, 10, 4, 8])
print(np.multiply(x,y)) 
print(np.greater(x, y)) # Note：默认x>y，看结果为True OR False。
arr_x = np.array([1, 5, 7])
arr_y = np.array([2, 6, 8])
arr_con = np.array([True, False, True]) # Note:True为arr_x，False为arr_y(从不同位置取值后重新拼接。)
result = np.where(arr_con, arr_x, arr_y)
print(result)
arr = np.array([[1, -2, -7], [-3, 6, 2], [-4, 3, 2]])
print(np.any(arr>0))    # Note：只要有一个元素大于0，就返回True。
print(np.all(arr>0))    # Note：所有元素都大于0，才返回True。
print(np.unique(arr))   # Note：提取数组中的唯一元素。
