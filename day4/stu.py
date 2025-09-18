class stu:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
    def display(self):
        print(f'roll:{self.roll} name:{self.name} marks:{self.marks}')
        # print("roll",self.roll,"name:",self.name,"marks:",self.marks)
s =stu(1,'rbr',[20,20,40])
s.display()
s2=stu(2,'dham',[20,30,40])
s2.display()

