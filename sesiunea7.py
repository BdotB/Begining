# # Clasa copil va mosteni/va avea acces la toate proprietatile/atributele si metodele din clasa parinte.
# class Chef:
#
#     def __init__(self, experience):
#         self.experience = experience
#
#     def make_salad(self):
#         print("salad")
#
#     def make_fries(self):
#         print("fries")
#
#
# # child class - mosteneste din clasa Chef
# # se trece intre paranteze numele clasei parinte
# class JapaneseChef(Chef):
#
#     def make_sushi(self):
#         print("sushi")
#
#
# # child class - mosteneeste din clasa Chef
# # se trece intre paranteze numele clasei parinte
# class ItalianChef(Chef):
#
#     def make_pizza(self):
#         print("pizza")
#
#
# chef1 = Chef(2)
# chef1.make_salad()
# chef1.make_fries()
# print(chef1.experience)
#
# chef2 = JapaneseChef(15)
# chef2.make_sushi()
#
# chef2.make_salad()
# chef2.make_fries()
# print(chef2.experience)
#
# chef3 = ItalianChef(23)
# chef3.make_pizza()
#
# chef3.make_salad()
# chef3.make_fries()
# print(chef3.experience)

# De asemenea, clasa copil poate si sa aiba proprietati extra si sa extinda comportamentul clasei de baza (clasei parinte).

# class Animal:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def describe(self):
#         print(f"Animal {self.name} has {self.age} years old.")
#
#
# class Dog(Animal):
#
#     # Pentru a adauga proprietati noi:
#     # 1. Extindem lista de parametrii pe care
#     # metoda __init__ ii poate lua.
#     # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
#     # super(), cu parametrii pentrunecesari pentru clasa parinte.
#     def __init__(self, name, age, sound, color):
#         super().__init__(name, age)
#         self.sound = sound
#         self.color = color
#
#     # Pentru a extinde metode din clasa parinte:
#     # Facem apel la metoda din clasa parinte folosind super()
#     def describe(self):
#
#         print(f"Animal's color is {self.color}.")
#         print(f"He says: {self.sound}.")
#         super().describe()
#
# animal = Animal('bob',5)
# print(animal.name)
# print(animal.age)
#
# animal.describe()
# dog1 = Dog("lucky", 3, "ham ham", "black")
# print(dog1.name)
# print(dog1.age)
# print(dog1.sound)
# print(dog1.color)
# dog1.describe()
#
# 1.
# a. Defineste o clasa numita Persoana.
# Aceasta clasa va avea urmatoarele atribute (in constructor):
# - nume
# - varsta
#
# Implementeaza metoda descrie(), care va afisa mesajul:
# 'Persoana {nume} are {varsta} ani.'
# """
#
# """
# b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
# Aceasta clasa va lua in constructor inca doi parametri, salariu si post.
# Defineste metoda afiseaza_salariu, care returneaza atributul salariu.
# """
#
# """
# c. Creeaza un obiect de tip clasa Persoana.
# Acceseaza si afiseaza proprietatile acesteia.
# Apeleaza/invoca metoda descrie.
# """
#
# """
# d. Creeaza un obiect de tip Angajat.
# Acceseaza si afiseaza proprietatile acesteia.
# Apeleaza/invoca metodele disponibile pe aceasta.
# """
#
# """
# e. Extinde metoda descrie din clasa Angajat, astfel incat sa se afiseze
# si o propozitie care contine atributele salariu si post.
# """
'''
class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descriere(self):
        print(f"Persoana {self.nume} are {self.varsta} ani")

class Angajat(Persoana):

    def __init__(self, nume, varsta, salariu, post):
        super().__init__(nume, varsta)
        self.salariu = salariu
        self.post = post

    def afiseaza_salariu(self):
        return self.salariu()

    def desciere(self):
        super().descriere()
        print(f"Salariul este {self.salariu} pentru postul {self.post}")

persoana1 = Persoana("Vasile", 30)

persoana1.descriere()
print(persoana1.nume)
print(persoana1.varsta)

angajat1 = Angajat("george", 40 ,2000, "sofer")

angajat1.descriere()

print(angajat1.afiseaza_salariu())
print(angajat1.nume)
print(angajat1.varsta)
print(angajat1.salariu)
print(angajat1.post)
'''

# class Persoana:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     def descrie(self):
#         print(f'Persoana {self.nume} are {self.varsta} ani.')
#
# class Angajat(Persoana):
#
#     def __init__(self,nume, varsta, salariu, post):
#         super().__init__(nume,varsta)
#         self.salariu = salariu
#         self.post = post
#
#     def afiseaza_salariu(self):
#         return self.salariu
#
#     def descrie(self):
#         super().descrie()
#         print(f'Salariul este {self.salariu} pentru postul {self.post}')
#
# persoana1 = Persoana("vasile", 30)
#
# persoana1.descrie()
# print(persoana1.nume)
# print(persoana1.varsta)
#
# angajat1 = Angajat('George', 40, 2000, 'sofer')
#
# angajat1.descrie()
#
# print(angajat1.afiseaza_salariu())
# print(angajat1.nume)
# print(angajat1.varsta)
# print(angajat1.salariu)
# print(angajat1.post)

