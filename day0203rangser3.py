#range100to0
def fun():
    temp=' '
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    for i in range(a,b+1,-1):
         temp=temp+str(i)+" "
    return temp[0:-1]
print(fun())
