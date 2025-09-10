lst = [1, 2, 2, 3, 1, 4, 2, 3, 5, 1];c=0
lst2=[]
for i in lst:
    if i in lst2:
        c+=1
        continue
    else:
        lst2.append(i)
print(lst2,c)