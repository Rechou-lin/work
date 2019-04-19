# -*- coding: utf-8 -*-
'''
by lin
2019.4.19
第八周作业第二题

个人觉得拟合得比较合理
我这里初始参数只给了一次，
如果分别给最高温和最低温一次初始拟合参数，
应该拟合效果会更合理
'''
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
def func(p,x):
    '''
    定义一个函数 拟合温度就等于平均温度加温差
    '''
    dtem,avertem,theta=p#dtem--温差， avertem--平均温度， theta--时间偏移引入的
    return avertem+dtem*np.sin(2*np.pi*(1/12)*x+theta)

def residuals(p,y,x):
    '''
    算残缺的函数
    '''
    return y -func(p,x)

# 真实数据
x=np.linspace(1,12,12)
y_max=np.array([17,19,21,28,33,38,37,37,31,23,19,18])
y_min=np.array([-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58])

p0=[-10,30,0]#根据数据大概猜一下参数
pltsq_max=leastsq(residuals,p0,args=(y_max,x))#拟合最高温的
pltsq_min=leastsq(residuals,p0,args=(y_min,x))#拟合最低温的

print('拟合参数',pltsq_max[0])#输出最高温曲线拟合参数
print('拟合参数',pltsq_min[0])#输出最低温曲线拟合参数

pl.rcParams['font.family'] = ['Heiti']
pl.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

pl.plot(x, y_max, label=u"maximum temperature")
pl.plot(x, y_min, label=u"minimum temperature")#画实际温度曲线
pl.plot(x,func(pltsq_max[0],x),label=u'fitting maximum temperature')
pl.plot(x,func(pltsq_min[0],x),label=u'fitting minimum temperature')#画拟合温度曲线
pl.legend()
pl.show()
