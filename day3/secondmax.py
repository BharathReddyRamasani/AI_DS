# l=[]
# for i in range(6):
#     l.append(input())
# l.sort()
# print(l[-2])


l=[10,-4,7,-7,6,5,1,-6,-9]
e1=l[0];e2=l[1]
for i in l:
    if i>e1: 
        e1,e2=i,e1
    elif i > e2 and i< e1:
        e2 = i
print(e2)