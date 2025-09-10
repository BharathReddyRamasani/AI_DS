# from collections import Counter
# s=input()
# print(Counter(s))
s=input()
f={}
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
max_e=max(f.values())
min_e=min(f.values())
print("max freq")
for i in f.items():
    if i[1]==max_e:
        print(i)
print("min freq")
for i in f.items():
    if i[1]==min_e:
        print(i)
for i in f.items():
    print(f'{i[0]}{i[1]}',end="")

