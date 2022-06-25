'''Task 9
Write the Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds. The number of seconds is taken as input from the user.

==========================================================

hint(1): we may consider our user input to be an integer value and use // and % operators to solve the problem

hint(2): 1 hour = 60 mins = 3600 seconds and 1 min = 60 seconds

==========================================================

Sample Input 1:
10000

Sample Output 1:
Hours: 2 Minutes: 46 Seconds: 40

Explanation:
10000 seconds = 10000 // 3600 = 2 hours and 10000 % 3600 = 2800 seconds.
Then again, 2800 // 60 = 46 minutes and 2800 % 60 = 40 seconds.
And hence we have arrived at our answer.'''

sec = int(input("Please input total seconds: "))
hours = sec // 3600
rem_sec = sec%3600
minutes = rem_sec//60
seconds = rem_sec%60
print("Hours:", hours,"Minutes:", minutes, "Seconds:", seconds)
