exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

inp1 = int(input("Enter the marks: "))
new_dict = {}

for key,value in exam_marks.items():
    if value>=inp1:
        new_dict[key] = value
        
print(new_dict)
