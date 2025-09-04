x=int(input("enter x"))
def func(x):
    cbill=0
    if x>50 and x<=100:
        cbill=50*3.80+(x-50)*4.20
    
    elif x>100 and x<=200:
        cbill=50*3.80+(x-50)*4.20+(x-100)*5.10
       
    elif x>200 and x<=300:
        cbill=50*3.80+(x-50)*4.20+(x-100)*5.10+(x-200)*6.30
    
    elif x>300:
        cbill=50*3.80+(x-50)*4.20+(x-100)*5.10+(x-200)*6.30+(x-300)*7.50
        
    else:
        cbill=x*3.80
    print(f"the current bill is:{cbill}")       
func(x)

