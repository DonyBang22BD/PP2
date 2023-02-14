# class Circle():
#     Pi = 3.14 #attribute
#     circle_count = 0
#     def __init__(self,radius): #method
#         self.radius = radius
#         Circle.circle_count += 1
#     def get_perimetr(self):
#         return self.radius * 2 * Circle.Pi
#     def get_area(self):
#         return Circle.Pi * self.radius ** 2
#     def get_info(self):
#         print(f"Perimetr of circle: {self.get_perimetr()}, Area of circle: {self.get_area()} ")
    
# c1 = Circle(int(input())) # object
# c1.get_info()

# c2 = Circle(int(input())) # object
# c2.get_info()

# print('Quantity of created circles:',Circle.circle_count)

#Пример создание класса человек

# class Person():
#     count_of_created_persons = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print("Person created \n")
#         # Person.count_of_created_persons += 1
#         # print(f"At the moment, quantity of people:" ,Person.count_of_created_persons,' \n' )
    
#     def say_hello(self):
#         print(f"{self.name} says hello to GOAT !!! \n")

# p1 = Person("Adward",28)
# p1.say_hello()

# class Student(Person): # наследование от класса Person
#     def __init__(self,name,age,gpa):
#         super().__init__(name,age)
#         self.gpa = gpa
#         print(f"Student created  \n")
#     def study(self):
#         print(f'{self.name} studies \n')
#     def say_hello(self): # переопределение метода класса Person
#         print(f"Student with name: {self.name} says hello \n")

# class Teacher(Person): # наследование от класса Person
#     def __init__(self,name,age,salary):
#         super().__init__(name,age)
#         self.salary = salary
#         print(f"Teacher created  \n")
#     def teach(self):
#         print(f"{self.name} teaches students \n")
# s1 = Student('Mike',22,4.0)
# t1 = Teacher('Janna',55,500000)

# s1.say_hello()
# t1.say_hello()

# s1.study()
# t1.teach()

# def introduce(person):
#     print("Now, person will say hello \n")
#     person.say_hello()
# people_list = [Student('Mike',22,3.9),Teacher('Janna',55,500000),Student("Nurdaulet",18,3.0)]
# for person in people_list:
#     introduce(person)

# Еще один пример

class Animal():
    def __init__(self,name):
        self.name = name
        print(f"Animal created \n")    
    def eat(self):
        print(f"{self.name} is eating \n")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"Dog named {self.name} is barking \n")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def meow(self):
        print(f"{self.name} says Meow \n")
class Frog(Animal):
    def _init_(self,name):
        super().__init__(name)
    def eat(self):
        print(f"Frog with name {self.name} is eating  \n")

# d = Dog("Aktos","Bulldog")
# c = Cat("Murcka")
# f = Frog("Lyagushka")
# d.bark()
# c.meow()
# f.eat()

# Difference between "lambda" and simple function "def"
# def rectangle_perimetr(a,b):
#     return a * b
# print(rectangle_perimetr(int(input()),int(input())))

# #and
# print((lambda a,b: a * b)(int(input()),int(input())))

# def maxi(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(maxi(25,17),' \n')

# #and
# print((lambda a,b: a if a > b else b)(25,17))

def func(n):
    return lambda a : a*n
my_doubler = func(2)
print(my_doubler(11))
