s=input()
def func(s):
    ca=cd=cs=0
    for i in s:
        if i.isalpha():
            ca+=1
        elif i.isdigit():
            cd+=1
        else:
            cs+=1
    return [ca,cd,cs]
print(func(s))