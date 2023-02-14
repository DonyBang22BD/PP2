def power(a,n):
    num = 1
    for i in range(abs(n)):
        num *= a
    if n >= 0:
        return num
    else: 
        return 1/num 
print( power( float(input()), int(input()) ))