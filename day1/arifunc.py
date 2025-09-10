# a,b=map(int,input("enter").split())
# def add(a,b):
#     return a+b
# print(add(a,b))
# def sub(a,b):
#     return a-b
# print(sub(a,b))
# def mul(a,b):
#     return a*b
# print(mul(a,b))
# def div(a,b):
#     return a/b
# print(div(a,b))
# def mod(a,b):
#     return a%b
# print(mod(a,b))


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0
    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

def show_report(student):
        print(f"\nReport for {student.name}")
        print("Marks:", student.marks)
        print("Average:", round(student.average(), 2))
        print("Grade:", student.grade())
s = Student(input("Enter student name: "))
for _ in range(3):
    mark = float(input("Enter mark (0-100): "))
    s.add_mark(mark)

show_report(s)
