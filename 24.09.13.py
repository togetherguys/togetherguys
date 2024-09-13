import numpy as np
B = np.array([[3,5,9],
              [4,8,10]])
print(np.diff(B))    
#Note该Python函数计算并打印数组B中每行元素的差值。具体来说：

# 计算第一行差值：[5-3=2], [9-5=4]
# 计算第二行差值：[8-4=4], [10-8=2]
# 最终输出结果为：[[2 4] [4 2]]
C = np.array([[0,5,9],
              [4,0,10]])
print(np.nonzero(C))
# print(np.where(C==0)) 行索引
# print(np.where(C==0)[0])  列索引
# 需要将二者组合起来看
A = np.arange(14,2,-1).reshape((3,4)) # -1表示反向递减一个步长
print(A)
# 构造等差数组，从14到3，递减4个元素。
print(np.sort(A))   # 对数组A进行升序排序。
print(np.transpose(A))  # 转置数组A,相当于print(A.T)。
print(np.clip(A,5,9))
# Note:该函数使用np.clip将数组A中的元素限制在指定范围[5, 9]内。具体功能如下：

# 将小于5的元素值设为5。
# 将大于9的元素值设为9。
# 保留处于5和9之间的元素不变。最终打印处理后的数组






