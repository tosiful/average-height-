student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

hscore=0
for i in  student_scores:
  if i >hscore:
     hscore=i
print(f"the height score is : {hscore}") 






