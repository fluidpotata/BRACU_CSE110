list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dict1 = {}
for i in list_1:
    (key,value)=i
    if key in dict1.keys():
        dict1[key].append(value)
    elif key not in dict1.keys():
        dict1[key] = []
        dict1[key].append(value)
print(dict1)
