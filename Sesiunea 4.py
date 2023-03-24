# RECAPITULARE

# Structuri de date

# LISTE
'''
# 1.
# DEFINIRE LISTA
# a. Defineste o lista cu numerele intregi de la 1 la 5.
numere = [1, 2, 3, 4, 5]
# b. Este o lista ordonata/neordonata?
# Descrie intr-un comentariu raspunsul tau si demonstreaza in cod
    #in aceeasi ordine in care au fost scrise + putem accesa elementele
# folosind lista de la punctul a.
print(numere[1])
# c. Este o lista mutabila/imutabila?
# Descrie intr-un comentariu raspunsul tau si demonstreaza in cod
    #elementele din lista pot fii modificate
# folosind lista de la punctul a.
numere.append(5)
print(numere)

# ACCESARE ELEMENTE DIN LISTA
# d. Acceseaza al doilea element din lista si printeaza-l.
print(numere[1])

# ADAUGARE ELEMENTE NOI IN LISTA
# e. Adauga un element nou la finalul listei.
numere.append(6)

# f. Adauga un element nou la indexul 1.
numere.insert(1, 11)

# MODIFICARE ELEMENT DIN LISTA
# g. Modifica un element din lista.
numere[2] = 10
print(numere)
# STERGERE ELEMENT DIN LISTA
# h. Sterge elementul/cifra 4 din lista, dupa valoare.
numere.remove(4)
print(numere)
# i. Sterge elementul/cifra 4 din lista, dupa index.
#del numere[4]
numere.pop(4)
print(numere)
# LUNGIMEA LISTEI
# j. Afiseaza lungimea listei.
print(len(numere))
# DEFINIRE DICTIONAR
# angajat_nou = {
#     'nume': 'Pop Marian',
#     'data angajare': '12.02.2023',
#     'salariu': 5000
# }

# a. Este dictionarul ordonat/neordonat?
# Descrie intr-un comentariu raspunsul tau si demonstreaza in cod
# folosind dictionarul dat.
#dictionarul este neordonat, nu putem accesa elementele dupa index ci le accesam duap chei

# b. Este dictionarul mutabil/imutabil?
# Descrie intr-un comentariu raspunsul tau si demonstreaza in cod
# folosind dictionarul dat.
#dictionarul este mutabil -> elem din dictionar pot sa fie modificate/adaugate/sterse


angajat_nou = {
    'nume': 'Pop Marian',
    'data angajare': '12.02.2023',
    'salariu': 5000
}
# ACCESARE
# c. Acceseaza si afiseaza numele noului angajat.
print(angajat_nou['nume'])
# d. Acceseaza si afiseaza salariul angajatului nou, dar asigura-te
# in acelasi timp, ca daca nu gasesti salariul in dictionar,
# vei afisa valoarea 0.
salariu = angajat_nou.get('salariu', 0)
print(salariu)

# ADAUGARE

# ADAUGARE ACCESAND ELEMENTUL DUPA CHEIE
# e. Adauga departamentul in care lucreaza noul angajat, folosind
# accesare dupa cheie. Valoarea o alegi tu.
angajat_nou['departament'] = 'marketing'
# ADAUGARE FOLOSIND METODA UPDATE
# f. Adauga durata perioadei de proba pentru noul angajat, folosind metoda update.
perioada_proba = {'perioada proba ': 1}
angajat_nou.update(perioada_proba)
print(angajat_nou)
# MODIFICARE

# MODIFICARE ACCESAND ELEMENTUL DUPA CHEIE
# g. Modifica salariul angajatului sa fie 6000, folosind accesarea dupa cheie.
angajat_nou['salariu'] = 6000
# MODIFICARE FOLOSIND METODA UPDATE
# h. Modifica salariul angajatului sa fie 7000, folosind metoda update.
salariu_nou = {'salariu': 7000}
angajat_nou.update(salariu_nou)
print(angajat_nou)

# STERGERE

# STERGERE ACCESAND ELEMENTUL DUPA CHEIE
# i. Sterge departamentul in care lucreaza angajatul nou, dupa cheie.
del angajat_nou['departament']
print(angajat_nou)
# STERGERE FOLOSIND METODA POP
# j. Sterge salariul angajatului, folosind metoda pop
angajat_nou.pop('salariu')
'''

# SET
fruits = {"apple", "banana", "orange", "grape"}
# adaugam un fruct in set (se adauga la pozitie aleatorie)
fruits.add("watermelon")
print(fruits)
# stergem elementul apple din set
fruits.remove("apple")
print(fruits)
# stergem un elem aleatoriu din set
fruits.pop()
print(fruits)
print(len(fruits))
# seturile au elemente unice, nu au elem duplicate

