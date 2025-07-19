def generatestring(s):
    mc=s[0]
    temp=mc
    for i in s[1:]:
        if i==mc:
            temp=temp+'$'
        else:
            temp=temp+i
    return temp
inp=input("enter the string:")
print(generatestring(inp))
    
