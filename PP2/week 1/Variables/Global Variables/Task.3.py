x = "awesome"
def function():
    global x
    x = "fantastic"
function()
print("Python is " + x)
# So, in this case we can reassign x to global in the function using function "global"
