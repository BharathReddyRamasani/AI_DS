# l=[]
# for i in range(6):
#     l.append(input())
# l.sort()
# print(l[-2])


l=[]
for i in range(6):
    l.append(input())
e1=l[0];e2=l[1]
for i in l:
    if i>e1:
        e1,e2=i,e1
print(e2)