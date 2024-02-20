#create list
students = input("please enter heights seperated by spaces\n").split()
for n in range(0,len(students)):
    students[n] = int(students[n])
#use for loop to add together
totalheights = 0
for heights in students:
    totalheights += heights
print(f"total of heights is: {totalheights}")
#user for loop to average
avgheights = 0
for heights in students:
    avgheights += heights / len(students)
print(f"average height is: {avgheights}")
#print outputs