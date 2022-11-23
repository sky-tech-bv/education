'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
'''

def spy_game(nums):
    if 0 in nums:
        first_nums = nums[nums.index(0)+1:]
        if 0 in first_nums:
            second_nums = first_nums[first_nums.index(0)+1:]
            if 7 in second_nums:
                return True
            else:
                return False
        else:
            return False
    else: 
        return False
        
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))