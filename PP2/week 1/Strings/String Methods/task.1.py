#1 The method returns a string where the first character is upper case, and the rest is lower case.capitalize()
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#2 This method is similar to the lower() method, but the casefold() method is stronger, more aggressive
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

#3 Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"

x = txt.center(20)

print(x)

#4 txt = "banana"

x = txt.center(20, "O")

print(x)

#5 The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)



