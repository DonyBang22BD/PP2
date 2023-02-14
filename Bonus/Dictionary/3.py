n = int(input())
my_dict={}
for i in range(n):
    candidate,votes = input().split()
    my_dict[candidate] = my_dict.get(candidate,0)+ int(votes)

for h,j in sorted(my_dict.items()):
    print(h,j)