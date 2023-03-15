def multiple(lst):
    x = 1
    for i in range(1,len(lst)):
        x *= lst[i]
    return x
lst = [int(i) for i in input().split()]
print(multiple(lst))


 