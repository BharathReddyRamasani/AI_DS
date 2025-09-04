x=int(input("enter x:"))
for i in range(1,x+1):
    t=i;r=0
    while t>0:
        d=t%10
        r=r*10+d
        t=t//10
        if i==r:
            print(i,end=" ")




        