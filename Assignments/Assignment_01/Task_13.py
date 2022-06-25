'''Task 13
Write the Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the mark is valid. For example, a student cannot receive -5 or 110 marks. So, the valid marks range is 0 to 100.

hint(1): you can consider the number to be an integer

hint(2): this problem can be solved in two ways: top-down (starts from A) and bottom-up (starts from F)

Marks	          Grade
90 or above	      A
80-89	            B
70-79	            C
60-69	            D
50-59	            E
Below 50	        F
'''


mark = int(input("Please enter the student's mark: "))
if mark>100 or mark<0:
    print("Invalid number")
elif mark<50:
    print("F")
elif mark<60:
    print("E")
elif mark<70:
    print("D")
elif mark<80:
    print("C")
elif mark<90:
    print("B")
elif mark>=90:
    print("A")