# POLIMORFISM

#  Exemplu de class methods polimorfice
# class Romania:
#     def language(self):
#         print("Romanian")
#
#
# class USA:
#     def language(self):
#         print("English")
#

#
# obj_ro = Romania()
# obj_usa = USA()
#
# obj_ro.language()
# obj_usa.language()

"""
2. 
a. Defineste o clasa Pasare care implementeaza metoda zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor pot zbura.'
"""

"""
b. Defineste o clasa Strut, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, ci o suprascriem -> OVERRIDING)
"""

"""
c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul "Ratele pot zbura."
"""

"""
d. Instantiaza cele 3 clase si apeleaza metoda zboara pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> comportament diferit.
"""
#
# class Pasare:
#     def zboara(self):
#         print("Maj pasarilor pot sa zboare")
#
# class Strut(Pasare):
#     def zboara(self):
#         print("strutii nu pot zbura")
#
# class Rata(Pasare):
#     def zboara(self):
#         print("ratele pot zbura")
#
# pasare = Pasare()
# strut = Strut()
# rata = Rata()
#
# pasare.zboara()
# strut.zboara()
# rata.zboara()

# ABSTRACTIZARE
#
# from abc import ABC, abstractmethod
#
#
# # clasa abstracta / interfata
# class Animal(ABC):
#
#     @abstractmethod
#     def sound(self):
#         pass
#
#     @abstractmethod
#     def sleep(self):
#         pass
#
#     def describe(self):
#         print("Animals are lovely.")
#
# # clasa copil care mosteneste din interfata Animal
# class Dog(Animal):
#
#     def sound(self):
#         print("Ham ham")
#
#     def sleep(self):
#         print('ZZZZ')
#
# # clasa copil care mosteneste din interfata Animal
# class Cat(Animal):
#
#     def sound(self):
#         print("Miau miau")
#
#     def sleep(self):
#         print("Prrrr")
#
#
# cat = Cat()
# cat.sound()
# cat.sleep()
# cat.describe()
#
# dog = Dog()
# dog.sound()
# dog.sleep()
# dog.describe()

"""
3. 
a. Defineste interfata Car. Aceasta va avea o metoda abstracta
numita car_model.
"""

"""
b. Defineste clasele Tesla si BMW, care implementeaza interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda car_model pe fiecare din acestea.
"""

# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def car_model(self):
#         pass
#
# class Tesla(Car):
#     def car_model(self):
#         print("Modelul Tesla este Y")
#
# class BMW(Car):
#     def car_model(self):
#         print("Modelul BMW este X5")
#
# tesla1 = Tesla()
# bmv = BMW()
# tesla1.car_model()
# bmv.car_model()


# E N C A P S U L A R E



# date PRIVATE
# class Car:
#
#     def init(self, brand):
#         self.brand = brand
#
#     def run(self):
#         print(f"Please run {self.brand}")
#
#
# car = Car("Dacia")
# # print(car.brand) # -> eroare
# car.run()

# date protected
# class Dog:
#
#     def init(self, nume, varsta):
#         self._nume = nume
#         self.varsta = varsta
#
#     def _descrie(self):
#         print(f"Cainele {self._nume} are {self.varsta} ani.")
#
# dog1 = Dog('Bob', 5)
# print(dog1._nume)
# print(dog1.varsta)
#
# dog1._descrie()
#
# class Car:
#     color = 'grey'
#
#     def get_color(self):  # folosim getter sa afisam culoarea
#         return self.color
#
#     def set_color(self, culoare_dorita): # setter
#         if culoare_dorita == 'galben':
#             print("Atentie! Culoarea aceasta nu e disponibila")
#         else:
#             self.color = culoare_dorita
#
# car1 = Car()
# # print(Car.color)
# print(car1.get_color())
#
# car1.set_color('red')
# print(car1.get_color())
#
# car1.set_color('galben')
# print(car1.get_color())

class CarPy:

    def init(self, color):
        self.c = color

    @property
    def color(self):
        return self.c

    @color.getter
    def color(self):
        print(f"Getter: Culoarea este {self.c}")
        return self.c

    @color.setter
    def color(self, culoare_noua):
        print(f"Setter: Noua culoare este {culoare_noua}")
        self.c = culoare_noua

    @color.deleter
    def color(self):
        print(f"Deleter: Am sters culoarea")
        self.__c = None


car2 = CarPy('gray')
# print(car2.color)
#
car2.color = 'red'
print(car2.color)
#
del car2.color
print(car2.color)
