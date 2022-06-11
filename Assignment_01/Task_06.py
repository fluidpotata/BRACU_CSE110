'''Task 6
Write the Python code of a program that reads an integer as input from the user, and prints the integer if it is a multiple of 2 OR 5 and prints "Not a multiple of 2 OR 5" otherwise.

For example, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22 … i.e. this includes multiples of 2 only, multiples of 5 only and multiples of 2 and 5 both.

==========================================================

hint(1): we may use the modulus (%) operator for checking the divisibility

hint(2): we can consider the number to be an integer

==========================================================

Sample Input 1:
5

Sample Output 1:
5

==========================================================

Sample Input 2:
10

Sample Output 2:
10'''

num = int(input("Please enter the number: "))
if num%2==0 or num%5==0:
    print(num)
else:
    print("Not a multiple of 2 or 5")
