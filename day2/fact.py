x=int(input("enter x:"))
def fact(x):
    if x==0 or x==1:
        return 1
    else: return x*fact(x-1)
print(f"factorial of {x} is {fact(x)}")
fact(x)
