# l=[1,2,3,4,5]
# l1=[]
# k=int(input())
# for i in range(len(l)):
#     if i==k:
#         continue
#     else:
#         l1.append(l[i])
# print(l1)



l=[1,2,3,4,5]
k=int(input())
l=list(l[:k])+list(l[k+1:])
print(l)