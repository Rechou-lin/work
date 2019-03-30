menu=eval(input("打开menu请输入1\n退出请输入2\n"))
message={}
while menu != 2:
    n=int(input("增加姓名和手机请输入 1\n删除姓名请输入 2\n修改手机号请输入 3\n查询所有用户请输入4\n查找手机号请输入5\n退出请输入0\n"))
    #1.name & nember
    if n==1:
        name=str(input("name:"))
        if name in message.keys():
            print('该联系人已保存请重新输入\n')
        else:
            number=int(input("number:"))
            message[name]=number
        
    #2.delete name&number
    if n==2:
        name=str(input("whose:"))
        if name in message.keys():
            message.pop(name) 
        else:
            print('该联系人不存在请重新输入\n')
            
            
    #3.change number
    if n==3:
        message[input('whose:')]=int(input('replace number:'))
            
    #4.all contacts
    if n==4:
        print(message)

    #5.seek contact
    if n==5:
        print(message[input('whose')])
	#退出
    if n == 0:
        break
    else:
        pass
