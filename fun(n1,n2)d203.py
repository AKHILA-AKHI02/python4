def fun(a,b,c):
    temp=" "
    if a>b:
        a,b=b,a
    for i in range(a,b+1,c):
        temp=temp+str(i)+','
    return temp[0:-1]
n1=int(input("enter a value:"))
n2=int(input("enter a value:"))
n3=int(input("enter a value:"))
print(fun(n1,n2,n3))
