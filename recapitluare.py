
# 1. Explica intr-un comentariu ce este o functie.

# FUNCTIE = este un bloc de cod care se executa doar atunci cand
# este apelata.
# Avantajul unei functii este ca este reutilizabila
# ( o putem folosi/invoca de cate ori vrem)

# 1. Explica intr-un comentariu ce este o functie.

# FUNCTIE = este un bloc de cod care se executa doar atunci cand
# este apelata.
# Avantajul unei functii este ca este reutilizabila
# ( o putem folosi/invoca de cate ori vrem)

# 2. Se da urmatoarea functie:

def suma(a, b):
    return a + b

# a. Care sunt parametrii functiei de mai sus?

# parametrii sunt a si b.

# b. Ce este un return?

# un return intr-o functie = date de iesire din functie

# c. Care este numele functiei?

# numele functiei este suma

# d. Apeleaza/invoca functia, pe rand, cu urmatoarele valori:
# - 2, 3
# - 100, 50
# Afiseaza rezultatul.

# print(suma(2, 3))
#
# sum2 = suma(100, 50)
# print(sum2)

# 3. Se da urmatoarea functie:

def calculate_total_price(name: str, price: float, quantity: int):
  total_price = price * quantity
  print(f"The total price for '{name}' este {total_price}")

# The total price for 'mere' este 200.

# a. Care sunt parametrii functiei?

# Parametrii sunt name, price si quantity.

# b. Care este diferenta intre parametri si argumente?

# Parametri = sunt datele care le scriem cand definim functia
# Argumentele = sunt definite cand apelam functia (valori pe care
# le dam parametrilor)

# Da exemple de argumente pentru functia data.
calculate_total_price('lapte', 10, 10)
calculate_total_price('paine', 5, 2)
# c. Descrie, verbal, ce face functia data.
# d. Apeleaza functia cu doua seturi diferite de valori.
calculate_total_price('lapte', 10, 10)
calculate_total_price('paine', 5, 2)

# 4. Se dau urmatoarele functii:

def find_first_occurence(c: str, sequence: str):
    for i in range(0, len(sequence)):
        if c == sequence[i]:
            return i
            # print("Caracterul a fost gasit!") => niciodata nu vom ajunge la linia asta
        # else:
        #     continue
            # print("Inca cautam caracterul") => niciodata nu se va afisa

def find_first_occ(c: str, sequence: str):
    for i in range(len(sequence)):
        if c == sequence[i]:
            print("Caracterul a fost gasit!") # se va afisa
            return i
        print("Inca cautam caracterul")

find_first_occurence('a', 'abcd')
find_first_occ('a', 'abcd')

# a. Explica, verbal, ce fac cele doua functii.
# b. Crezi ca daca apelam cele doua functii cu acelasi set
# de valori, vom avea acelasi rezultat sau va fi diferit?
# Explica diferentele si neconcordantele, daca sunt.