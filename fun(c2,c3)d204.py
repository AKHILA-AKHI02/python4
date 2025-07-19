def fun(a,b,c):
    temp=" "
    if a>b:
        a,b=b,a
    for i in range(a,b+1,c):
        temp=temp+str(i)+','
    return temp[0:-1]
c2=int(input("enter a value:"))
c4=int(input("enter a value:"))
c6=int(input("enter a value:"))
print(fun(c2,c3,c6))
