x=int(input("enter x:"));l=[]
for i in range(1,x+1):
    if x%i==0:
        l.append(i)
for i in l:
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
            break