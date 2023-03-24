'''
y_str = 'povesteppppppp'
# print(my_str[:2]) #po

# print(my_str.find('e'))
my_str2 = '     poveste    '
print(my_str2)
print(my_str2.strip()) # eliminam spatiile de la inceput si final
print(my_str.strip('p'))

# LISTE

list1 = ["abc", 34, True, 40]
print(list1[0])

# Exemplu de modificare a unui element dintr-o lista
numbers = [1, 2, 3, 4, 5, 5, 5]
numbers[2] = 7 # modificam elementul de la indexul 2
print(numbers)
print(len(numbers))
# Output: [1, 2, 7, 4, 5]

lista_cumparaturi = ['rosii', 'paine', 'lapte']
print(type(lista_cumparaturi))
print(len(lista_cumparaturi))
print(lista_cumparaturi[0])
culori_preferate = ['rosu', 'galben', 'mov']
contacte = ['0722345678', '0721549888', '0765332967']

# 1.
# a. Defineste o lista cu 3 elemente.
list1 = ['a', 'b' , 'c']
# b. Este lista o structura de date ordonata? De ce da/nu?
#da
# c. Acceseaza al doilea element din lista si afiseaza-l.
print(list1[1])
# d. Afiseaza lungimea listei.
print(len(list1))

filme_preferate = ['Film1', 'Film2', 'Film3']
# b. Inverseaza lista folosind slicing. (ca la string)
print(filme_preferate[::-1])
# c. Folosind if, verifica daca lista este goala sau nu,
lista_goala= []
if not filme_preferate :
    print('Lista este goala')
else:
    print('Lista nu este goala')
# si afiseaza un mesaj corespunzator pentru fiecare situatie.
'''
'''
# 3. Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# a. Verifica tipul structurii de date dat.
print(type(cifre))
# b. Accesand metodele de pe lista, sorteaza lista cifre.
cifre.sort()
print(cifre)
# c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
if 9 in cifre:
    print("9 este in lista")
else:
    print("9 nu este in lista")
'''
'''
# 4. Cum se adauga un elemente intr-o lista.

#cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
#cifre.append(9)   # adauga cifra 9 in lista la finalul listei
#print(cifre)
#cifre.insert(0, 9)
#print(cifre)

# 5 DICTIONARE

# o lista
contacte = ['0722345678', '0721549888', '0765332967']

my_dict = {
    'nume_produs': 'produs_1',
    'pret': 23.00,
    'in_stoc': False
}

contacte_dict = {
    'Ana': '0722345678',
    'Marius': '0721549888',
    'Maria': '0765332967'
}

# Exemplu de adaugare a unei perechi cheie-valoare
# intr-un dictionar
person = {
    "name": "John",
    "age": 30,
    "city": ["New York", "Los Angeles"],
    "occupation": "teacher"
}
print(person)
# Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'teacher'}

# print(person['name'])

# adaugare element nou in dictionar
# person['salary'] = 3000.00
# print(person)

# modifca un element in dictionar
# person['age'] = 31
# print(person)

# stergem un element din dictionar
# del person['city'], person['salary'] # stergem mai multe key:value deodata
# del person['city']
# print(person)

cities = person['city']
print(cities)

cities.remove('Los Angeles')
print(cities)

print(person)
''''''
# 1.
# a. Defineste un dictionar, numit student1, cu urmatoarele chei:
# nume, prenume, varsta, an_studiu, facultate, medie. Valorile le alegi tu.
student1 = {
    'nume': 'pop',
    'prenume': 'maria',
    'varsta': 20,
    'an_studiu' : 2023,
    'facultate': 'utc',
    'medie': 9.45
}
# b. Afiseaza lungimea dictionarului.
print(len(student1))
# c. Printeaza prenumele studentului.
print(student1['nume'])
# d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
student1['tara'] = "romania"
print(student1)
# e. Verifica daca dictionarul contine cheia oras.
if student1.get('oras', False):
    print("da")
else:
    print("no")
    '''
# 2.
# a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
# ingrediente, timp prepapare.
nume = input("Introdu nume reteta ")
ingrediente = input("Introdu ingrediente ")
timp_preparere = float(input("Introdu timp "))
# b. Salveaza datele citite intr-un dictionar.
reteta = {
    "nume_reteta" = nume,
    "ingrediente" = ingredienete,
    "timp" = timp_preparere,
}
# c. Actualizeaza numele retetei, scriind-ul cu litere mari.