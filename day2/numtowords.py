x=int(input("enter x:"))
def func(x):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    s=""
    while x>0:
        r=x%10
        s=d[r]+" "+s
        x=x//10
    return s
print(func(x))