# 1. Se da lista
# numere_intregi = [1, 2, 3, 4, 5, 1, 5, 4]
# Sa se elimine duplicatele din lista si sa se afiseze
# noua lista. (hint: type casting).
numere_intregi = [1, 2, 3, 4, 5, 1, 5, 4]
numere = set(numere_intregi)
numere_finale = list(numere)
# numere = list(set(numere_intregi))
print(numere)
print(numere_finale)
# 2. Se de set-ul:
# my_set = {1, 2, 3, 4, 5}
my_set = {1, 2, 3, 4, 5}
# a. Adauga numerele 6 si 7 in set
my_set.add(6)
my_set.add(7)
print(my_set)
# b. Sterge numarul 3
my_set.remove(3)
print(my_set)
# c. Sterge aleator un element din set
my_set.pop()
print(my_set)

# TUPLU
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(my_tuple[0])  # apple
print(my_tuple[1])  # banana
print(my_tuple[2])  # cherry
print(len(my_tuple))  # 3
# 1. Se da urmatorul tuplu, care stocheaza datele despre un
# student (nume, prenume, facultate, nota examen)
# student1 = ("Ion", "Pop", "Facultatea de Mecanica", 9)

# Verifica media studentului1 si afiseaza un mesaj in functie
# de aceasta:
# daca media e mai mare sau egala cu 5, afiseaza mesajul "Studentul x a trecut examenul"
# altfel, afiseaza mesajul "Studentul x nu a trecut examenul"
student1 = ('Ion', 'Pop', 'Facultatea de Mecania', 9)
if student1[3] >= 5:
    print("Studentul", student1[0] + ' ' + student1[1], "a trecut examenul")
else:
    print("Studentul", student1[0] + ' ' + student1[1], "nu a trecut examenul")
# 2. Se dau urmatoarele doua tupluri care salveaza date despre
# 2 produse din supermarket. Valorile reprezinta in ordine:
# nume produs, pret, cantitate in stoc.
# produs1 = ("Lapte", 8.5, 0)
# produs2 = ("Paine", 5, 2)
# a. Pentru fiecare produs, verifica daca produsul este in stoc
# si afiseaza un mesaj sugestiv.
# b. Afiseaza lungimea tuplului produs1.
produs1 = ("Lapte", 8.5, 0)
produs2 = ("Paine", 5, 2)
if produs1[2] > 0:
    print("Produsul", produs1[0], "este in stoc")
else:
    print("Prodsul", produs1[0], "nu este in stoc")
if produs2[2] > 0:
    print(f"Produsul {produs2[0]} este in stoc")
else:
    print(f"Produsul {produs2[0]} nu este in stoc")
print(len(produs1))

# WHILE / WHILE ELSE
i = 0
while i <= 3:
    print(i)
    i += 1
else:
    print("Am terminat ciclul repetitiv while.")
# 1. Se da numarul x = -5.
# Foloseste un while pentru a afisa numerele negative pornind
# de la -5.
# La final, afiseaza un mesaj ca s-au afisat toate numerele
# negative.
x = -5
while x < 0:
    print(x)
    x += 1
else:
    print("s-au afisat toate numerele negative")

# FOR/ FOR ELSE
for i in range(4):
    print(i)
else:
    print("am terminat")
# 1. Afiseaza toate numerele pare pana la 10.
for y in range(0, 11):
    if y % 2 == 0:
        print(y)

legume = ['rosii', 'castraveti', 'varza', 'conopida']
#print(legume[0])
#print(legume[1])
#print(legume[2])
#print(legume[3])
for index_legume in range(0, len(legume)):
    print(legume[index_legume])

''' varianta cu for each
for leguma in legume
    print(leguma)
'''

#FOR EACH

culori = ["rosu", "albastru", "galben", "mov"]

for culoare in culori:
        print(f"Culoarea mea preferata este {culoare}")

# 1. Se da lista:
#legume = ['rosii', 'castraveti', 'varza', 'conopida']
# Afiseaza toate elementele din lista folosind for each.
vegg = ['rosii', 'castraveti', 'varza', 'conopida']
for veg in vegg:
    print(veg)
#2. Se da lista:
# produse = [
#     {
#         'nume produs': 'Rosii',
#         'pret': 5
#     },
#     {
#         'nume produs': 'Paine',
#         'pret': 8
#     },
#     {
#         'nume produs': 'Lapte',
#         'pret': 6
#     },
#     {
#         'nume produs': 'Cafea'
#     }
# ]
# Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]

for x in produse:
    if 'pret' in x.keys() and x['pret'] > 5:
#if x.get('pret', False) and x['pret'] >5
        print(x['nume produs'])

for z in range(1, 50):
    if z == 3:
        break
    print(z)

for t in range(5):
    if t == 3:
        continue
    print(t)
#afisam primul numar par din intervalul 1 10
for l in range(1, 11):
    if l % 2 == 0:
        print(l)
        break
#afisam numerele din lista numeree in afara de numerele 3 si 5
numeree = [1, 2, 3, 4, 5, 6, 7]
for ii in numeree:
    if ii == 3 or ii == 5:
        continue
    print(ii)

