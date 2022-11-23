def master_yoda(text):
    word_list = text.split()
    reverse_list = word_list[::-1]
    return " ".join(reverse_list)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))