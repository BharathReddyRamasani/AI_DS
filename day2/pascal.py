# # # # # x=int(input("enter x:"))
# # # # # def pascal(n):
# # # # #     for i in range(n):
# # # # #         for j in range(n-i-1):
# # # # #             print(" ",end=" ")
        
# # # # def magic(n):
# # # #     s=0
# # # #     for i in range(1,n):
# # # #         if n%i==0:
# # # #             s=s+i
# # # #     return s==n
# # # # print(magic(28))

# # # def f(x):
# # #     for i in range(x,0,-1):
# # #         if x%i==0:
# # #             return i
# # #     return 1
# # # print(f(7)+f(9))

# # def magic(n):
# #     while n>9:
# #         s=0
# #         while n>0:
# #             s=s+n%10
# #             n=n//10
# #         n=s
# #     return n==1
# # print(magic(19))

# def do_it(a,b):
#     c=0
#     for i in range(a,b):
#         if i%3==0 and i%5!=0:
#             c=c+1
#     return c
# print(do_it(1,16))
def calc(n):
    s=1
    for i in range(1,n+1):
        if i%2!=0:
            s=s*i
    return s
print(calc(5))