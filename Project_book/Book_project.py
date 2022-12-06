dracula_object = open('dracula.txt', encoding='cp437')
text = dracula_object.read()
words = text.split()

vampire_count = 0
for object in words:
    if "Vampire" in object:
        vampire_count = vampire_count + 1
    if "vampire" in object:
        vampire_count = vampire_count + 1

print("The word Vampire appears", vampire_count, "times")
dracula_object.close()