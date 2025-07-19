#range100to10
def fun():
    temp=' '
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    for i in range(a,b+1,-10):
         temp=temp+str(i)+" "
    return temp[0:-1]
print(fun())
