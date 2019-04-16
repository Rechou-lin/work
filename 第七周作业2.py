'''
第七周作业中提高题第1题
by lin
2019.4.16
这段程序使用Mask_II的csv文件
改不动了，不知道50行以后到底什么错了
'''
import numpy as np 
import matplotlib.pyplot as plt
import csv
# 读取第一行
date=[]
with open('d:/lin/python/Mark_II/三5.csv','r+',encoding='utf-8') as f :
    for i,row in enumerate(csv.reader(f)):
        if i ==0:
            date=row
for i in range(5):
    date.pop(0)
print(date)

# 读取考号和成绩
param=dict(
    fname='d:/lin/python/Mark_II/三5.csv',
    delimiter = ',',
    usecols =(0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),
    skiprows=1,
    unpack=False,
    encoding='utf-8'
)
data=np.loadtxt(**param)
#读取名字
param=dict(
    fname='d:/lin/python/Mark_II/三5.csv',
    delimiter = ',',
    dtype=str,
    usecols =3,
    skiprows=1,
    unpack=False,
    encoding='utf-8'
)
name=np.loadtxt(**param)
# print(name)
# print(data)


datefirst=date.index(input('date1:'))#输入日期1
datesecond=date.index(input('date2:'))#输入日期2
x=np.arange(datefirst,datesecond+1,1)

for i in range(42):
    plt.title(data[i,0])
    plt.xlabel('score')
    plt.ylabel('exams dates')
    plt.plot(x,data[i,datefirst+1:datesecond],'co-') 
    plt.ylim(0,100)
    plt.xticks(x,date[datefirst,datesecond])
    param=dict(
    fname=name[i],
    figtype='jpg'
    )
    # plt.savefig(**param)
    plt.show()
