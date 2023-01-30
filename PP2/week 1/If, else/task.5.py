# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Pass statement 
a = 33
b = 200

if b > a:
  pass