s = input()
a = [int(s) for s in s.split() ]
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        print(a[i],end=' ')