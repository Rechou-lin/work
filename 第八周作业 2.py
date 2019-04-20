'''
by lin
2019.4.20
第八周作业第二题 
利用 scipy.optimise.curve_fit 拟合曲线

不知道有没有符合老师的要求
'''
import numpy as np
from scipy.optimize import curve_fit
import pylab as pl

def func(x,dtem,avertem,theta):
    '''
    定义一个函数 拟合温度就等于平均温度加温差
    '''
    #dtem--温差， avertem--平均温度
    return avertem+dtem/2*np.sin(2*np.pi*(1/12)*(x+theta))

# 真实数据
x=np.linspace(1,12,12)
y_max=np.array([17,19,21,28,33,38,37,37,31,23,19,18])
y_min=np.array([-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58])

x1=np.linspace(1,12,100)#为了让拟合曲线更加光滑

popt,pcov=curve_fit(func,x,y_max)
avertem=popt[1]
dtem=popt[0]
theta=popt[2]
yvals_max=func(x1,dtem,avertem,theta)#拟合最高温曲线
print('拟合参数-最高温',avertem,dtem,theta)#输出最高温曲线拟合参数

popt,pcov=curve_fit(func,x,y_min)
avertem=popt[1]
dtem=popt[0]
theta=popt[2]
yvals_min=func(x1,dtem,avertem,theta)#拟合最高温曲线
print('拟合参数-最低温',avertem,dtem,theta)#输出最低温曲线拟合参数


pl.rcParams['font.family'] = ['Heiti']
pl.rcParams['font.sans-serif'] = ['Heiti'] # 步骤一（替换sans-serif字体）
pl.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

pl.plot(x, y_max, label=u"maximum temperature")
pl.plot(x, y_min, label=u"minimum temperature")#画实际温度曲线
pl.plot(x1,yvals_min,label=u'fitting minimum temperature')#画拟合温度曲线
pl.plot(x1,yvals_max,label=u'fitting maximum temperature')#画拟合温度曲线
pl.legend()
pl.show()
