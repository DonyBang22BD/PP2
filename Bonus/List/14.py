a = [ int(i) for i in input().split()]
a.sort()
cnt = 0
for i in range(len(a)):
    for j in range(i): 
        if a[i] == a[j]:
            cnt += 1
print(cnt)          
   