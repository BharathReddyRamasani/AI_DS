sno,sname=map(str,input("enter sno,sname").split())
smarks=[int(x) for x in input("enter 3 marks").split()]
s=0
for i in smarks:
    s=s+i
avg=round(s/3,2)
print(f'sn0:{sno} sname:{sname} total:{s} avgmarks:{avg} ')