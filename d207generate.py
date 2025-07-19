def generatelength(s):
    if len(s)<2:
        return "empty string"
    return s[0:2]+s[-2:]
        
inp=input("enter the string")
print(generatelength(inp))
    
