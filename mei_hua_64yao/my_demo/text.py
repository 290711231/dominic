# -*- coding: utf-8 -*-


import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import random

#y = np.array([random.randint(0, 5) for _ in range(10)])
#x = np.array([num for num in range(10)])
#
#xnew = np.arange(0, 9, 0.1)
#
#func = interpolate.interp1d(x, y, kind='cubic')
#ynew = func(xnew)
#
#plt.plot(x, y, 'ro-')
#plt.plot(xnew, ynew)
#plt.show()


# 计算正弦曲线上点的 x 和 y 坐标
z1 = []
z2 = []
x = np.arange(0, 8* np.pi,0.5)*100
y = np.sin(x)*40

plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()