x=int(input("enter x:"))
if x==2:
        print(f'{x} is a prime number')
for i in range(2,x):  
    if x>2 and x%i==0:
        print(f"{x} not prime number")
        break
    else:
        print(f"{x} is a prime number")
