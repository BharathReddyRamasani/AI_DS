s1=input();s2=input()
def func(s1,s2):
    c1=c2=0
    for i in s1:
        c1+=1
    for i in s2:
        c2+=1
    print(c1,c2)
    print(s1+s2)
    print(s1==s2)
func(s1,s2)
