'''Task 5
Write the Python code of a program that reads a number, and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.

hint(1): we may use the modulus (%) operator to check for even or odd

hint(2): we can consider the number to be an integer

==========================================================

Sample Input 1:
7

Sample Output 1:
The number is odd

==========================================================

Sample Input 2:
10

Sample Output 2:
The number is even'''

num = int(input("Please input the number: "))
if num%2 ==0:
    print("The number is even")
elif num%2 != 0:
    print("The number is odd")
