# class Car:
#     # fields (atributtes)
#     make = 'Dacia'
#     model = None
#     year = 2022
#     color = None
#
#     # methods
#     def accelerate(self, viteza):
#         print(self.year)
#         #print(year) #nu functioneaza...trebuie mereu apelat cu self
#         print(f"Vrum vrrrum {viteza}")
#
#     def stop(self):
#         self.accelerate(500)
#         print('STOP')
#
# car1 = Car() # initializam obiecte de tip Car
# car2 = Car() # car2 este instanta a clasei Car
# print(car1.make) # dupa . avem acces la fields
# print(car2.make)
#
# print(car1.model)
#
# car1.model = 'Duster' # putem suprascrie valori
# print(car1.model)
# print(car2.model)
# car2.model = 'Logan'
# print(car2.model)
#
# car1.accelerate(20) # dupa . avem acces la metode
# car2.accelerate(80)
# car1.stop()
# car2.stop()

# class Car:
#     # fields (attributes)
#     make = 'Dacia'
#     year = 2022
#
#     def init(self, model, color):
#         self.model = model
#         self.color = color
#
# car1 = Car('Duster', 'white')
# car2 = Car('Logan', 'blue')
#
# print(car1.make)
# print(car1.model)
# print(car1.color)

# class Complex:
#
#     def init(self, real, imag):
#         self.r = real
#         self.i = imag
#
# z = Complex(3.0, -4.5)
#
# print(type(z))
#
# print(z.r)
# print(z.i)

# class Car:
#     make: 'Dacia'
#     year: 2022
# 1.
# a. Defineste o clasa noua Dog.
# b. Obiectele de tip Dog vor avea obligatoriu 2 atribute:
# name si age.
# c. Creeaza doua obiecte de tip clasa Dog, acceseaza atributele
# si afiseaza-le.
# d. Schimba atributul nume pentru unul din obiecte
# si afiseaza-l din nou.
# e. Creaza o metoda description, care returneaza
# mesajul '{nume} is {age} years old.
# f. Folosind unul din obiectele instantiate la exercitiul
# apeleaza metoda description, salveaza rezultatul
# intr-o variabila si afiseaza variabila.
# g. Clasa Dog este caracterizata si de atributul rasa.
# Adauga acest atribut ca si un atribut al clasei (nu al obiectului)
# h. Adauga o noua metoda in clasa Dog, numita speak,
# care ia un parametru numit sound.
# Metoda trebuie sa returneze mesajul "<name> says <sound>."
# g. Apeleaza metoda speak pe unul din obiecte si afiseaza
# rezultatul.

class Dog:
    breed = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}."

dog1 = Dog('Labrador', 3)
print(dog1.name)
print(dog1.age)
dog2 = Dog('Shiba', 5)
print(dog2.name, dog2.age)
dog1.name = 'Buddy'
print(dog1.name)
print(dog1.description())
print(dog1.speak("Bark"))