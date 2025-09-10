d={}
for i in range(2):
    id=input();name=input()
    d[id]=name
print(d)
def add(id,name):
    d[id]=name
    print(d)
def rem(id):
    del d[id]
    print(d)
def check(id):
    if id in d.keys():
        print(f'{d[id]} is avaliable')
    else:print(f'{d[id]} is not avaliable')
def upd(id,name):
    d[id]=name
def display():
    print(d)
def cou():
    print(len(d))
def checktitle(name):
    if name in d.values():
        print(f'{name} is existed')
    else:print(f'{name} is not exist')
print("1:add,2:remove,3:check,4:update,5:display,6:total books,7:check title")
while(True):
    n=int(input("entet ope no range 1 to 7"))
    match n:
        case 1:
            id=input();name=input()
            add(id,name)
        case 2:
            id=input()
            rem(id)
        case 3:
            id=input()
            check(id)
            
        case 4:
            id=input();name=input()
            upd(id,name)
        case 5:
            display()
        case 6:
            cou()
        case 7:
            name=input()
            checktitle(name)
        case _:
            print("invalid input")
