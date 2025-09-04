x=int(input("enter x:"))
def func(x):
    notes10=0;notes20=0;notes50=0;notes100=0;notes200=0;notes500=0;notes2000=0
    if x>0:
        if x>10 and x<20:
            notes10= x//10
        elif x>=20 and x<50:
            notes20=x//20
            notes10=(x%20)//10
        elif x>=50 and x<100:
            notes50=x//50
            notes20=(x%50)//20
            notes10=((x%50)%20)//10
        elif x>=100 and x<200:
            notes100=x//100
            notes50=(x%100)//50
            notes20=((x%100)%50)//20
            notes10=(((x%100)%50)%20)//10
        elif x>=200 and x<500:
            notes200=x//200
            notes100=(x%200)//100
            notes50=((x%200)%100)//50
            notes20=(((x%200)%100)%50)//20
            notes10=((((x%200)%100)%50)%20)//10
        elif x>=500 and x<2000:
            notes500=x//500
            notes200=(x%500)//200
            notes100=((x%500)%200)//100
            notes50=(((x%500)%200)%100)//50
            notes20=((((x%500)%200)%100)%50)//20
            notes10=(((((x%500)%200)%100)%50)%20)//10
        elif x>=2000:
            notes2000=x//2000
            notes500=(x%2000)//500
            notes200=((x%2000)%500)//200
            notes100=(((x%2000)%500)%200)//100
            notes50=((((x%2000)%500)%200)%100)//50
            notes20=(((((x%2000)%500)%200)%100)%50)//20
            notes10=((((((x%2000)%500)%200)%100)%50)%20)//10
        else:
            notes10=x//10
        print(f"the number of 2000 notes is:{notes2000}")
        print(f"the number of 500 notes is:{notes500}")
        print(f"the number of 200 notes is:{notes200}")
        print(f"the number of 100 notes is:{notes100}")
        print(f"the number of 50 notes is:{notes50}")
        print(f"the number of 20 notes is:{notes20}")
        print(f"the number of 10 notes is:{notes10}")
    else:
        print("invalid input")
func(x)


        

        