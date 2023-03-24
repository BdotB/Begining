# a. USOR (RECOMANDAT)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# b. OBLIGATORIU: USOR SPRE MEDIU

# IMPORTANT! -> Pentru TOATE EXERCITIILE, apelati functia de cel putin 2 ori cu valori
# diferite pentru a testa. Daca functia are return, printati raspunsul!

# 1. Scrie o functie care sa calculeze si sa returneze suma a 2 numere
def sum_numbers(num1, num2):
    sum = num1 + num2
    return sum
result = sum_numbers(3, 5)
print(result)
# 2. Scrie o functie care sa returneze True daca un numar este par, False daca este impar
def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
numar = int(input("Introduceti un numar: "))
if este_par(numar):
    print(numar, "este par")
else:
    print(numar, "este impar")
# 3. Scrie o functie care sa returneze numarul total de caractere din numele tau complet
# (nume, prenume, nume_mijlociu)
def numar_caractere(nume:str, prenume:str, nume_mijlociu:str) -> int:
    full_name = nume + ' ' + prenume + ' ' + nume_mijlociu
    num_characters = len(full_name)
    return num_characters
print(numar_caractere("Bogdan", "Mihai", "Dorel"))

# 4. Scrie o functie care returneaza aria dreptunghiului
def aria_dreptunghiului(lungime: float, latime: float) -> float:
    aria = lungime * latime
    return aria
aria = aria_dreptunghiului(5, 6)
print(aria)
# 5. Scrie o functie care returneaza aria cercului
import math
def aria_cerc(raza: float) -> float:
    aria2 = math.pi * raza * raza
    return aria2
aria2 = aria_cerc(5)
print(aria2)
# 6. Scrie o functie care returneaza True daca un caracter x se gaseste intr-un string dat, False daca nu.
def gaseste_caracterul(x: str, sir: str) -> bool:
    if x in sir:
        return True
    else:
        return False
rezultat = gaseste_caracterul('a', 'Ana are mere')
print(rezultat)
# 7. Scrie o functie fara return care primeste ca parametru un string si printeaza pe ecran:
# - Nr. caractere lower case este x
# - Nr. caractere upper case este y
def count_upper_lower(string):
    num_lower = 0
    num_upper = 0
    for char in string:
        if char.islower():
            num_lower += 1
        elif char.isupper():
            num_upper += 1
    print("Nr. caractere lower case este", num_lower)
    print("Nr. caractere upper case este", num_upper)
count_upper_lower("MaMa ARE mere")

# 8. Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele pozitive.
def positive_numbers(numbers):
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive
print(positive_numbers([-5, 3, 5, -4, 132]))

# 9. Scrie o functie care nu returneaza nimic. Primeste 2 numere si printeaza:
# - primul numar x este mai mare decat al doilea y
# - al doilea numar y este mai mare decat primul numar x
# - Numerele sunt egale.
def compare_numbers(x, y):
    if x > y:
        print(f"{x} este mai mare decat {y}")
    elif x < y:
        print(f"{y} este mai mare decat {x}")
    else:
        print("Numerele sunt egale.")
compare_numbers(2,3)
compare_numbers(3,4)
compare_numbers(5,4)
# 10. Scrie o functie care primeste un numar si un set de numere.
# Printeaza 'am adaugat numarul nou in set' + returneaza True
# sau printeaza 'Nu am adaugat numarul nou in set. Acesta exista deja' + returneaza False
def add_number_to_set(num, num_set):
    if num in num_set:
        print("Nu am adaugat numarul nou in set. Acesta exista deja")
        return False
    else:
        num_set.add(num)
        print("Am adaugat numarul nou in set")
        return True
num_set = {1, 2, 3}
result = add_number_to_set(4, num_set)
result = add_number_to_set(3, num_set)
# c. OPTIONALE (STUDIU DE ECHIPA) -> may need google

# 1. Scrie o functie care primeste o luna din an si returneaza cate zile are acea luna.
def days_in_month(month):
    if month in ("ianuarie", "martie", "mai", "iulie", "august", "octombrie", "decembrie"):
        return 31
    elif month in ("aprilie", "iunie", "septembrie", "noiembrie"):
        return 30
    elif month == "februarie":
        return 28
    else:
        return -1
