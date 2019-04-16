'''
第七周作业中提高题第2题
by lin
2019.4.16
这段程序使用Mask_II的csv文件
'''
import numpy as np 
import matplotlib.pyplot as plt

param=dict(
    fname='d:/lin/python/Mark_II/三5.csv',
    delimiter = ',',
    usecols =(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),
    skiprows=1,
    unpack=False,
    encoding='utf-8'
)
data=np.loadtxt(**param)
print(data)
average=np.array(np.average(data,axis=1),dtype=int)

count=np.bincount(average//10)
x=[]
x=range(0,100,10)
plt.bar(x,count,5)
plt.ylabel('distibution')
plt.legend()
plt.title('三5')
plt.xticks(x,['0+','10+','20+','30+','40+','50+','60+','70+','80+','90+'])
for x, count in zip(x,count):
    plt.text(x, count, str(count), ha='center', va='bottom', fontsize=10,rotation=0)
plt.show()