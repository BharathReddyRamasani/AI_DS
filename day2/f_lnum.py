x=int(input("enter"))
# def func(x):
#     f=str(x)[0];l=str(x)[-1]
#     print(f)
#     print(l)
#     print(int(f)+int(l))
# func(x)

def func(x):
    f=x
    while f>=10:
        f=f//10
    l=x%10
    return f,l,f+l
print(func(x))