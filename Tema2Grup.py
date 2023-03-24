'''
# C. OPTIONAL (nivel > MEDIU) (s-ar putea sa ai nevoie de Google)

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# . Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).    '''

x = int(input("Introduceti un numar de la tastatura: "))
if len(str(x)) >= 4:
    print("Numarul are minim 4 cifre")
else:
    print("Numarul are mai putin de 4 cifre")
# 2. Verifica daca x are exact 6 cifre.

if len(str(x)) == 6:
    print("Numarul are exact 6 cifre")
    '''
# 3. Verifica daca x este numar par sau impar.
if x%2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
# 4. Avand trei variabile x, y, z (toate int) (le poti declara in cod sau citi de la tastatura),
# afiseaza in consola care este cel mai mare dintre ele.
y = int(input("Introduceti un numar de la tastatura: "))
z = int(input("Introduceti un numar de la tastatura: "))
if x > y and x > z:
    print("x este cel mai mare.")
elif y > x and y > z:
    print("y este cel mai mare.")
else:
    print("z este cel mai mare.")
# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid
# sau nu. (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau
# daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi).
if x + y + z == 180:
    print("Este un triunghi valid")
else:
    print("Nu este un triunghi valid")
# 6.
# a. Avand stringul: 'Coral is either the stupidest animal or the smartest rock', citește de la tastatura
# un număr x de tip int.
# b. Afișează stringul fără ultimele x caractere.
# Exemplu: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
s = "Coral is either the stupidest animal or the smartest rock"
i = int(input("Introduceti un numar de la tastatura"))
print(s[:-i])
# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din
# primele 5 caractere + ultimele 5 caractere.
s2 = s[:5] + s[-5:]
print(s2)
# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start
# al cuvântului rock - adică poziția in string la care începe cuvântul rock.
# (hint: este o funcție care te ajuta sa faci asta).
index = int(s.find("rock"))
print(index)
# Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant.
print(s[0:index])
# Output asteptat: 'Coral is either the stupidest animal or the smartest '
# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul
# si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
string = input("Introduceti un string ")
assert string[0].lower() == string[-1].lower()
print("Primul si ultimul caracter sunt la fel")

# 10. Avand stringul '0123456789', afiseaza doar numerele pare si apoi doar numerele impare.
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

stringn = "0123456789"
print(stringn[::2], "Numere pare")
print(stringn[1::2], "Numere impare")


# D. EXERCITII BONUS

# 1. Vrem sa cream o aplicatie pentru achizitionare de bilete de avion care sa primeasca drept inputuri
# urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport.
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti.
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la
# celalat parinte.
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi
# ca ar trebui testate.
# Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results
# sunt egale cu actual results.
# Exemple:
# 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
def urcare_avion (varsta, pasaport, insotit_de_mama, insotit_de_tata, act_permisiune_mama, act_permisiune_tata):
    if varsta >= 18 and pasaport:
        return True
    elif varsta < 18 and pasaport:
        if insotit_de_mama and insotit_de_tata:
            return True
        elif insotit_de_mama and act_permisiune_tata:
            return True
        elif insotit_de_tata and act_permisiune_mama:
            return True
    return False

# Scenarii de testare:
# 1. 20 de ani cu passport : true
assert urcare_avion(20, True, False, False, False, False) == True
print(1)
# 2. 17 ani cu passport si insotit de ambii parinti : true
assert urcare_avion(17, True, True, True, False, False) == True
print(2)
# 3. 16 ani cu passport insotit de mama si cu permis de la tata = true
assert urcare_avion(16, True, True, False, False, True) == True
print(3)
# 4. 16 ani cu passport insotit de mama si fara permis de la tata = false
assert urcare_avion(16, True, True, False, False, False) == False
print(4)
# 5. 25 de ani fara passport = false
assert urcare_avion(25, False, False, False, False, False) == False
print(5)

# 2. Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random.
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online.
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator.
# - Verifica si afiseaza daca utilizatorul a ghicit numarul.
# - Vor exista 3 optiuni care vor trebui tratate:
# a. Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# b. Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# c. Ai ghicit. Felicitari! Ai ales x si zarul a fost y.

import random

# Generare numar random intre 1 si 6, simuland un zar
dice_roll = random.randint(1, 6)

# citire numar ales de utilizator
user_choice = int(input("Introdu un numar intre 1 si 6: "))

# verificare daca utilizatorul a ghicit numarul
if user_choice == dice_roll:
    print(f"felicitari, ai ales {user_choice} si zarul a fost {dice_roll}.")
elif user_choice < dice_roll:
    print(f"ai ales un numar mai mic {user_choice} dar a fost {dice_roll}.")
else:
    print(f"ai ales un numar mai mare {user_choice} dar a fost {dice_roll}.")


# 3. Verifica daca varsta introdusa de utilizator este mai mare
# decat 18 ani.
age = int(input("Introduceti varsta: "))
if age >= 18:
    print("esti major ")
else:
    print("nu esti major ")

# 4. Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
price = float(input("Introdu pretul produsului: "))
if price <= 100:
    print("Pretul este mai mic sau egal cu 100 de dolari.")
else:
    print("Pretul este mai mare de 100 de dolari.")
# 5.
# a. Citeste un numar de la tastatura.
# b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
number = int(input("Introdu un numar: "))
if number % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

# 6.
# a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
# b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
# c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
speed = int(input("Introdu viteza ta: "))
if speed <= 50:
    print("Viteza normala.")
else:
    print("Viteza depasita.")

# 7. Citeste de la tastatura varsta utilizatorului si afiseaza categoria
# de varsta in care se incadreaza.
# Tine cont de aceste categorii de varsta:
# intre 0-18 ani: minor
# intre 18-65 ani: adult
# peste 65 ani: senior
age = int(input("Introdu varsta ta: "))
if age < 18:
    print("Minor.")
elif age <= 65:
    print("Adult.")
else:
    print("Senior.")
''''''
# 8. Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
# cosul de cumparaturi, in functie de totalul cosului de cumparaturi
# Reducerea se aplica in felul urmator:
# - Total este intre 100 si 200 lei -> reducere 10%
# - Total intre 200 - 300 lei -> reducere 15%
# - Total intre 300-400 -> reducere 20 %
# - Total mai mare de 400 -> reducere 30 %.
# a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
# b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
# dupa aplicarea reducerii.
total = float(input("Introdu totalul cosului de cumparaturi: "))
if total < 100:
    print(f"Pretul final este: {total:.2f}")
elif total <= 200:
    discount = total * 0.1
    final_price = total - discount
    print(f"Pretul final este: {final_price:.2f} (Reducere 10%: {discount:.2f})")
elif total <= 300:
    discount = total * 0.15
    final_price = total - discount
    print(f"Pretul final este: {final_price:.2f} (Reducere 15%: {discount:.2f})")
elif total <= 400:
    discount = total * 0.2
    final_price = total - discount
    print(f"Pretul final este: {final_price:.2f} (Reducere 20%: {discount:.2f})")
elif total > 400:
    discount = total * 0.3
    final_price = total - discount
    print(f"Pretul final este: {final_price:.2f} (Reducere 30%: {discount:.2f})")'''