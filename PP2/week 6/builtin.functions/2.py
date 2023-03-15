def counter(s):
    upper = 0
    lower = 0
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z': #s.isupper()
            upper += 1
        elif s[i]>='a' and s[i]<='z': #s.islower()
            lower += 1
    print(upper)
    print(lower)

s = input()
counter(s)
