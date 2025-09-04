from math import factorial as fact
x=int(input("enter x:"))#145
for i in range(1,x+1):
    t=i;s=0
    while t>0:
        d=t%10
        s=s+fact(d)
        t=t//10
    if i==s:
        print(i,end=" ")