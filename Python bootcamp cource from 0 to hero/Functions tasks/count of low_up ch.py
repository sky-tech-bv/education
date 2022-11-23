def up_low(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        else:
            pass
    print(f'No. of Upper case characters: {upper}')
    print(f'No. of Lower case Characters: {lower}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday? Is it?'
up_low(s)