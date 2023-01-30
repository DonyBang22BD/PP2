#1
fruits = ["banana","grapes","aplle"]
for x in fruits:
    print(x)
    if x == "apple":
        break

#2 break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#3 continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
        continue
   print(x)