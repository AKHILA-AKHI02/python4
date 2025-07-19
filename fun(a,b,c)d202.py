def fun(a,b,c):
    temp=" "
    if a>b:
        a,b=b,a
    for i in range(a,b+1,c):
        temp=temp+str(i)+','
    return temp[0:-1]
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=int(input("enter a value:"))
print(fun(a,b,c))
