def fun(n):
    nb=bin(n)[2:]
    return nb.count('0')
n=int(input("enter the value"))
print(fun(n))
    

    
