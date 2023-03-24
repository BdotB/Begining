
# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.
'''
nume = input(" introduceti numele ")
prenume = input(' introduceti prenumele ')
x = len(nume + prenume)
print(f'Numele complete are {x} caractere')
'''
# 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.
'''
lungimea = int(input(' Introduceti lungimea dreptunghiului '))
latimea = int(input(' Introduceti latimea dpretungiului '))
x = lungimea * latimea
print (f' Aria dreptunghiului este {x}')
'''
# 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# 'the' in acesta.
'''
string = 'Coral is either the stupidest animal or the smartest rock'
cuvant = 'the'
aparitii = string.count(cuvant)
print("Cuvantul ", cuvant, "apare de ", aparitii, "ori in text" )
'''
# 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# rezultatul.
'''
string = 'Coral is either the stupidest animal or the smartest rock'
string2 = string.replace('the', 'THE')
print(string2)
'''
# 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# numere.
'''
lungimea = input(' Introduceti lungimea dreptunghiului ')
latimea = input(' Introduceti latimea dpretungiului ')
assert lungimea.isdigit() and latimea.isdigit(), " Lungimea si latimea trebuie sa fie numere"
lungimea = int(lungimea)
latimea = int(latimea)
x = lungimea * latimea
print(" aria este", x)
'''
# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:
# a. endswith()
'''endswith() este o metoda a obiectelor de tip sir de caractere(string) care returneaza o valoare booleana care 
indica daca sirul se termina cu un alt sir specificat
EX: 
text = 'Ana are mere'
if text.endswith('mere'):
    print('Da, textul se termina cu "mere"')
else:
    print('Nu, textul nu se termina cu "mere"')
'''
# b. index()
'''index() este o metoda a obiectelor de tip sir de caracter(string) care retureaza pozitia (indexul) primei aparitii
a unui alt sir specificat in cradrul sirului original
EX1:
x = 'Ana are mere'
y = x.index('are')
print(y)
Putem sa cautam un sir in sirul original si dupa o pozitie anume
EX2:
x= 'Ana are mere'
y= x.index('a', 3)   #cautam 'a' dupa ignorand/trecand peste pozitia 3 
print(y)
'''
# c. lower()
'''lower() converteste toate caracterele dintr-un sir in caractere cu litere mici
EX:
text = ' Ana are Mere'
lower_text = text.lower()
print(lower_text)
'''
# d. replace()
'''replace() se foloseste pentru a inlocui intr-un sir cu un alt sir
EX:
text = 'Hello, World'
new_text = text.replace('o', 'x')
print(new_text)
'''
# e. strip()
'''strip()  indeparteaza caracterele albe(spatii, tab-uri, newline-uri) de la ambele margini ale sirului
   lstrip() indeparteaza din stanga
   rstrip() indeparteaza din dreapta
EX
text = ' hello world '
new_text = text.strip()
print(new_text)
'''
# f. split()
'''split() se foloseste pentru a imparti un sir in mai multe subsiruri bazandu-se pe o anumita conditie
EX'''
'''
text = 'hello world'
cuvant = text.split()
print(cuvant)
text2 = '13 4 5 6'
numar = text2.split()
print(numar)
'''

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.
""" If este o conditie daca este indeplinita se executa else se executa cealalta conditie"""
# 7. Verifica si afiseaza daca x este numar natural sau nu.
# (un numar se considera natural daca este numar intreg mai mare ca 0)
'''
n = 10
if isinstance(n, int) and n >= 0:
    print("n este un număr natural")
else:
    print("n nu este un număr natural")
'''
# 8.. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0)
'''
x = float(input("Introdu un numar: "))
if x > 0:
    print("Numarul este pozitiv")
elif x < 0:
    print("Numarul este negativ")
else:
    print("Numarul este neutru")
'''
# 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).
'''
x = float(input("Introdu un numar: "))
if -2 <= x <= 13:
    print("Numarul este in intervalul cerut")
else:
    print("Numarul nu este in intervalul cerut")
'''
# 10.
# a. Declara o noua variabila numita y, de tip int.
'''
y = int(input("Introdu un numar de tip int "))
# b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = float(input("Introdu un numar "))
if x - y < 5:
    print("Diferenta dintre x si y este mai mica de 5 ")
else:
    print("Diferenta dintre x si y este mai mare sau egala cu  5")
'''
# 11. Verifica daca  x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
'''
x = float(input("Introdu un numar de la tastatura: "))
if not 5 <= x <= 27:
    print("Numarul nu este in intervalul dorit")
else:
    print("Numarul este in intervalul dorit")
'''
# 12.
# a. Declara o noua variabila numita y, de tip int.
'''
x = int(input("Introdu un numar de la tastatura: "))
y = int(input("Introdu un numar de la tastura "))
# b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.
if x == y:
    print("X este ", x, "Y este ", y)
elif x > y:
    print("X este ", x)
elif x < y:
    print("Y este", y)
'''
# 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
'''
x = int(input("Introdu latura 1 "))
y = int(input("Introdu latura 2 "))
z = int(input("Introdu latura 3 "))
if x == y == z:
    print("Triunghiul este echilateral ")
elif x == y or y == z or x == z:
    print("Triunghiul este isoscel ")
else :
    print("Triunghiul este oarecare ")
'''
# 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''
x = input("Introduceti o litera de la tastatura: ")
if x.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Litera este voacala")
else:
    print("Litera nu este voacala")
'''
    # 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
x = float(input("Introduceti nota: "))
if x > 9:
    x = "A"
    print("Ati luat nota: ",x )
elif 8 <= x <= 9:
    x = "B"
    print("Ati luat nota: ",x)
elif 7 <= x < 8:
    x = "C"
    print("Ati luat nota: ",x)
elif 6 <= x < 7:
    x = "D"
    print("Ati luat nota: ",x)
elif 4 <= x < 6:
    x = "E"
    print("Ati luat nota: ",x)
else:
    x = "F"
    print("ati luat nota: ",x)