# sno,sname=map(str,input("enter sno,sname").split())
# smarks=[int(x) for x in input("enter 3 marks").split()]
# s=0
# for i in smarks:
#     s=s+i

# avg=round(s/3,2)






sno,sname=map(str,input("enter sno,sname").split())
smarks=[int(x) for x in input("enter 3 marks").split()]
s=0
for i in smarks:
    if i>40:
        if i<50:print("grade c")
        elif i>50 and i<70:print("grade b")
        elif i>70 and i<80:print("grade a")
        elif i>80:print("destinction")
        else:print("pass")
    else:print("fail")
    s=s+i
avg=round(s/3,2)
