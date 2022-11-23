def ran_check(num,low,high):
    for item in range(low, high):
        if num==item:
            return f'{num} is in the range between {low} and {high}'
        
print(ran_check(4,2,7))