x=int(input("enter x:"))
for i in range(1,x+1):#153,370
    t=i;r=0
    while t>0:
        d=t%10
        r=r+d**3
        t=t//10
    if i==r:
        print(i,end=" ")