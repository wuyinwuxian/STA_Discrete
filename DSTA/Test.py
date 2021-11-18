from DSTA import DSTA
from otherlib import f1,f2,f3

import numpy as np
import matplotlib.pyplot as plt


#初始化
SE = 30   
MaxIter = 500

# #### 测试函数信息
# fun = f1
# Dim = 8
# Range = np.repeat([0,10],Dim).reshape(-1,Dim)


# #### 测试函数信息
# fun = f2
# Dim = 10
# Range = np.repeat([0,49],Dim).reshape(-1,Dim)


#### 测试函数信息
fun = f3
Dim = 20
Range = np.repeat([0,99],Dim).reshape(-1,Dim)


# 实例化一个DSTA对象
dsta = DSTA(fun,Range,SE,MaxIter)

# 迭代优化
dsta.run()
print(dsta.fBest)
# 绘制迭代曲线
plt.plot(dsta.history)
plt.show()