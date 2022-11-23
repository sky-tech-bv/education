'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69(arr):
    if 6 in arr:
        if arr[0]==6:
            list1 = []
        else:
            list1 = arr[:arr.index(6)]
        if 9 in arr:
            if arr[-1] == 9:
                list2 = []
            else:
                list2 = arr[(arr.index(9)+1):]
        list_r = list1 + list2
        return sum(list_r)
    else:
        return sum(arr)
        
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))