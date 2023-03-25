"""
Recapitulare OOP ( Clase, obiecte, cei 4 piloni OOP)
"""

"""
1. Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""
from abc import ABC, abstractmethod

class AbstractVIdeo(ABC):
    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print("Video is playing")
"""
2. Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""
class Videoclip(AbstractVIdeo):
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration

    def show_details(self):
        print(f'{self.title} are o durata de {self.duration} minute')

v = Videoclip("Titlu",75)

print(v.title)
print(v.duration)
print(v.play())
print(v.show_details())
print("ana")
"""
3. 
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""
class Movie(Videoclip):

def __init__(self, title, duration, genre, director, actors):
    super().__init__(title, duration)
    self.genre = genre
    self.__director = director
    self.actors = actors


def show_details(self):
    super().show_details()
    print(f'Is directed by {self.__director} and the actors are {", ".join(self.actors)}.')


@property
def director(self):
    return self.__director


@director.setter
def director(self, new_director):
    self.__director = new_director


@director.deleter
def director(self):
    del self.__director