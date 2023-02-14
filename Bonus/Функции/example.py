# inPut = int(input())
# number = 1
# for i in range(1,inPut+1):
#     number *= i
# print(number) 

# def factorial(n):
#     number = 1
#     for i in range(1,n+1):
#         number *= i
#     return number
# print(factorial(int(input())))

# def max(a,b,c):
#     if c< a > b:
#         return a
#     elif a< b >c:
#         return b
#     elif a < c >b:
#         return c
    
# print(max(int(input()), int(input()),int(input())))

# def factorial(n):
#     num = 1
#     for i in range(1,n+1):
#         num *= i
#     return num

# for i in range(1,int(input())+1):
#     print(i,'!= ',factorial(i),sep='')

# def short_story():
#     print("У попа была собака, он ее любил.")
#     print("Она съела кусок мяса, он ее убил,")
#     print("В землю закопал и надпись написал:")
#     short_story()
# print(short_story())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input())))