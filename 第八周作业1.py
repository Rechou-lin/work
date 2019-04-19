# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
#定义拟合函数
def func(x, p):
    A, k, theta,b = p
    return A*np.sin(2*np.pi*k*x+theta)+b   

# 定义残差函数
def residuals(p, y, x):
    return y - func(x, p)

# 真实数据
x0= (np.array([0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48]))*np.pi/180
y=np.array([48.5,52.6,27.0,-13.8,-38.0,-29.5,-4.9,25.2,48.6,53.2,
26.7,-16.1,-39.4,-29.9,-3.5,25.2,48.5 ])

x1=np.linspace(0,48*np.pi/180,100)# 将真实数据的x区间细化，因为真实数据的数据量太少。否则拟合曲线不光滑

p0 = [50,2,0,0] # 根据数据大概猜一下参数
plsq = leastsq(residuals, p0, args=(y, x0))#利用最小二乘拟合曲线，并存放拟合曲线的参数

print("拟合参数", plsq[0]) # 实验数据拟合后的参数
pl.rcParams['font.family'] = ['Heiti']
pl.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
pl.plot(x0, y, label=u"real data")#画实际数据的曲线
pl.plot(x1, func(x1, plsq[0]), label=u"fitting data")#画拟合曲线
pl.legend()
pl.show()
