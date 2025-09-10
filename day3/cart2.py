l=["laptop","bike","mobile","car"]
def add(add_item):
    l.append(add_item)
    print(l,len(l))
def remove(rem_item):
    l.remove(rem_item)
    print(l,len(l))
def exist(che_item):
    if che_item in l:
        print(f'yes {che_item} is avaliable')
    else:
        print(f'{che_item}is not avaliable')
def display():
    print(l)
def len_cart():
    print(len(l))
def sort_():
    l.sort()
    print(l)
def clear_():
    l.clear()
print(l)
print("1:add,2:check,3:remove,4:display,5:total carts,6:sort,7:clear")
while(True):
    n=int(input("entet ope no range 1 to 7"))
    match n:
        case 1:
            add_item=input("enter add item")
            add(add_item)
        case 2:
            che_item=input("enter checkitem")
            exist(che_item)
        case 3:
            rem_item=input("enter remitem")
            remove(rem_item)
        case 4:
            display()
        case 5:
            len_cart()
        case 6:
            sort_()
        case 7:
            clear_()
        case _:
            print("invalid input")
