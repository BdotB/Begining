'''
def first_function():
    print("hello world!")
first_function()
print(2)
first_function()
first_function()
first_function()
'''
# 1. Defineste o functie care printeaza pe rand primele 10 numere (1-10)
# def numere():
#     for i in range(1, 11):
#         print(i)
# numere()

#FUNCTII CU PARAMETRI

# functie cu 1 singur argument/parametru
# def print_hi(user):
#     print(f"Hi, {user}")
#
# print_hi('Andy87') # Hi Andy 87
# print_hi('Andrei') # Hi Andrei
#
# # functie cu doi parametri
#
# def add_numbers(a, b):
#     result = a + b
#     print(f'Sum: {result}')
#
# add_numbers(1, 2)  # Sum: 3
# add_numbers(3, 4)  # Sum: 7
# add_numbers(1) # => EROARE!!
# add_numbers(1, 2, 3) # => EROARE!!

# def add_numbers(a, b):
#     result = a + b
#     print(f'Sum: {result}')
#
# add_numbers(a=1, b=2)
# add_numbers(a=3, b=4)

#. Scrie o functie care parcurge o lista de numere data si
# afiseaza mesajul 'Este par' pentru numerele pare si
# 'Este impar' pentru numere impare.
# Daca in lista se gaseste un element care nu e numar intreg,
# afiseaza un mesaj utilizatorului si apoi sari peste
# elementul respectiv.
# (Foloseste functia built-in isinstance()
# pentru verificare daca elementul curent e int sau nu)

# def verifica_lista(lista):
#     for elem in lista:
#         if not isinstance(elem, int):
#             print(f"{elem} nu este un numar intreg, trecem la urmatorul element")
#             continue
#         if elem % 2 == 0:
#             print(f"{elem} este par")
#         else:
#             print(f"{elem} este impar")
# numere = [2, 7, 4, 8, "abc", 5, 10]
# verifica_lista(numere)
#
# def parcurg_ista_numere_pare(lista_in):
#     for i in lista_in:
#         if isinstance(i, int):
#             if i%2 ==0:
#                 print('este par')
#             else:
#                 print('este impar')
#         else:
#             continue
#
# parcurg_ista_numere_pare([3, 7, 9, 11, 8])
# parcurg_ista_numere_pare([1, 2, 'abc'])

# def get_square(i):
#     square = i ** 2
#     print(square)
# get_square(3)
# get_square(12)

# 4. Scrie o functie care calculeaza inmultirea dintre doua numere.
# Afiseaza rezultatul.

# def inmultire_numere(a,b):
#     inmultire = a*b
#     print(inmultire)
# inmultire_numere(3,4)
# inmultire_numere(5,7)
#
# def numar_preferat():
#     numar = 7
#     return numar
# rez = numar_preferat()
# print(rez)

# functie cu parametri si return
# def is_natural(numar):
#     if numar >= 0:
#         return 'numarul este natural'
#     else:
#         return 'numarul nu este natural'
#
# raspuns = is_natural(3)
# print(raspuns)

# functie cu return
#
# def numar_preferat():
#     numar = 7
#     return numar
#
# rezultat = numar_preferat()
# print(rezultat)
#
# # functie cu parametri si return
# def is_natural(numar):
#     if numar >= 0:
#         return 'numarul este natural'
#     else:
#         return 'numarul nu este natural'
#
# raspuns = is_natural(3)
# print(raspuns)
#
# raspuns2 = is_natural(-5)
# print(raspuns2)
#Rescrie functia de la exercitiul 3, astfel incat sa returneze rezultatul.
# Rescrie functia de la exercitiul 4, astfel incat sa returneze rezultatul.
# def get_square(i):
#     sq = i ** 2
#     return sq
#
# numar = get_square(9)
# print(numar)
#
# def inmultire_numere(a,b):
#     inmultire = a*b
#     return inmultire
#
# numar = inmultire_numere(8,9)
# print(numar)nn

# 10. Scrie o functie care ia ca parametru un numar intreg si returneaza True daca numarul e par
# si False daca numarul e impar.

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
a = is_even(5)
print(is_even(40))
print(a)
