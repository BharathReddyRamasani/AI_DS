# def even_odd(x):
#     return "even"if x%2==0 else "odd"
# print(even_odd(3))

# def pos_neg(x):
#     return "pos" if x>0 else "neg"
# print(pos_neg(-3))

# def div5_11(x):
#     return "yes" if x%5==0 and x%11==0 else"not"
# print(div5_11(57))

# def leap_year(x):
#     if x%400==0 or (x%100!=0 and x%4==0):
#         return "leap"
#     else:
#         return "not"
# print(leap_year(2025))

# def alpha(x):
#     return "alpha" if x.isalpha()==True else "not"
# print(alpha("g"))

# def vowel_consonant(x):
#     i=['a','e','i','o','u','A','E','I','O','U']
#     return "vowel" if x in i else "consonant"  # return "vowel" if x in 'aeiouAEIOU' else "consonant"
# print(vowel_consonant("G"))

def big(a,b,c):
    if a>b and a>c:return a
    elif b>a and b>c:return b
    else:return c
print(big(3,5,1))



