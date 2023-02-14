n = int(input())
cnt = {}
for word in input().split():
    if word in cnt:
        cnt[word] = cnt.get(word,0)+1
d = max(cnt.values())
l =set()
for key in cnt:
    if cnt[key] == d:
        l.add(key)
print(sorted(1)[0])