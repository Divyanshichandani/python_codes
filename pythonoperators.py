


#wap to make a calculator that does all arithmatic and logical as well as comparision operations
a=int(input('first digit'))
b=int(input('second digit'))
select=int(input('enter the operation to be performed'))
if  select==1:
    print(a+b)
elif select==2:
    print(a-b)
elif select==3:
    print(a*b)
elif select==4:
    print(a/b)
elif select==5:
    print(a**b) #prints a^b
elif select==6:
    print(a//b)
elif select==7:
    print(a>b)
elif select==8:
    print(a<b)
elif select==9:
    print(a==b)
elif selct==10:
    print(a!=b)
elif select==11:
    print(a>=b)
else: 
    print("not the correct option")

