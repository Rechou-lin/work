'''
by lin
2019.4.8
'''
import random 
a=[]
with open('d:/lin/work2','w+') as f:
    for i in range(50):
        a.append(int(random.random()*1000))
    for i in range(49):
        for j in range(i,50):
            if a[i]>=a[j]:
                a[i],a[j]=a[j],a[i]
    # print(a)
    for i in range(50):
        a[i]=str(a[i])
        f.write(a[i])
        f.write(' ')

with open('d:/lin/work2','r') as f:
    print(f.read())
with open('d:/lin/work2','r') as f:    
    b=f.read()
    # print(b)
    b=b.split(' ')
    # print(b)
    b=b[-1::-1]
    b.pop(0)
    # print(b)
    with open('d:/lin/work2','a+') as f:
        f.write("\n")
        for i in range(50):
            f.write(b[i])
            f.write(' ')
print("\n")
with open('d:/lin/work2','r') as f:    
    print(f.read())