# 1. Citeste de la tastatura un string de dimensiune impara. Afiseaza caracterul din mijloc.
# introducem un sir de la tastatura
s = input("Introduceți un șir: ")
# calculam lungimea sirului
l = len(s)
# verificam daca lungimea sirului este impara
if l % 2 == 1:
    #daca lungimea sirului este impara atunci acesta o sa fie caracterul din mijloc
    m = s[l // 2]
    print("Caracterul din mijloc este:", m)
else:
    print("Lungimea șirului trebuie să fie impară.")
# 2. Folosind assert, verificati daca un string este palindrom.
def is_palindrome(string):
    return string == string[::-1]
string = input("Introduceti un string: ")
if is_palindrome(string):
    print("String-ul introdus este un palindrom.")
else:
    print("String-ul introdus nu este un palindrom.")
# 3. Folosind o singura linie de cod, citeste un string de la tastatura (ex: 'alabala portocala') si salveaza fiecare
# cuvant intr-o variabila. Printeaza variabilele generate pentru verificare.
cuv = [word for word in input("Introduceti un string: ").split()]
print(cuv)
# 4. Citeste un string de la tastatura (ex: 'alabala portocala'). Salveaza primul caracter din string intr-o variabila.
# Capitalizeaza acest caracter peste tot in string, mai putin primul si ultimul caracter.
# Exemplu 1:
#   input: 'alabala portocala'
#   output: 'alAbAla portocAla'
# Exemplu 2:
#   input: 'maria are mere'
#   output: 'maria are Mere'
# Exemplu 3:
#   input: 'aritmetica'
#   output: 'aritmetica'
string = input("Introduceti un string: ")
first_char = string[0]
new_string = first_char + string[1:-1].replace(first_char, first_char.upper()) + string[-1]
print(new_string)
# 5. Citeste un user de la tastatura. Citeste apoi o parola de la tastatura. Afiseaza: 'Parola pentru userul x este ***
# si are y caractere.', unde x este user-ul citit de la tastatura, iar y lungimea parolei introduse la tastatura.
# Numarul de * din stringul afisat se va calcula dinamic, avand atatea * cate caractere exista in parola.
# Exemplu:
#   - daca parola introdusa este 'abcd', vom avea ***
#   - daca parola introdusa este 'abcdef', vom avea ******.
user = input("Introduceti un user: ")
password = input("Introduceti o parola: ")
print(f"Parola pentru user-ul {user} este {'*' * len(password)} si are {len(password)} caractere.")