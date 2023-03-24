# RECAPITULARE

# SETURI
# 1. Explica intr-un comentariu:
# a. Ce sunt seturile
#structuri de date care contin elemente unice
# b. Sunt seturile ORDONATE/NEORDONATE?
#neordonate --> elementele nu sunt salvate in memorie in oridinea in care sunt adaugate
# c. Sunt seturile MUTABILE/IMUTABILE?
#seturile sunt mutabile / putem sterge si adauga elemente

# 2. Se da setul:
# fructe = {'capsuni', 'mere', 'pere'}
# a. Adauga un nou element in set: 'pepene'.
fructe = {'capsuni', 'mere', 'pere'}
fructe.add('pepene')
print(fructe)
# b. Adauga 'capsuni' in set. Ce observi?
fructe.add('capsuni')
print(fructe)
# c. Sterge elementul 'capsuni'.
fructe.remove('capsuni')
# d. Sterge un element aleator.
fructe.pop()
# e. Salveaza dimensiunea set-ului intr-o variabila si afiseaz-o.
x = len(fructe)
print(x)

# TUPLURI
# 1. Explica intr-un comentariu:
# a. Ce sunt tuplurile
#structuri de date care pot pastra mai multe valori intr-o singura variabila
#my_tuple = ('a', 'b', 'c')
# b. Sunt tuplurile ORDONATE/NEORDONATE?
#tuplurile sunt ordonate(se salveaza in memorie in ordinea introdusa)
# c. Sunt tuplurile MUTABILE/IMUTABILE
#tuplurile sunt imutabile(elem nu se pot modifica)

# 2. Citeste de la tastatura numele a trei tari pe rand.
# Salveaza numele celor trei tari intr-un tuplu.
'''
tara1 = input("Introduceti o tara de la tastatura: ")
tara2 = input("introduceti o tara de la tastatura: ")
tara3 = input("introduceti o tara de la tastatura: ")
tari = (tara1, tara2, tara3)
for i in tari:
    print("Tara mea preferata este: ",i)
'''
# Folosind un for, afiseaza urmatorul mesaj pentru fiecare tara:
# Tara mea preferata este x.

# WHILE
# 1. Explica intr-un comentariu ce este un while.
#while este un ciclu repetitiv care se va executa atata timp cat o conditie este adevarata
#while poate avea si un else si elseul se executa cand se termina whileul
# 2. Mihai doreste sa isi cumpere o bicicleta electrica.
# Aceasta costa 10 000 lei si ar vrea sa stie cate luni va dura
# sa stranga suma dorita daca economiseste 1 000 lei in fiecare luna.
buget = 0
luni = 0
while buget < 10000:
    luni += 1
    buget += 1000
else:
    print(luni)

# FOR
# 1. Explica intr-un comentariu ce este un for.
#for = un ciclu repetitiv care se executa cat timp conditia se indeplineste

# 2. Explica verbal ce face urmatoarele programe:
my_list = ['a', 'b', 'c']
for i in my_list:
    print(i)
    break
else:
    print("hello")
# a.
# fructe = ['capsuni', 'mere', 'pere']
# for fruct in fructe:
#     if fruct == 'capsuni':
#         print("Am gasit fructul meu preferat")
#         break
#     print(f"Acesta este un fruct bun, dar nu preferatul meu {fruct}")
#

# b.
# lista_numere = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_div_5 = []
# for i in lista_numere:
#     if i % 5 == 0:
#         lista_div_5.append(5)
#
# print(lista_div_5)

# 3. Se da lista:
# my_list = [4, 56, 24, 70, 5, 3, 53, 22]

# Folosind lista data, va trebui folosin un for, sa ajungi
# la urmatoarea lista pe care sa o si afisezi:
# [0, 0, 0, 0, 5, 3, 53, 0]
#
# Rezolva problema folosind for. Apoi rezolva aceeasi problema
# folosind foreach
my_list = [4, 56, 24, 70, 5, 3, 53, 22]
for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = 0
            print(my_list)
# foreach
# for i in my_list:
#     if i % 2 == 0:
#         i = 0
#
# print(my_list)
