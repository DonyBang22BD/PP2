def is_polindrom(s):
    if s[::-1]==s:
        return 'Polindrome'
    else:
        return 'Not polindrome'
s = input()
print(is_polindrom(s))