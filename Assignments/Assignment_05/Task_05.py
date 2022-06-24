tuple1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
counter = 0
check = int(input("Please enter your desired number: "))
for i in tuple1:
    if i==check:
        counter += 1
print(f"{check} apperars {counter} times in the tuple")
