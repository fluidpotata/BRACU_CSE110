dict1 = {}
inp = input("Enter your string: ")
for alphabet in inp.lower():
    if alphabet == " ":
        pass
    elif alphabet not in dict1.keys():
        dict1[alphabet] = 1
    elif alphabet in dict1.keys():
        dict1[alphabet] += 1
print(dict1)
