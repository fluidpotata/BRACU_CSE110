dict1 = {}
sum = 0
counter = 0
input1 = int(input("How many input you want? "))
for i in range(input1):
    key = input("Please enter your key: ")
    value = int(input("Please enter your value: "))
    dict1[key] = value
for i in dict1.values():
    sum += i
    counter += 1
average = sum//counter
print(f"Average is {average}.")
