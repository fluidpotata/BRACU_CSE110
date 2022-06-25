given_tuple = (10, 20, 30, 40, 50, 60)
list1 = []

for i in given_tuple:
    list1.append(i)
    
list1.reverse()
output_tuple = tuple(list1)

print(output_tuple)
