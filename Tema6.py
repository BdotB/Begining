
# A. RECOMANDAT
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva.

# B. OBLIGATORIU (MEDIU)

# ATENTIE!! Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati metodele clasei.

# 1. Clasa Cerc
# atribute: raza, culoare
# constructor pentru ambele atribute

# metode:
# descrie_cerc() -> va PRINTA culoarea si raza
# aria() -> va returna aria
# diametru()
# circumferinta()

import math

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} și culoarea {self.culoare}.")

    def aria(self):
        return math.pi * self.raza ** 2

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * math.pi * self.raza
c1 = Cerc(3, "rosu")
c2 = Cerc(5, "albastru")

c1.descrie_cerc()
print("Aria cercului este:", c1.aria())
print("Diametrul cercului este:", c1.diametru())
print("Circumferința cercului este:", c1.circumferinta())

c2.descrie_cerc()
print("Aria cercului este:", c2.aria())
print("Diametrul cercului este:", c2.diametru())
print("Circumferința cercului este:", c2.circumferinta())

# 2. Clasa Dreptunghi

# atribute: lungime, latime, culoare
# constructor pentru toate atributele

# metode:
# descrie()
# arie()
# perimetru()
# schimba_culoare(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        print(f"Dreptunghiun are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}")

    def aria_dreptunghi(self):
        return self.lungime * self.latime

    def perimetru_dreptunghi(self):
        return self.lungime + self.lungime + self.latime + self.latime

    def schimb_culoare_dreptunghi(self):
        self.culoare = "red"

d1 = Dreptunghi(4, 5, "verde")
d2 = Dreptunghi(5, 6, "maro")
d1.descriere_dreptunghi()
d1.schimb_culoare_dreptunghi()
d1.descriere_dreptunghi()
print("Aria este: ", d1.aria_dreptunghi(), "Perimetrul este: ", d1.perimetru_dreptunghi())
d2.descriere_dreptunghi()
d2.schimb_culoare_dreptunghi()
d2.descriere_dreptunghi()
print("Ara este: ", d2.aria_dreptunghi(), "Perimetrul este: ", d2.perimetru_dreptunghi())

# 3. Clasa Angajat

# atribute: nume, prenume, salariu

# Connstructor pentru toate atributele

# Metodele:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu} lei pe luna")

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu += self.salariu * procent / 100
        print(f"Salariul a fost marit cu {procent}% si a devenit {self.salariu} lei pe luna")

a1 = Angajat("Popescu", "Ion", 3000)
a2 = Angajat("Ionescu", "Maria", 4000)

a1.descrie()
print("Numele complet al angajatului este:", a1.nume_complet())
print("Salariul lunar al angajatului este:", a1.salariu_lunar())
print("Salariul anual al angajatului este:", a1.salariu_anual())
a1.marire_salariu(20)
a1.descrie()

a2.descrie()
print("Numele complet al angajatului este:", a2.nume_complet())
print("Salariul lunar al angajatului este:", a2.salariu_lunar())
print("Salariul anual al angajatului este:", a2.salariu_anual())
a2.marire_salariu(10)
a2.descrie()


# 4. Clasa Cont

# atribute: iban, titular_cont, sold

# constructor pentru toate

# metode:
# afisare_sold() -> Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare cont(suma)

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}"

    def debitare_cont(self, suma):
        return self.sold - suma

    def creditare_cont(self, suma2):
        return self.sold + suma2

x = Cont("BCR123" , "Ion Daniel", 45000)
x.afisare_sold()
print(f"Titularul {x.titular_cont} are in contul {x.iban} soldul {x.sold}")
print(f"Soldul din cont dupa debitarea este {x.debitare_cont(400)}")
print(f"Soldul din cont dupa creditare este {x.creditare_cont(5000)}")
# BONUS (daca aveti timp soi doriti sa lucrati suplimentar)

# 5. Clasa Factura
# atribute: seria (va fi constanta, nu trebuie constructir, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc

# Constructor: toate atributele, fara serie

# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti

# Exemplu:
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | Cantitate | Pret Bucata | Total
# Telefon|     7     |    700      | 49000

class Factura():
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitate(self, cantitate):
            self.cantitate = cantitate

Factura(None, None, 400, None)
seria = "VX450392"
cant = Factura(None, None, 400, None)

print(f"Noua cantitate este {cant.schimba_cantitate(300)}")



# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

# 6. Clasa Masina
# atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set),
# inmatriculata (bool)

# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# culori_disponibile = alegeti 5-7 culori
# marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# inmatriculata = False

# constructor: model, viteza_maxima

# Metode:
# descrie() (se vor printa toate atributele, in afara de culori disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vospeste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare este in culori_disponibile,
# altfel afisati un mesaj.
# accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa - mesaj de eroare,
# daca viteza e mai mare decat viteza maxima - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0

# 7. Clas ToDoList

# Atribute: to_do (dict, chiea e numele task-ului, valoarea e descrierea)
# La inceput nu avem task-uri, dict e gol si nu avem nevoie de constructor.

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - afiseaza doar cheile
# afiseaza_detalii_suplimentare(nume_task) = in functie de numele task-ului, printam
# detalii suplimentare. Daca task-ul nu e in to_do list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# Daca raspunde da - ii cerem detalii task si salvam nume + detalii in dict