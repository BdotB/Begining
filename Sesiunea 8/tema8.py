"""
EXERCITII BONUS - OOP

Aceste exercitii sunt OPTIONALE!

"""

"""
1. 
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).

b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""

class User:


    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None
        self.aranjare = []

    @property
    def password(self):
        if self.__password:
            return '*' * len(self.__password)
        else:
            return "Parola nu a fost setata"

    @password.setter
    def password(self, value):
        if len(value) < 10:
            self.aranjare.append("Parola trebuie sa aiba minim 10 caractere.")
        elif not any(c.isupper() for c in value):
            self.aranjare.append("Parola trebuie sa contina cel putin o litera mare.")
        else:
            self.__password = value
    def login(self):
        if self.username and self.email and self.__password:
            print("Conectat")
        else:
            self.aranjare.append("Lipsesc credentiale de conectare. Nu va putem conecta")

    def print_aranjare(self):
        for aranjaree in self.aranjare:
            print(aranjaree)


user1 = User("Dorel", "Dorel@yahoo.com")
user2 = User("Gigel", "Gigel@gmail.com")
user3 = User("Ion", "Ion@yahoo.com")

user1.password = "Password123"
user2.password = "password2"
user3.password = "password21341"

print("User1:")
print("Username:", user1.username)
print("Email:", user1.email)
print("Password:", user1.password)
user1.login()
user1.print_aranjare()
print("User2:")
print("Username:", user2.username)
print("Email:", user2.email)
print("Password:", user2.password)
user2.login()
user2.print_aranjare()
print("User3:")
print("Username:", user3.username)
print("Email:", user3.email)
print("Password:", user3.password)
user3.login()
user3.print_aranjare()



"""
2.
a. Defineste clasa abstracta Person.
Metode abstracte: wake_up, sleep, eat.
Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

b. Defineste clasa Student.
Clasa Student implementeaza clasa abstracta Person.
Atribute in constructor: name, university, grade.
Metode describe -> afiseaza SI mesajul:
Studentul x, studiaza la universitatea y si are nota generala z.

c. Defineste clasa Employee.
Clasa Employee implementeaza cls abstracta Person.
Atribute in constructor: name, experience, salary.
Salary este un atribut privat!
Metoda describe -> afiseaza SI mesajul:
Angajatul x lucreaza de y ani.

d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.
"""

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def wake_up(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def describe(self):
        print("O persoana se trezeste, mananca si doarme.")


class Student(Person):
    def __init__(self, name, university, grade):
        self.name = name
        self.university = university
        self.grade = grade

    def wake_up(self):
        print(f"Studentul {self.name} se trezeste la ora 7 dimineata.")

    def sleep(self):
        print(f"Studentul {self.name} se culca la ora 23 noaptea.")

    def eat(self):
        print(f"Studentul {self.name} mananca 3 mese pe zi.")

    def describe(self):
        super().describe()
        print(f"Studentul {self.name}, studiaza la universitatea {self.university} si are nota generala {self.grade}")


class Employee(Person):

    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary


    def wake_up(self):
        print(f"Angajatul {self.name} se trezeste la ora 8 dimineata")

    def sleep(self):
        print(f"Angajatul {self.name} se culca la ora 00:00 noaptea")

    def eat(self):
        print(f"Angajatul {self.name} mananca 3 mese pe zi")

    def describe(self):
        super().describe()
        print(f"Angajatul {self.name}, lucreaza de {self.experience} ani si are un salariu de {self.__salary}")




s1 = Student("Bogdan", "UPB", 10)
s1.describe()
s1.wake_up()
s1.eat()
s1.sleep()

e1 = Employee("Maria", 5, 4000)
e1.describe()
e1.wake_up()
e1.eat()
e1.sleep()

e1.salary = 4500
e1.describe()