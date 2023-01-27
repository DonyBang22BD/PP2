# Looping Through a String

for x in "Banana":
    print(x)

# String Length
# To get the length of a string, use function len()

a = "banana"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

# Or
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
