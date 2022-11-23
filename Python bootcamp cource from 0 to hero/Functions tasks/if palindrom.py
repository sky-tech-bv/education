def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(palindrome('helleh'))
print(palindrome('madam'))
print(palindrome('kayak'))
print(palindrome('racecar'))