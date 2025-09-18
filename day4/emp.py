class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def show(self):
        print(f'name{self.name} salary{self.sal}')
class man(emp):
    def __init__(self, name, sal,dept):
        super().__init__(name, sal)
        # self.name=name
        # self.sal=sal
        self.dept=dept

    def show(self):
        print(f'name:{self.name} sal:{self.sal} dept:{self.dept}')
    
e=emp('rbr',300000)
e.show()
m=man('rbr',3000000,'ds')
m.show()
