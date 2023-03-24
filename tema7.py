"""
1.Git setup

OBLIGATORIU!
Creati-va cont de github si incarcati intr-un repo nou tot ce am facut pana acum la ore
Curs git/github
https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
"""

"""
!! 2. Faceti urmatoarele exercitii dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
"""
"""
1. ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
"""

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colțuri")

"""
2. INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura


    @latura.setter
    def set_latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def del_latura(self):
        del self.__latura

    def aria(self):
        return self.__latura ** 2

"""
3. Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
"""

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def set_raza(self):
        self.__raza = raza

    @raza.getter
    def get_raza(self):
        return self.__raza

    @raza.deleter
    def del_raza(self):
        del self.__raza

    def aria(self):
        return FormaGeometrica.PI * self.__raza ** 2


"""
4. POLYMORPHISM 
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
un

Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
"""

# Cream un obiect de tip Patrat cu latura de 5
patrat = Patrat(5)

# afisam latura patratului
print("Latura patratului:", patrat.latura)

#afisam aria
print("aria este", patrat.aria())

# setam noua valoare pentru latura

patrat = Patrat(7)

# afisam noua valoare a laturii patratului
print("Latura patratului actualizata:", patrat.latura)

# aria patratului
print("Aria patratului:", patrat.aria())

# descrierea
patrat.descrie()


# cream un obiect de tip Cerc cu raza de 3
cerc = Cerc(3)

# Afisam raza cercului
print("Raza cercului:", cerc.raza)

#afisam aria
print("aria cercului este: ", cerc.aria())
# Setam o nouă valoare pentru raza cercului

cerc = Cerc(5)

# Afisam raza cercului actualizata
print("Raza cercului actualizata", cerc.raza)

# aria cercului
print("aria cercului:", cerc.aria())

#descrierea
cerc.descrie()
"""
5. Actualizati proiectul pe github facand un push la noul cod
In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public

Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4
"""