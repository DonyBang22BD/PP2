cnt = {}
# creating empty dictionary
for word in input().split(): # - переводит слова в такую форму - {'one','two', 'one', 'tho','three'}
    if word in cnt:
        cnt[word] = cnt.get(word,0)+1  # здесь значение каждого ключа ровна к нулю,
        #если оно повторяется то к значению добавляется +1
        print(cnt.get(word))
    else:
        cnt[word] = 0
        print(cnt.get(word)) 
    