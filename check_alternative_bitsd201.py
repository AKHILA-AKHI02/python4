def check_alternative_bits(n):
    res=bin(n)[2:]
    if('00'not in res)and('11'not in res):
        return'True'
    else:
        return'False'
n=int(input("enter the value:"))
print(check_alternative_bits(n))
