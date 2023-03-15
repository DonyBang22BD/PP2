#1
"""

import os

path = "C:\Users\diase\OneDrive\Рабочий стол\Python\PP2"

print("Directories:")

for item in os.listdir(path):
    if os.path.isdir(os.path.join(path,item)):
        print(item)

print("\nFiles:")

for item in os.listdir(path):
    if os.path.isfile(os.path,item):
        print(item)

print('\nAll directories and files:')
for item in os.listdir(path):
    print(item)"""

#2
'''
import os
print('Exist:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.F_OK))
print('Readable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.R_OK))
print('Writable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.W_OK))
print('Executable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.X_OK))
'''



#3
'''
import os
phonk="C:\\Users\\Биболат\\Desktop\\PP2\\week 6"
print(os.path.exists(phonk))
print(os.path.basename(phonk))
print(os.path.dirname(phonk))
'''


#4
'''
f=open("C:\\Users\\Биболат\\Desktop\\PP2\\demofile2.txt","r")
lines=len(f.readlines())
print(lines)
'''


#5
'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)
content = open('abc.txt')
print(content.read())
'''




#6
'''
for i in range(65,91):
    file=open(chr(i)+".txt","w")
'''


#7
'''
with open("first.txt",'r') as firstfile,open("second.txt",'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
'''



#8
'''
import os
path="C:\\Users\\Биболат\\Desktop\\PP2\\week 6"
if os.path.exists(path):
    os.remove(path)
else:
    print('File does not exist')
'''