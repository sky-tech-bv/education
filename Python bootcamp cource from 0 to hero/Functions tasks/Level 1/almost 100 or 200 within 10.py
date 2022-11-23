def almost_there(n):
    if (n>90 and n<110) or (n>190 and n<210):
        return True
    else:
        return False
        
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))