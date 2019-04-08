import pandas as pd 
a=[1,2,3,4,5]
b=['mayi','jack','tom','rain','hanmeimei']
c=[18,21,25,19,23]
d=[99,89,95,80,81]
data = pd.DataFrame({'NO.':a,'Name':b,'age':c,'score':d})
data.to_csv('data.csv',index=False,sep=",")