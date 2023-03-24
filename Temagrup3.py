# 1. Explica intr-un comentariu ce este o variabila de tip string.
# un array de caractere
# 2. Defineste o variabila string, numita descriere si afiseaz-o.
descriere = "Ion"
print(descriere)
# 3. Defineste 3 variabile: oras, strada si nr.
oras = "Bucuresti"
strada  = "Fat frumos"
nr = 7
# a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
print("Orasul " + oras + " strada " + strada +  " numarul " + str(nr))
# b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
print(f"Orasul {oras} pe strada {strada} cu nuamrul {nr}")
# 4. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
# a. Afiseaza primul element din string.
nume_complet = 'Pop Maria Ioana'
print(nume_complet[0])
# b. Afiseaza al doilea prenume.
prenume = nume_complet.split()
prenume2 = prenume[1]
print(prenume2)
# c. Afiseaza de cate ori apare litera 'a' in nume_complet.
numarare = nume_complet.count("a")
print(numarare)
# d. Inverseaza string-ul si afiseaza rezultatul.
inversare = nume_complet[::-1]
print(inversare)
# e. Inlocuieste al doilea prenume cu 'Elena'.
inlocuire = nume_complet.split()
inlocuire[1] = "Elena"
nume_complet2 = ' '.join(inlocuire)
print(nume_complet2)
# f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv).
print(nume_complet[5:10])
# g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
print(nume_complet[:9])
# 5. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
culoare = input("Introduceti culoarea preferata: ")
# a. Determina lungimea inputului citit de la tastatura.
c = len(culoare)
# b. Determina tipul inputului citit de la tastatura.
d = print(type(culoare))
# c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
culoare = culoare.upper()
print(culoare)
# d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
culoare = culoare.capitalize()
print(culoare)
# Afiseaza rezultatul.
# 6. Se da variabila my_var = '1234'. Verifica daca my_var este compus doar din numere.
my_var = '1234'
if my_var.isdigit():
    print("Variabila my_var este compusă doar din numere")
else:
    print("Variabila my_var nu este compusă doar din numere")
# 7. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
anotimp = 'primavara'
if anotimp[-4:] == 'vara':
    print("Variabila anotimp se termină cu 'vara'.")
else:
    print("Variabila anotimp nu se termină cu 'vara'.")
# 8. Citeste de la tastatura numarul de zile ramase pana la vacanta.
# Verifica, folosind assert, daca numarul de zile este mai mare de 7 zile.
numar_zile = int(input("introduceti numarul de zile ramase pana la vacanta: "))
assert numar_zile > 7, "Numarul de zile ramase pana la vacanta trebuie sa fie mai mare decat 7"
print("Numarul de zile ramas pana la vacanta este mai mare decat 7")
# 9. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
cos_cumparaturi = float(input("Introduceti pretul cosului de cumparaturi: "))
cos_cumparaturi_discount = cos_cumparaturi - cos_cumparaturi * 25/100
print(cos_cumparaturi_discount)
# 10. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
# Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'
zile_sapt_list = zile_sapt.split(',')
print(zile_sapt_list)
# 11. Se citeste de la tastatura 2 string-uri. Verifica daca al doilea string se gaseste in primul.
string1 = input("Introduceti primul string: ")
string2 = input("Introduceti al 2-lea string: ")
if string2 in string1:
    print(f"sirul '{string2}' se gaseste in sirul '{string1}' ")
else:
    print(f"sirul '{string2}' nu se gaseste in sirul '{string1}' ")
# 12. Scrie un program care solicita utilizatorului sa introduca varsta sa
# și returneaza un mesaj personalizat, in funcție de varsta introdusa.
# Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
# mesajul "Esti major si poti vota".
varsta = int(input("Introduceti varsta: "))
if varsta < 18:
    print("Esti minor si nu poti vota inca")
else:
    print("Esti major si poti vota")
