import numpy as np
print(np.around([1,2,5,6,56], decimals=-1))
# Note:对个位进行四舍五入。
print(np.around([1,2,5,6,56], decimals=-2)) 
#Note:看后两位决定是否采用进位。
x = np.arange(1 , 16).reshape((3 , 5))
print(np.diff(x,axis=1))    #Note:计算沿x轴方向的差值。
print(np.diff(x,axis=0))    #Note:计算沿y轴方向的差值。
print(np.floor([-0.6,-1.4,-0.1,-1.8,0,1.4,1.7])) #Note:向下取整。
print(np.ceil([1.2,1.5,1.8,2.1,2.0,-0.5,-0.6,-0.3])) #Note:向上取整。
x = np.array([[1, 0],
       [2, -2],
     [-2, 1]])
print(np.where(x>0,x,0))    #Note:将x中大于0的元素替换为0。
