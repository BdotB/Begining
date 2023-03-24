'''
#1.Având lista:
#mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
#'Fiat', 'Trabant', 'Opel']
#Folosește un for că să iterezi prin toată lista și să afișezi;
#● ‘Mașina mea preferată este x’.
#● Fă același lucru cu un for each.
#● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for i in masini:
    print(i)
#for
for x in masini:
    print("masina mea prefera este", x)
#for each
for z, masina in enumerate(masini):
    print("Mașina mea preferată este", masina)
#while
w = 0
while w < len(masini):
    print("Mașina mea preferată este", masini[w])
    w += 1

#2. Aceeași listă:
#Folosește un for else
#În for
#- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
#exceptând primul și ultimul.
#În else:
#- Printează lista.
for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)


#3. Aceeași listă:
#Vine un cumpărător care dorește să cumpere un Mercedes.
#Itereaza prin ea prin modalitatea aleasă de tine.
#Dacă mașina e mercedes:
#Printează ‘am găsit mașina dorită de dvs’
#Ieși din ciclu folosind un cuvânt cheie care face acest lucru
#Altfel:
#Printează ‘Am găsit mașina X. Mai căutam‘
for xd in masini:
    if xd == 'MERCEDES':
        print("Am gasit masina dorita")
        break
    else:
        print(f"Am gasit masina {xd}. Mai cautam")

#4. Aceași listă;
#Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
#excepția Trabant și Lăstun.
#- Dacă mașina e Trabant sau Lăstun:
#Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
#else).
#- Printează S-ar putea să vă placă mașina x.

for xdd in masini:
    if xdd == "LASTUN" or xdd == "TRABANT":
        continue
    else:
        print(f"s-ar putea sa va placa masina {xdd}")

#5. Modernizează parcul de mașini:
#● Crează o listă goală, masini_vechi.
#● Itereaza prin mașini.
#● Când găsesti Lăstun sau Trabant:
#- Salvează aceste mașini în masini_vechi.
#- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#● Printează Modele vechi: x.
#● Modele noi: x.

masini_vechi = []
for xddd in range(len(masini)):
    if masini[xddd] == "LASTUN" or masini[xddd] == "TRABANT":
        masini_vechi.append(masini[xddd])
        masini[xddd] = "Tesla"
        print(f"Modele vechi: {masini_vechi}")
        print(f"Modele noi: {masini}")
'''
'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
'''
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f"Pentru un buget de sub {buget} euro puteti alege masina {masina}")
for masina in pret_masini.keys():
    print(masina)
'''
'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for i in numere:
    if i == 3:
        x += 1
print("numarul de aparaitii este", x)
'''
#8. Aceeași listă:
#● Iterează prin ea
#● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

numere2 = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for z in numere2:
    sum += z
print('suma este', sum)

'''
#9. Aceeași listă:
#● Iterează prin ea.
#● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere3 = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere3[0]
for w in numere3:
    if w > max:
        max = w
print('valoarea maxima este', max)



''''''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
'''
numere4 = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for d in range(len(numere4)):
    if numere4[d] > 0:
        numere4[d] = -numere4[d]
print("noua lista este", numere4)

'''
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
Google.
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
'''
'''
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for nr in alte_numere:
    if nr % 2 == 0:
        numere_pare.append(nr)
    else:
        numere_impare.append(nr)
    if nr >= 0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)
print("nr pare: ",numere_pare)
print("nr impare: ", numere_impare)
print("nr pozitive: ", numere_pozitive)
print("nr negative: ", numere_negative)
'''
#2. Aceeași listă:
#Ordonează crescător lista fară să folosești sort.
#Te poți inspira vizual de aici.
#https://www.youtube.com/watch?v=lyZQPjUT5B4
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for cresc in range(len(alte_numere)):
    index = cresc
    for k in range(cresc+1, len(alte_numere)):
        if alte_numere[index] > alte_numere[k]:
            index = k
    alte_numere[cresc], alte_numere[index] = alte_numere[index], alte_numere[cresc]
print(alte_numere)

#3. Ghicitoare de număr:
#numar_secret = Generați un număr random între 1 și 30
#Numar_ghicit = None
#Folosind un while
#User alege un număr

#Programul îi spune:
#● Nr secret e mai mare
#● Nr secret e mai mic
#● Felicitări! Ai ghicit!
import random

numar_secret = random.randint(1, 30)
numar_ghicit = None

while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Ghiceste un numar intre 1 si 30: "))

    if numar_ghicit < numar_secret:
        print("Numarul secret este mai mare.")
        break

    elif numar_ghicit > numar_secret:
        print("Numarul secret este mai mic.")
        break

    else:
        print("Felicitari! Ai ghicit numarul secret!")
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
n = int(input("Alege un numar: "))

for i in range(1, n+1):
    print(str(i)*i)
'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for rand in tastatura_telefon:
    for cifra in rand:
        print(f'Cifra curentă este {cifra}')