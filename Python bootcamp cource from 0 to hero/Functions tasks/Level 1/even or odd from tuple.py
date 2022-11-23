def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return a
    elif a%2!=0 or b%2!=0:
        return b
    
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))