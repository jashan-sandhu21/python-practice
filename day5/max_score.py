student_scores = input("Enter the student scores: ").split()
for n in range (0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for n in student_scores:
    if n > max_score:
        max_score = n 
print(f"maximum score is {max_score}")