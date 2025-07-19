#range 0to100
def fun():
    temp=' '
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    for i in range(a,b+1,5):
         temp=temp+str(i)+" "
    return temp[0:-1]
print(fun())
