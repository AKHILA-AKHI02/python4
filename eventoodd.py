def fun():
    temp=' '
    a=int(input('enter the value'))
    b=int(input('enter the value'))
    for i in range(b,a-1,1):
        temp=temp+str(i)+' '
        
    return temp[0:1]
print(fun())
##def order():
##    temp=' '
##    a=int(input('enter the value'))
##    b=int(input('enter the value'))
##    for i in range(a,b+1,1):
##        temp=temp+str(i)+' '
##        
##    return temp[0:-1]
##print(order())
