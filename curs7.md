# Curs 7: OOP2 (Cei 4 piloni ai OOP-ului + Exceptii)

## 📝 OBIECTIVE
1. Incapsulare
2. Mostenire
3. Abstractizare
4. Polimorfism
5. Exceptii: ce sunt si cum le 'tratam'

## 📌 OOP - Cei 4 piloni ai programarii orientate pe obiect (OOP)

- 4 principii de baza in OOP => clean code
- Acestia sunt: Mostenire, Polimorfism, Incapsulare, Abstractizare.

## 📌 Inheritance - Mostenire

- Mostenire = capacitatea unei clase de a deriva sau a mosteni din alta clasa.
1. Clasa de baza (parent class) = clasa din care se mosteneste.
2. Clasa derivata (child class) = clasa care mosteneste/deriva din clasa parinte.
- Clasa copil va mosteni/va avea acces la toate proprietatile/atributele si metodele din clasa parinte.

```python

# base class / parent class
class Chef:
    
    def __init__(self, experience):
        self.experience = experience

    def make_salad(self):
        print("salad")
        
    def make_fries(self):
        print("fries")
  

# child class - mosteneste din clasa Chef
# se trece intre paranteze numele clasei parinte
class JapaneseChef(Chef):

    def make_sushi(self):
        print("sushi")

        
# child class - mosteneeste din clasa Chef
# se trece intre paranteze numele clasei parinte
class ItalianChef(Chef):
    
    def make_pizza(self):
        print("pizza")

        
chef1 = Chef(2)
chef1.make_salad()
chef1.make_fries()
print(chef1.experience)


chef2 = JapaneseChef(15)
chef2.make_sushi()

chef2.make_salad()
chef2.make_fries()
print(chef2.experience)

chef3 = ItalianChef(23)
chef3.make_pizza()

chef3.make_salad()
chef3.make_fries()
print(chef3.experience)

```

- De asemenea, clasa copil poate si sa aiba proprietati extra si sa extinda comportamentul
clasei de baza (clasei parinte).

```python

class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self):
        print(f"Animal {self.name} has {self.age} years old.")
        
class Dog(Animal):
    
    # Pentru a adauga proprietati noi:
    # 1. Extindem lista de parametrii pe care
    # metoda __init__ ii poate lua.
    # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
    # super(), cu parametrii pentrunecesari pentru clasa parinte.
    def __init__(self, name, age, sound, color):
        super().__init__(name, age)
        self.sound = sound
        self.color = color
    
    # Pentru a extinde metode din clasa parinte:
    # Facem apel la metoda din clasa parinte folosind super()
    def describe(self):
        super().describe()
        print(f"Animal's color is {self.color}.")
        print(f"He says: {self.sound}.")
```

## 📌 Polymorphism - Polimorfism

- Polimorfism = mai multe forme.
- Cand avem 2 sau mai multe functii cu acelasi nume
dar au comportament diferit.

```python
# Exemplu de functie built-in polimorfica
print(len("abc"))
print(len([1, 2, 3, 4]))
```

```python
# Exemplu de functie polimorfica
def add(x, y, z = 0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))
```

```python
# Exemplu de class methods polimorfice
class Romania:
    def language(self):
        print("Romanian")
    
class USA:
    def language(self):
        print("English")

obj_ro = Romania()
obj_usa = USA()

obj_ro.language()
obj_usa.language()
```

## 📌 Abstraction - Abstractizare

- O clasa abstracta contine metode abstracte/ fara corp/ fara implementare
dar si metode cu logica definita.
- O interfata contine doar metode abstracte.
- Aceste clase pot fi mostenite de clasele copii care vor trebui sa scrie
logica metodelor.
- "Dog class implements the Animal interface".
- Clasa parinte e ca o reteta ce trebuie implementata exact asa de catre
toti mostenitorii.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    
    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')

class Cat(Animal):
    
    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
dog = Dog()
```
## 📌 Encapsulation - Encapsulare

- Encapsularea este procesul prin care facem datele si comportamentul
dintr-o clasa, sa nu fie accesibile in exteriorul acesteia.
- Pentru asta, facem datele/atributele si/sau metodele PRIVATE.
- Pentru a face un atribut sau o metoda privata, punem _ _ in fata numelui
atributului/metodei.

```python
class Car:

    def __init__(self, brand):
        self.__brand = brand
        
    def run(self):
        print(f"Please run {self.__brand}")
    

car = Car("Dacia")

# print(car.__brand) -> eroare
car.run()
```

- Mai exista optiunea de PROTECTED ATTRIBUTES/METHODS.
- Pentru a face atributele/metodele protected, punem un singur _
in fata numelui atributului/metodei.
- Atributele/metodele protected pot fi accesate din exterior.
- Protected este doar o conventie prin care putem informa ceilalti programatori
ca atributul/metoda nu ar trebui sa fie folosita in afara clasei.

- Encapsularea se foloseste si pentru a nu aglomera optiunile
utilizatorului, ascunzand atributele.
- In loc sa vada toate atributele si metodele, va vedea doar metodele.
- Astfel, pastram codul clean/curat.

```python
class Car:
    
    __color = 'grey'
    
    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color
    
    def set_color(self, culoarea dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita
```

### @property - ne ajuta sa folosim getter, setter si deleter intr-un mod mai 'Pythonic'

```python
class CarPy:
    
    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.getter
    def color(self):
        print(f"Getter: Culoarea este {self.__color}")
        return self.__color
    
    @color.setter
    def color(self, culoare_noua):
        print(f"Setter: Noua culoare este {culoare_noua}")
        self.__color = culoare_noua

    @color.deleter
    def color(self):
        print(f"Deleter: Am sters culoarea")
        self.__color = None

car2 = CarPy('gray')
print(car2.color)

car2.color = 'red'
print(car2.color)

del car2.color
print(car2.color)
```



