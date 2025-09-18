n,d=map(int,input().split())
try:
    if d<=0:
        print(f'res:{n/d}')
except:
    print("div by zero error")
else:
    print("no error")
finally:
    print("succesfully executed")