# In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
# 13. Scrie un program care primeste un pret de la tastatura si afiseaza
# un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
pret = float(input("Introduceti pretul de la tastatura: "))
if pret > 100:
    print("Pretul este mai mare decat 100")
elif pret < 100:
    print("Pretul este mai mic decat 100")
else:
    print("Pretul este fix 100")
# 14. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
# daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
nr1 = float(input("Introduceti primul numar: "))
nr2 = float(input("Introduceti cel de-al 2-lea numar: "))
nrprod=nr1*nr2
nrsum=nr1 + nr2
if nr1*nr2 <= 1000:
    print(nrprod)
else:
    print(nrsum)
# 15. Se dau doua liste:
# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]
# Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
# In functie de rezultat, afiseaza un mesaj.
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
if lista_1[0] == lista_1[-1] and lista_2[0] == lista_2[-1]:
    print("Primul element este acelasi cu ultimul")
else:
    print("Primul si ultimul element nu sunt la fel")
# 16. Scrie un program care afiseaza de cate ori apare litera 'e' in
# stringul str_1 = 'Emma is a sofware developer.'
str_1 = 'Emma is a sofware developer.'
count = 0
for char in str_1:
    if char == 'e':
        count += 1
print("Numarul de aparitii ale literei 'e' in stringul dat este:", count)
# 17. Scrie un program in care citesti de la tastatura doua nr intregi,
# numite base si exponent.
# Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
# Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
# ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
# hint: exploreaza functia abs() si vezi cum o poti folosi
base = int(input("Introduceti valoarea bazei: "))
exponent = int(input("Introduceti valoarea exponentului: "))
power = base ** abs(exponent)
print(f"{base} la puterea {exponent} este {power}")
# 18. Scrie un program in care se citeste de la tastatura un string.
# Daca string-ul are numar impar de caractere, afiseaza un string care
# contine primul caracter, caracterul din mijloc al string-ului
# citit de la tastatura si ultimul caracter.
# Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
# si ultimul caracter  al string-ului citit de la tastatura.
string = input("Introduceti un string: ")
if len(string) % 2 == 0:
   new_string = string[0] + string[-1]
else:
    middle_index = len(string) // 2
    new_string = string[0] + string[middle_index] + string[-1]
print("Noul string este:", new_string)
# 19. Se dau doua variabile:
# str1 = 'Abc'
# str2 = 'Xyz'
# Creeaza o variabila string, str3 formata din:
# - primul caracter din str1 cu litera mica
# - primul caracter din str2 cu litera mare
# - al doilea caracter din str1 cu litera mare
# - al doilea caracter din str2 cu litera mare
# - al treilea caracter din str1 cu litera mare
# - al treilea caracter din str2 cu litera mica
str1 = 'Abc'
str2 = 'Xyz'
str3 = str1[0].lower() + str2[0].upper() + str1[1].upper() + str2[1].upper() + str1[2].upper() + str2[2].lower()
print(str3)
# 20. Se da string-ul my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
# Afiseaza ultima pozitie a substring-ului "Emma" in string-ul dat.
# HINT: vezi metoda ajutatoare string rstrip()
my_str = 'Emma is a data scientist who knows Python. Emma works at google.'
last_pos = my_str.rstrip().rfind('Emma')
print(last_pos)
# 21. Split-uieste urmatorul string, dupa caracterul '-':
# str1 = "Maria-is-an-automation-tester."
# Printeaza rezultatul.
str11 = "Maria-is-an-automation-tester."
rez = str11.split('-')
print(rez)
# 22. Scrie un program care citeste doua numere intregi de la tastatura
# si afiseaza rezultatul.
num1 = int(input("Introduceti primul numar: "))
num2 = int(input("Introduceti al doilea numar: "))
rezul = num1 + num2
print(rezul)
# 23. Se da variabila num = 345.3344.
# Afiseaza variabila num cu doua zecimale (hint: search on google).
num = 345.3344
print("Numarul cu doua zecimale este: {:.2f}".format(num))
# 24. Inverseaza lista my_list = [100, 200, 300, 400].
my_list = [100, 200, 300, 400]
reversed_list = my_list[::-1]
print(reversed_list)
# 25. Lista de cumparaturi:
# Se citeste de la tastatura o lista de cumparaturi. Utilizatorul introduce
# lista de cumparaturi ca un string, cu alimentele separate prin virgula,
# ATENTIE: fara spatii
# Exemplu:rosii,castraveti,branza,oua
# a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
# b. Sorteaza lista de cumparaturi si printeaza lista sortata.
# c. Adauga un aliment nou in lista de cumparaturi.
# d. Sterge un aliment din lista de cumparaturi. A se face o stergere aleatorie. (vezi metoda pop())
# e. Modifica elementul de la pozitia 0 din lista.
# f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
# Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
shopping_list_str = input("Introdu lista de cumparaturi (fara spatii, separate prin virgula): ")
shopping_list = shopping_list_str.split(',')
shopping_list.sort()
print("Lista sortata:", shopping_list)
new_item = input("Adauga un nou aliment in lista de cumparaturi: ")
shopping_list.append(new_item)
print("Lista actualizata:", shopping_list)
import random
random_item_index = random.randint(0, len(shopping_list) - 1)
removed_item = shopping_list.pop(random_item_index)
print("Alimentul eliminat: ", removed_item)
print("Lista actualizata: ", shopping_list)
shopping_list[0] = 'lapte'
print("Lista actualizata:", shopping_list)
if 'rosii' in shopping_list:
    print("Aliment sanatos")
