def animal_crackers(text):
    a,b = tuple(text.split())
    if a[0]==b[0]:
        return True
    else:
        return False
        
print(animal_crackers('Levelheaded Llama'))