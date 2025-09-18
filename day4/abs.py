from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass
class circle(shape):
    def __init__(self,r):
        self.r=r
    def show(self):
        print(f'area of circle{3.14*(self.r**2)}')
class rect(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def show(self):
        print(f'area of rectangle{self.l*self.b}')
r=rect(2,3)
r.show()
c=circle(5)
c.show()

    