else:
    print("Iti recomandam rosiile de asemenea")
# 26. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
# Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). (search on google)
fructe = ['capsuni', 'mere', 'lamai']
fructe_string = ','.join(fructe)
print(fructe_string)
# 27. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
# Afiseaza elementul cu valoarea maxima din string. (google- functia max())
numere = [1, 2, 3, 4, 56, 22, 5]
maxim = max(numere)
print(maxim)
# 28. Se da lista preturi = [12.3, 34.5, 22].
# Calculeaza suma elementelor din lista preturi. (google - functia sum())
preturi = [12.3, 34.5, 22]
suma = sum(preturi)
print(suma)
# 29. Se da dictionarul:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# a. Afiseaza valoarea cheii city.
# b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
# c. Sterge varsta din dictionar.
# d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
# e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
sample_dict = {
     "name": "Kelly",
     "age": 25,
     "salary": 8000,
     "city": "New york"
}
print(sample_dict["city"])
sample_dict["salary"] = 10000
print(sample_dict)
del sample_dict["age"]
sample_dict["employment_date"] = "2023-02-24"
if "country" not in sample_dict:
    sample_dict["country"] = "unknown"
# 30. Se da dictionarul:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
# b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
# c. Verifica lungimea dictionarului.
sample_dict2 = {
     "name": "Kelly",
     "age": 25,
     "salary": 8000,
     "city": "New york"
 }
print("Cheile dictionarului sunt: ", sample_dict2.keys())
print("Valorile dictionarului sunt: ", sample_dict2.values())
print("Lungimea dictionarului este: ", len(sample_dict2))
# 31. Gasirea unui element intr-un dictionar
# Se da dictionarul:
# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# Utilizatorul introduce cheia cautata.
# Verifica daca aceasta se gaseste sau nu in dictionar.
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
cheie = input("Introdu cheia cautata: ")
if cheie in persoana:
    print("Cheia se gaseste in dictionar.")
else:
    print("Cheia nu se gaseste in dictionar.")