print(days_in_month("ianuarie"))
print(days_in_month("aprilie"))
print(days_in_month("februarie"))
print(days_in_month("sdasd"))
# 2. Scrie o functie calculator care sa returneze 4 valori: suma, diferenta, inmultirea a 2 numere.
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
def calculator(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    if num2 != 0:
        quot = num1 / num2
    else:
        quot = None
    return sum, diff, prod, quot
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
# 3. Scrie o functie care primeste o lista cu cifre (adica doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un dictionar care ne spune de cate ori apare fiecare cifra
# =>
# dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def count_digits(lst):
    result = {}
    for i in range(10):
        result[i] = lst.count(i)
    return result
lst = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(count_digits(lst))


# 4. Scrie o functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
def max_of_three(a, b, c):
    return max(a, b, c)
max_of_three(5, 10, 3)
max_of_three(0, -5, 10)


# 5. Scrie o functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3, suma va fi 6 (0 + 1 + 2 + 3)
def suma_pana_la(numar):
    suma = 0
    for i in range(numar + 1):
        suma += i
    return suma
print(suma_pana_la(4))
# 6. Scrie o functie care primeste 2 liste de numere (numerele pot fi dublate).
# Returnati valorile comune
def valori_comune(lista1, lista2):
    comunee = []
    for numar in lista1:
        if numar in lista2 and numar not in comunee:
            comunee.append(numar)
    return comunee

print(valori_comune([1, 2, 3, 4, 5, 6], [2, 3, 4, 6, 7]))


# exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

# 7. Scrie o functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10 %, pretul va fi 90.
# Tratati cazurile in care reducerea este invalida. De exemplu o reducere de 110 % e invalida.
def aplicare_reducere_pret(pret_initial, reducere_procent):
    if reducere_procent < 0 or reducere_procent > 100:
        print("Eroare: reducerea de procent trebuie sa fie intre 0 si 100.")
        return None
    else:
        pret_final = pret_initial * (100 - reducere_procent) / 100
        return pret_final
pret_initial = int(input("Introduceti pretul intiial: "))
reducere_procent = int(input("introduceti procentu de reducere, intre 0 si 100 preferabil :"))
pret_final = aplicare_reducere_pret(pret_initial, reducere_procent)
print(f"pretul final este: ", pret_final)

# 8. Scrie o functie care sa afiseze data si ora curenta din RO.
# (bonus: afisati si data si ora curenta din China)
import datetime
import pytz
def get_current_time():
    tz_ro = pytz.timezone('Europe/Bucharest')
    tz_china = pytz.timezone('Asia/Shanghai')
    current_time_ro = datetime.datetime.now(tz_ro)
    current_time_china = datetime.datetime.now(tz_china)
    print("Data si ora curenta in Romania: ", current_time_ro.strftime("%d-%m-%Y %H:%M:%S"))
    print("Data si ora curenta in China: ", current_time_china.strftime("%d-%m-%Y %H:%M:%S"))
get_current_time()

# 9. Scrie o functie care sa afiseze cate zile mai sunt pana la ziua ta/ sau pana la craciun daca nu vrei sa ne zici
# cand e ziua ta :D.

def days_until_date(date):
    today = datetime.date.today()
    remaining_days = (date - today).days
    if remaining_days > 0:
        print("Mai sunt", remaining_days, "zile pana la data de", date.strftime("%d-%m-%Y"))
    elif remaining_days == 0:
        print("Astazi este", date.strftime("%d-%m-%Y"))
    else:
        print("Data", date.strftime("%d-%m-%Y"), "a trecut deja")
birthday = datetime.date(2023, 8, 14)
days_until_date(birthday)
today = datetime.date.today()
year = today.year
christmas = datetime.date(year, 12, 25)
if today > christmas:
    year += 1
    christmas = datetime.date(year, 12, 25)
days_until_date(christmas)