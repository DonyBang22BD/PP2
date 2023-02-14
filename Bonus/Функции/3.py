def capitaliz(s):
    a = s.split()
    for i in a:
        print( chr(ord(i[0])-32) + i[1:],end=' ')
capitaliz(input())

