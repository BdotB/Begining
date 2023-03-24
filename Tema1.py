# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila.
# O variabila este un loc de stocare pentru o valoare care poate fi schimbata in timpul executiei programului

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool.
# Valorile le alegeti voi dupa preferinte.
nume = "Bogdan"
numar = 29
exercitiu = 4.23
rezolvat = True
print(exercitiu)

# 3. Utilizati functia type(), pentru a verifica daca variabilele declarate la punctul 2 au tipul de date asteptat.
print(type(nume))
print(type(numar))
print(type(exercitiu))
print(type(rezolvat))

# 4. Rotunjiti variabila definita ca tip float, folosindu-va de functia round() si salvati aceasta modificare in aceeasi
# variabila (suprascriere). Verificati apoi tipul acesteia.
print(round(exercitiu))
exercitiu = round(exercitiu)
print(type(exercitiu))

# 5. Folositi functia print() pentru a printa in consola 4 propozitii, folosind cele 4 variabile.
# (Rezolvati nepotrivirile de tip prin ce modalitate doriti)
print("Numele meu este " + nume + " am varsta " + str(numar) + " am rezolvat exercitiul " + str(exercitiu) + ' ' +  str(rezolvat))
print("Pe el il cheama " + nume)
print("Afara sunt " + str(numar) + " de grade")
print("Cel de mai sus este exercitiul " + str(exercitiu))
print("Exercitiul este complet " + str(rezolvat))

# 6.
# a. Defineste o variabila float cu valoarea 1.5 .
a = 1.5

# b. Verifica daca variabila este egala cu 1.5 .
assert a == 1.5
print('da')

# c. Verifica daca variabila este egala cu true. Ce observi?
#assert a == True
#Eroare ? Nu trece mai departe deoarece a este de tip float iar True este operator logic asa ca trb sa folosim bool

# d. Cum poti face ca assert-ul de la punctul c sa treaca?
a = bool(a)
print ("enuntul este " + str(a))