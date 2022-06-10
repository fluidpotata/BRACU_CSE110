'''Task 3
Write the Python code of a program that reads two numbers from the user. The program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.

==========================================================

Sample Input 1:
7
3

Sample Output 1:
First is greater

==========================================================

Sample Input 2:
-33
-3

Sample Output 2:
Second is greater

==========================================================

Sample Input 1:
11
11

Sample Output 1:
The numbers are equal
'''
#Solve:
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1>num2 :
    print("First is greater")
elif num1<num2:
    print("Second is greater")
elif num1==num2 :
    print("The numbers are equal")
