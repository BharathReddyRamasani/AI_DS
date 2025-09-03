cno,pmr,lmr=map(int,input("enter").split())
cname=input("enter cname")
units=pmr-lmr
bill=round(units*3.80,2)
print(f'cn0{cno} cname:{cname} pmr:{pmr} lmr:{lmr} units:{units} cbill:{bill}')




