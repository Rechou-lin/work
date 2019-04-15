import numpy as np 
import matplotlib.pyplot as plt
import csv

# 读取并存放文件里的数据
data=[]
with open('d:/lin/python/统计作业/三5.csv','r+') as f :
    for row in csv.reader(f):
        for i in range(0,21):
            data.append(row[i])
data=np.array(data).reshape(43,21)
score=np.array(data[1:43,5:21],dtype=float)

x=np.arange(1,17)
for i in range(42):
    plt.title(data[i+1,0])
    plt.xlabel('score')
    plt.ylabel('exams dates')
    plt.plot(x,score[i],'co-') 
    plt.ylim(0,100)
    plt.xticks(x,data[0,5:21])
    param=dict(
    fname=data[i+1,3],
    figtype='jpg'
    )
    plt.savefig(**param)
    # plt.show()


    


