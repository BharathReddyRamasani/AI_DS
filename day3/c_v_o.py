x=input()

def vowel_consonant(x):
    cv=0;co=0
    k=['a','e','i','o','u','A','E','I','O','U']
    for i in x:
        if i in k:
            cv+=1
        else:
            co+=1
    return [cv,co]
print(vowel_consonant(x))