# 32. Adaugarea unui element intr-un dictionar
# Se da dictionarul:
#  persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# Utilizatorul trebuie sa introduca cheia si valoarea pe care doreste sa
# le adauge in dictionar.
# Foloseste metoda update() (metoda ajutatoare pe dictionar)
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
cheie = input("Introdu cheia de adaugat: ")
valoare = input("Introdu valoarea de adaugat: ")
persoana.update({cheie: valoare})
print(persoana)
# 33. Stergerea unui element din dictionar
#  Se da dictionarul:
#  persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# Utilizatorul introduce cheia elementului de eliminat.
# a. Elimina elementul, verificand prima data daca cheia se afla in dictionar,
# si daca se afla, foloseste metoda del.
# b. Elimina elementul, folosind metoda ajutatoare pop().
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
cheie = input("Introdu cheia elementului de eliminat: ")
if cheie in persoana:
    del persoana[cheie]
    print("Elementul a fost eliminat cu succes.")
else:
    print("Cheia nu se afla in dictionar.")
print(persoana)
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
valoare = persoana.pop(cheie, None)
if valoare is None:
    print("Cheia nu se afla in dictionar.")
else:
    print("Elementul a fost eliminat cu succes.")
print(persoana)
# 34. Concatenarea a doua dictionare.
# Se dau doua dictioanare:
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# Sa se concateneze cele doua dictionare folosind metoda update().
# Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
# perechi cheie:valoare in dictionar.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)
# 35. Se da urmatoarea lista cu dictionare:
# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
# a. Adauga perechea {'c':'3'} in primul dictionar din lista.
# b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
# c. Aduaga un nou dictionar ca element in lista, la indexul 1.
# d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
lista[0].update({'c': 3})
print(lista)
nou_dict = {'g': 7, 'h': 8}
lista.append(nou_dict)
print(lista)
nou_dict2 = {'i': 9, 'j': 10}
lista.insert(1, nou_dict2)
print(lista)
if 'c' in lista[1]:
    print("Cheia 'c' se gaseste in al doilea dictionar din lista.")
else:
    print("Cheia 'c' nu se gaseste in al doilea dictionar din lista.")
# 36. Se citeste de la tastatura un numar.
# a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
# b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
numar = int(input("Introduceti un numar: "))
if numar % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")
if numar % 4 == 0:
    print("Numarul este multiplu de 4.")

# 37. Se citesc de la tastatura doua numere, num si check. Verifica daca
# num este divizibil cu check si afiseaza un mesaj corespunzator catre utilizator.
num = int(input("Introdu un numar: "))
check = int(input("Introdu un numar de verificat: "))

if num % check == 0:
    print(f"{num} este divizibil cu {check}.")
else:
    print(f"{num} nu este divizibil cu {check}.")
# 38. Se da dictionarul:
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
# b. Schimba valoarea cheii 'year' in 1970.
# c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
# Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si asigand o valoare.
# Adaug-o folosind metoda update()
# d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
# e. Foloseste metoda empty() pentru a 'goli' dictionarul.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get('model'))
car['year'] = 1970
car['color'] = 'red'
car.update({'color': 'red'})
car.pop('model')
car.clear()

# 39. Se da lista:
# fruits = ["apple", "banana", "cherry"]
# a. Schimba elementul 'apple' cu 'kiwi'.
# b. Foloseste metoda append() pentru a adauga elementul 'oranges'.
# c. Foloseste metoda insert() pentru a adauga elementul 'lemon' ca al doilea
# element din lista.
# d. Foloseste metoda remove() pentru a sterge elementul 'banana' din lista.
# e. Foloseste un index negativ pentru a accesa ultimul element din lista.
# f. Foloseste un index negativ pentru a accesa penultimul element din lista.
# g. Afiseaza lungimea listei.
# h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, al treilea
# si al patrulea element.
fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'
fruits.append('oranges')
fruits.insert(1, 'lemon')
fruits.remove('banana')
fruits[-1]
fruits[-2]
print(len(fruits))
new_list = fruits[1:4]
# 40. Se da dictionarul my_dict = { 1: 'hello', 2: 'world'}.
# Creeaza o copie a dictionarului cu metoda copy().
my_dict = {1: 'hello', 2: 'world'}
copy_dict = my_dict.copy()