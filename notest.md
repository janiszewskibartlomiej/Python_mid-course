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
   
   w cls mozemy odwolac się np do nazwy klasy cls.__name__  dostaniemy 'Liczby' oraz dużo innych metod.
   

   POLA KLASOWE możeby odwoływać się do nich tak jak do @classmethod  czyli rownież bez tworzenia instacji:
   print(Numbers.numbersSum)  dla klasy 
   
   class Numbers:
    numbersSum = 0
    
    pola klasowe mozemy modyfikowac poprzez cls poniewaz odwoluje sie do klasy i wtedy mozemy :
    
    @classmethod
    def prepareNumbersSum(cls, number):
        cls.numbersSum += number
   
   POLA KLASOWE SĄ BARDZO WAŻNA FUKCJONALNOSCIA, PONIEWAZ PRZETRZYBUJA FAKTYCZNY STAN NIE ZALERZNIE OD ILOSCI INSTANCJI.
   pola klasowe istnije bez instacji co umozliwia odczytywanie danej np liczacej.
   w ramach tworzenie obbiektu/instancji mozemy nadpisac numbersSum = 10, natomiast nie nadpisujemy tym pola metody. wrzucajac np liczby do listy sa one trzymane tylko dla danej instancji natomiast mozemy ozyskac inf  z pola klasowego na temat calej sumy.
   dobre jest to ze kazda instancja posiada swoje odrembe wartosci numberSum.
   
     def addNumberToList(self, number):
        self.numbers.append(number)  >> dodajemy do listy
        Numbers.prepareNumbersSum(number) >> wywolujemy classmethod i wiekszamy stan pola klasy - musimy odwolac sie poprzez nazwe klasy 
        
          @classmethod
    def prepareNumbersSum(cls, number):
        cls.numbersSum += number
        
   ZMIANA W JEDNYM OBIEKCIE numbersSum ZMIENIA TO POLE DLA KAZDEGO INNEGO OBIEKTU I KAZDY OBIEKT MA DOSTE DO TEJ SAMEJ ZMIENNEJ POLA KLASOWEGO
   
   możemy w __init__ miec dostep do pola klasowego poprzez cls i rowniez selfa dzieki temu np kazde dodnei marki samochodu zmienia polek lasowe na +1:
   
   class Car:
    howManyCars = 0

    @classmethod
    def __init__(cls, self, brand):
        self.brand = brand
        cls.howManyCars += 1
        
    W takim wypadku tworzenie obiektu jest troche inne ponieważ musimy podac nazwe cls >> samochod1 = Car(Car,"inna")
    
    
    POLA KLASOWE BARDZO PRZYDATNE ABY GRUPOWAC DANE WZGLEDEM WSZYSTKICH OBIEKTOW
    
  obiekt = Foo()  >> obiekt
  obiekt.pole = 5   >> zmienna statyczna instncyjna/obiektu Foo()
    
    
   #### 6. setery i getery
   
       def __init__(self):
        self.__a = 5   >> ustawiamy na protected dzieki temu nikt w latwy sposob nie bedzie mial dostepu do tej zmiennej. Wtedy powinismy ustawic get do pobierania i 
        wykonujemy to z @property   a modyfikacje wszelkie na zmiennej  robimy metoda @get_a.setter

    @property
    def get_a(self):
        return self.__a

    @get_a.setter
    def set_a(self,value):
        if value < 0:
            self.__a = 0
        else:
            self.__a = value
            
    mozeby rowniez ustawic property na def a  >> w takim wypadku jak ktos przypisze Obiekt().a = -11 to utuchomi metode a a nie bedzie to przypisanei do pola statycznego
    
    #### 7. zmienne globalne i nielokalne
    
    naezy pamietac ze funkcje ajak i klasy mozna w sobie zagniezdzac.
    
    def f(x):
    print("Funkcja f")
    def g(y):
        
        x = 7   >> zmienna lokakna dlatego nie jest dostepna dla print(x)
        print("Dostałem", y)
        print(x) >> 3
    x += 1
    g(x)
    print(x)
    
    f(2)
-------------
x = 3   >> zmienna globalna

def f():
    global x  >> odwolanie do zmiennej globalnej
    x = 2
    print(x)
    
f() # dostaniemy 2
print(x)
mamy efekt przeslaniania nazw i jezeli chcemy zmienic x globalny na 2 trzeba w funkcji podac ze chodzi nam o x ktory istnije >> global x  wtedy print(x) >> 2
slowo global mowi ze jest w pierwszej lini dstepne a nie we wcieciu. >> bez zagniezdzien

nonlocal sprawdza zmienne w bloku nad wywolaniem


zmienna = 10
def a():
    zmienna = 11
    def b():
        nonlocal zmienna  >> zmieniamy 11 na 12
        
        3 jezeli chcemy zmienic zmienna (10)  na 12 musimy napisac global zmienna 
        zmienna = 12
    b()
    print(zmienna)

a()
print(zmienna)


#### 8. zamiana zmiennych:

a = 3
b = 5

#najlepszy sposób

a, b = b, a


print("a:",a,"oraz b:",b)

#### 9 True == 1 == 1.0 :

slownik = {True: 'a', 1: 'b', 1.0: 'c'}
print(slownik)

#### 10 kopiowanie list, tupli, slownikow:

x = [1,2,3]
y = list(x) >> ten sposób utworzymy nowa na podstawie x   jak zrobimy y = x to tworzymy jedynie polaczenie [twozymy wskaznik do tej samej zmiennej] 
do x i jak cos zmienimy w x to bedzie w y 
x.append(4)
print(y)

przy obiektach  musimy:

import copy

class MyClass:
    def __init__(self):
        self.a = 0

obiekt = MyClass()
obiekt2 = copy.copy(obiekt)   >> w ten sposub tworzymy kopie niezalezne od 1 obiektu















```
