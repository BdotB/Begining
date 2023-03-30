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

    @property
    def password(self):
        if self.__password:
            return '*' * len(self.__password)
        else:
            return "Parola nu a fost setata"

    @password.setter
    def password(self, value):
        if len(value) < 10:
            print("Parola trebuie sa aiba minim 10 caractere.")
        elif not any(c.isupper() for c in value):
            print("Parola trebuie sa contina cel putin o litera mare.")
        else:
            self.__password = value
    def login(self):
        if self.username and self.email and self.__password:
            print("Conectat")
        else:
            print("Lipsesc credentiale de conectare. Nu va putem conecta")

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
print("User2:")
print("Username:", user2.username)
print("Email:", user2.email)
print("Password:", user2.password)
user2.login()
print("User3:")
print("Username:", user3.username)
print("Email:", user3.email)
print("Password:", user3.password)
user3.login()



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