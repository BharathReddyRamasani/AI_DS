#without agrs and return
# def kmtomiles():
#     x=10
#     print(x*0.621371)
# kmtomiles(10)

#with agrs and no return
# days=int(input("enter days"))
# def dtomy(days):
#     y=days//365
#     m=days//30
#     print(f'years:{y} months:{m}')
# dtomy(days)

#with args and return
# days=int(input("enter days"))
# def dtomy(days):
#     y=days//365
#     m=(days%365)//30
#     return y,m
# print(dtomy(days))

#without args and with return
def sample():
    name="rbr"
    age=21
    return name,age
print(sample())