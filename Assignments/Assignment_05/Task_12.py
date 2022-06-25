dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
counter = 0
for items in dict_1.keys():
    for i in dict_1[items]:
        counter += 1
print(counter)
