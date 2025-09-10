l = []
for i in range(5):
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")
    marks = list(map(int, input("Enter 3 subject marks (space-separated): ").split()))
    l.append([roll, name, marks])
t = tuple(l)
print("\nAll Students:")
for i in t:
    print(i)
highest_total = 0
topper = None
for student in t:
    total = sum(student[2])
    if total > highest_total:
        highest_total = total
        topper = student
print("\nTopper (highest marks):")
print(f"Roll: {topper[0]}, Name: {topper[1]}, Marks: {topper[2]}, Total: {highest_total}")
print("\nStudents scoring more than 75 marks (total):")
for student in t:
    total = sum(student[2])
    if total > 75:
        print(f"Roll: {student[0]}, Name: {student[1]}, Marks: {student[2]}, Total: {total}")

