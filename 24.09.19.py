import numpy as np
x = [[1,3,3],
     [7,5,2]]
print(np.argmax(x,axis=0))
y = np.array([1, 3, 2, 3, 0, 1, 0])
print(y.argmax())   #Note:返回最大值的索引。
print(np.around([-0.6,1.2798,2.357,9.67,13], decimals=0))
#Note:四舍五入,精确到个位。
print(np.around([-0.6,1.2798,2.357,9.67,13], decimals=1))   
#Note:浮点数四舍五入，精确到小数点后一位。
print(np.around([1.2798,2.357,9.67,13], decimals=2))
#Note:decimals指定的是精确的位数。
