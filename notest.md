```python
1. metody wirtualne - morzemy deklarowac w klasie abstrakcyjnej aby byly dostepne w podpowiadaniu dla innych klas ktore dziedzicza, 
natomiast trzeba po stworzeniu w klasie anbstrakcyjnej rzucuc wyjatek aby nie bylo dostepu do tej metody w glownej klasie ogolnej/abstrakcyjnej:

 żeby okreslic ze dana klasa jest abstrakcyjna trzeba skorzytsac z biblioteki from abc import ABC, abstractmethod.
 
 obiektu tej klasy a ma sluzyc tylko do dziedziczenia metod dla innych zwierzat  robimy np class nazwa_klasy(ABC):

  @abstractmethod  >>> to jest określenie że nie mozemy tworzyć tej metody 
    def giveVoice(self):
        raise NotImplementedError()
        



```