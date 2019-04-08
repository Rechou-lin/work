import csv
a=[]
average=0
with open('d:\\lin\\python\\aapl.csv','r') as csv_f:
    for row in csv.reader(csv_f):
            a.append(row[5])
# print(a)
a.pop(0)
# print(a)
for i in range(len(a)):
    average+=int(a[i])
average=average/len(a)