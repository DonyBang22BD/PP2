# n = int(input())
# dictionary = {}
# for i in range(n):
#     first,second = input().split()
#     dictionary[first] = second
#     dictionary[second] = first
# print(dictionary[input()])
 #2
n = int(input())
data = dict(input().split() for i in range(n))
word = input()
if word in data.keys():
    print(data[word])
else:
    for i,j in data.items():
        if j == word:
            print(i)
            break