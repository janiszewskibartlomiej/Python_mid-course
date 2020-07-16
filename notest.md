```python
1. metody wirtualne - morzemy deklarowac w klasie abstrakcyjnej aby byly dostepne w podpowiadaniu dla innych klas ktore dziedzicza, 
natomiast trzeba po stworzeniu w klasie anbstrakcyjnej rzucuc wyjatek aby nie bylo dostepu do tej metody w glownej klasie ogolnej/abstrakcyjnej:

 żeby okreslic ze dana klasa jest abstrakcyjna trzeba skorzytsac z biblioteki from abc import ABC, abstractmethod.
 
 obiekt tej klasy ma sluzyc tylko do dziedziczenia metod dla innych  robimy np class nazwa_klasy(ABC):

  @abstractmethod  >>> to jest określenie że nie mozemy tworzyć tej metody 
    def giveVoice(self):
        raise NotImplementedError()
        
2. dziedziczenie wielokrotne > po paru klasach
trzeba projektowac tak aby to bylo zgodne z live czyli np mamy zachowania kaczki >> kaczka  oraz toy >> kaczka toy ktora bedzie dziedzicyc po toy i kaczka. 
wazne jest wydzielenie 
niektorych konstruktorow lub metod do innej klasy np abstrakcyjnej

3. poliformizm - pozwal urzyc tej samej metody nie zaleznie od typu.
w naszym przkladzie duck i duckToy maja te same metody i mozemy ich uzyc nie zaleznie na ktorym obiekcie wolamy.
Pyton potrafi wykonać np print nie zaleznie od obiektu czyli jest poliformiczny

 jest metoda do sprawdzania czy dany obiekt posiada dany atrybut:
 
 lista = [kaczka, zabawka, kaczka, zabawka, Robot("Android")]

for obiekt in lista:
    if hasattr(obiekt, "fly") and hasattr(obiekt, "say"):
        obiekt.say()
        obiekt.fly()

drugi sposob to obsluga wyjatków except AttributeeError - jest lepszym podejsciem jak chcemy sprawdic wiele metod na różnych obiektach, 
bo obslugujemy wszytsko jedym wyjatkiem.

4. podsumowanie dev object
to styl programowania oparty na paradygmatach
- abstrakcja (cos ogulnego - obiekt) np
   liczba naturalna = 5
   dowolny element zbioru liczb naturalnych
   zbiór liczb naturalnych
   > największą anstrakcją w tym przykłądzie biędzie zbiór rzeczywistych
   > zbiór w ogólnie (kolejne poziomy abstrakcji)
- Enkapsulacja
  ukrywanie pewnych danych, ukrywanie imlementacji, rodzajem hermetyzacji jest __zmienna niby protected
- Dziedziczenie - przejmowaniu cech klasy bazowej przez klasy pochodne
- poliformiz - operowanie na wielu obiektach w ten sam sposob

5. dekoratory
class Liczby:
   @staticmethods    >> w takim wypadku nie potrzebujemy obiektu czyli selfa / instancji
   def nazwa():
 pozwala to na odwołanie sie bezpośrednio do metody bez instancji klasy nie trzeba tworzyc obiektu czyli wywołujem Liczby.nazwa  a nie Liczby().nazwa

drugi przykład to:

@classmethod
    def printInformationAboutMe(cls):
        print("Jestem klasową metodą")
        print("wywołaną na rzecz klasy", cls.__name__)
        
   To jest metoda klasowa - z cls - do niej mamy dostep bez instancji jak @staticmethods  czyli Liczby.printInformationAboutMe()
   
   w cls mozemy odwolac się np do nazwy klasy cls.__name__  dostaniemy 'Liczby'
```
