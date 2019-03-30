date={}
global date_first_len
global date_second_len
date_first=input('请输入日期1:')
date_second=input('请输入日期2:')

date_first=list(date_first.split('.',2))
date_second=list(date_second.split('.',2))
for i in range(3):
    date_first[i]=int(date_first[i])
    date_second[i]=int(date_second[i])
while date_first>date_second :
    print('日期1要大于日期2，请重新输入')
    date_first=input('请输入日期1:')
    date_second=input('请输入日期2:')
a=['年','月','日']
date['日期1']=dict(zip(a,date_first))
date['日期2']=dict(zip(a,date_second))
print(date)
# 求某年某月的天数的函数
def yearlen(year):
    if (year%4 == 0 and year%100 !=0) or year%400==0:
        l=366
    else:
        l=365
    return l
    
def monthlen(year,month):
    if month==2:
        if yearlen(year) == 366:
            b=29
        else:
            b=28
    elif month==1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12 :
        b=31
    else:
        b=30
    return b

date_first_len=date['日期1']['日']-1
date_second_len=date['日期2']['日']-1
while date['日期1']['月'] >1:
    date['日期1']['月']-=1
    date_first_len+=monthlen(date['日期1']['年'],date['日期1']['月'])
    

while date['日期2']['月'] >1:
    date['日期2']['月']-=1
    date_second_len+=monthlen(date['日期2']['年'],date['日期2']['月'])
while date['日期2']['年']>date['日期1']['年']:
    date['日期2']['年']-=1
    date_second_len+=yearlen(date['日期2']['年'])
    
variation=date_second_len-date_first_len
print('相差',variation,'天')
