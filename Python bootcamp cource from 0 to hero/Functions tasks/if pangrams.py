import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    if (set(alphabet) - set(str1.replace(' ', ''))) == set():
        return True
    else:
        return False
    
print(ispangram("The quick brown fox jumps over the lazy dog"))