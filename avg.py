student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height=0   
for total in student_heights:
  total_height =total_height + total
#print(total_height)    

ns=0
for st in student_heights:
  ns=ns+1
#print(ns)     

average_height=total_height/ns   
print("average height of the students:",round(average_height))





