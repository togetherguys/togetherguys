import numpy as np
a = np.arange(10,21,2) # 10-20的数据，步长为2
print(a)
b = a.reshape((2,3))
print(b)
m = np.linspace(1,10,20) # 开始端1，结束端10，且分割成20个数据，生成线段
print(m)
