def generateOutput(n):
    n=str(n)
    for i in n:
        if i not in'0123456789':
            return'INVALID'
    s=' '
    n=int(n)
    for i in range(0,n+1):
        s=s+str(i)+' '
    return s[0:-1]
x=input("enter the number:")
print(generateOutput(x))
