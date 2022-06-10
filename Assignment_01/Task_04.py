'''
Task 4
Write the Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.

Hint: First, we may check which number is greater

==========================================================

Sample Input 1:
-40
-4

Sample Output 1:
36

Explanation: -4 > -40 so -4 - (-40) = -4 + 40 = 36
'''

#Solve

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))

if num1<num2 :
    result = num2-num1
    print(result)
elif num2<num1 :
    result = num1 - num2
    print(result)
else :
    result = num1 - num2
    print(result)
