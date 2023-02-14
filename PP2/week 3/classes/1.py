class String():
    def __init__(self):
        self.string = ""
    def getstring(self):
        self.string = input("Entire words or phrases: ")
    def printstring(self):
        print(self.string.upper())
s1 = String()
s1.getstring()
s1.printstring()
 

