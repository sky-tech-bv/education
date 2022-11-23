def multiply(numbers):
    result = 1
    for item in numbers:
        result *= item
    return result

print(multiply([1,2,3,-4,5]))