student_heights = input("enter height of students :").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
number_of_students = 0
for student in student_heights:
    number_of_students += 1
average = total_height // number_of_students
print(average)