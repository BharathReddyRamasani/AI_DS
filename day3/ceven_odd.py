l=[]
for i in range(5):
    l.append(int(input()))
ce=co=0
for i in l:
    if i%2==0:
        ce+=1
    else:
        co+=1
print(ce,co)
