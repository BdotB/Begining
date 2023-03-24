
# Exerciții RECOMANDATE - grad de dificultate: Ușor

# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link video: https://www.itfactory.ro/8174437-intro-in-programare/

# EXERCITII OBLIGATORII

# 1.
# a. Declara o lista, note_muzicale, in care sa pui do re mi etc pana la do.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# b. Afiseaz-o.
print(note_muzicale)
# c. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata).
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
# d. Aplica o metoda pe lista care banuiesti ca face același lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat)
# si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială.
note_muzicale.reverse()
print(note_muzicale)
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
# sau sa o salvezi intr-o listă nouă.
# Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări.
# Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.
# e. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
note_do = note_muzicale.count('do')
print(note_do)
# 2. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante prin care sa le unesti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
lista1.extend(lista2)
print(lista3)
print(lista1)
# 3.
# a. Sorteaza si afiseaza lista generata la exercitiul anterior.
lista1.sort()
print(lista1)
# b. Sterge numarul 0 din lista folosind o functie/metoda ajutatoare si apoi afiseaza din nou lista.
lista1.remove(0)
print(lista1)
# 4. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# Lista este goala (IF)
# Lista nu este goala (ELSE)
if len(lista1) == 0:
    print("lista este goala ")
else:
    print("lista nu este goala ")

# 5. Foloseste o functie care sa goleasca lista de la exercitiul 3/ sa o transforme in lista goala.
lista1.clear()
print(lista1)
# 6. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala.
if len(lista1) == 0:
    print("lista este goala ")
else:
    print("lista nu este goala ")
# 7. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},
# foloseste o functie ca sa afisezi Elevii (cheile).
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for elev in dict1:
    print(elev)
# 8. Printeaza cei 3 elevi din dictionarul de la exercitiul 7 si respectiv notele lor.
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie
    nota = dict1[elev]
    print(f"Elevul {elev} a luat nota {nota} ")

# 9. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# Modifica nota lui Dorel in 6
# Printeaza nota lui dupa modificare
dict1['Dorel'] = 6
print(dict1)
print("Dorel a luat: ", dict1['Dorel'])


# 10. Imagineaza-ti ca Gigel se transfera din clasa.
# a. Cauta o functie care sa il stearga
# b. Vine un coleg nou.
# Adaugati-l in lista pe Ionica, cu nota 9.
# c. Printati dictionarul cu noii elevi

del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9
print(dict1)
# EXERCITII OPTIONALE

# 1. Ne imaginam o echipa de fotbal.
# a. Declara o lista cu 5 jucatori (numele lor) care sunt pe teren: lista_jucatori_teren.
lista_jucatori_teren = ['juc1', 'juc2', 'juc3', 'juc4', 'juc5']
# b. Declara o lista cu 5 jucatori (numele lor) care sunt de rezerva: lista_jucatori_rezerva.
lista_jucatori_rezerva = ['rez1', 'rez2', 'rez3', 'rez4', 'rez5']
# c. Declara o lista goala cu jucatori care sunt scosi de pe teren: lista_jucatori_scosi.
lista_jucatori_scosi = []
# d. Declara constanta SCHIMBARI_MAXIME = 3.
SCHIMBARI_MAXIME = 3
# e. Declara o variabila schimbari_efectuate. (Joaca-te cu valori diferite sa vezi cum curg datele prin cod).
schimbari_efectuate = 1
# f. Citeste numele a doi jucatori de la tastatura, salveaza-le numele in variabilele x si y.
x = input('Introduceti numele jucatorului: ')
y = input('Introduceti numele celui de-al 2-lea jucator: ')
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
if x in lista_jucatori_teren and schimbari_efectuate < SCHIMBARI_MAXIME:
    #Efectuam urmatoarea schimbare daca jucatorul y e in lista de rezerve si nu exista in lista de teren:
        lista_jucatori_rezerva.append(y)
if y in lista_jucatori_rezerva and y not in lista_jucatori_teren:
        # Stergem jucatorul x din lista de teren si il adaugam in lista de jucatori scosi
        lista_jucatori_teren.remove(x)
        lista_jucatori_scosi.append(x)
        # Adaugam jucatorul y in lista de jucatori pe teren si il scoatem din lista de jucatori de rezerva
        lista_jucatori_teren.append(y)
        lista_jucatori_rezerva.remove(y)
        # Crestem numarul de schimbari_efectuate (hint: operator de atribuire)
        schimbari_efectuate += 1
        # Afisam pe ecran: a intrat y, a iesit x. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)
        print(f"A intrat {y}, a iesit {x}. Mai aveti {SCHIMBARI_MAXIME - schimbari_efectuate} schimbari.")
#   Daca jucatorul y este pe teren deja:
elif y in lista_jucatori_teren:
        # Afisam ‘nu se poate efectua schimbarea deoarece jucatorul y e deja pe teren teren’
        print(f"Nu se poate efectua schimbarea deoarece jucatorul {y} este deja pe teren.")
        # Afisam si nr schimbari: ‘mai aveti z schimbari’.
        print(f"Mai aveti {SCHIMBARI_MAXIME - schimbari_efectuate} schimbari.")
else:
    print('Nu se poate')