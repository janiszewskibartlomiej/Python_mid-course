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
    
    
   6. setery i getery
   
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
    
    7. zmienne globalne i nielokalne
    
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


8. zamiana zmiennych:

a = 3
b = 5

#najlepszy sposób

a, b = b, a


print("a:",a,"oraz b:",b)

9 True == 1 == 1.0 :

slownik = {True: 'a', 1: 'b', 1.0: 'c'}
print(slownik)

10 kopiowanie list, tupli, slownikow:

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

11 NONE object

# if x is not None:
#     print(x)

jak nie podamy jakiejś wartości to dostaniemy zawsze None

12 wyrażenia listowe

Powielienie pewnych kolejcji jest mozliwe do wykonania za pomoca mnożenia dla wartosci powtarzajacych sie

lista2 = [10]*10
print(lista2)

#lista = [wyrażenie for element in kolekcja]

lista4 = [litera for litera in "Jakiś napis"]
print(lista4)

lista5 = [int(znak) for znak in "0123456"]
print(lista5)

x, y = [int(liczba) for liczba in input("Podaj dwie liczby: ").split()]
print(x*y)

lista3 = [x * y for (x, y) in ([1, 2], [3, 4])]
print(lista3)

lista4 = [[x * y, (x + 1) * (y + 1)] * 3 for x, y in ([a, a + 1] for a in range(5))]
print("lista4:", lista4)

#lista = [wyrażenie for element in kolekcja if warunek]

parzyste = [x*x for x in range(11) if x % 2 == 0]
print(parzyste)

13 inne:

person1, preson2, person3 = "bob", "joe", "merinda"

x = "print(5*5)"
exec(x)

X = "5+5"
print(eval(X)) 


X = "print(5+5)"
eval(X)

X = "print(5+5)"
print(dir(X)) 
help(X.upper) 
 
File = open("test.txt", "w") 
File.write(File.read())

f = open("links.csv", "r")
    f.read()
    print(f.tell())   >> pozycja kursora po odczytaniu znakow
    
f.seek(0,0)
f.read()
    
14 lambda
 
 Ważna funkcjonalność to domknięcia:
 
 def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(100)
print(f(11))
 ----
 
 print((lambda a, b: a ** 3 + 3 * a - b ** 2)(10, 20))

 lista = sorted(range(-3, 12), key=lambda x: x ** 2)
print(lista)

15. Funkcje:

parametry domyślne powinny być jko ostatnie w funkcji np  def dodaj(a, b=0)

można zadeklarować jaki typ ma być przyjmowany i jaki zwracany

def dodaj(a: int = 0, b: int = 0) -> str:
    return str(a + b)

funkcja jest obiektem bo np print(dodaj.__name__)

funkce mozemy zagnierzadzac w sobie jak metody w klasie, natomiast wywolanie nei jest dla nie tak przejrzyste.

def generatorFunkcji(bezZmian, czyUpper):
    def powielTekst(text, ileRazyPowtorzyc=1):
        return text * ileRazyPowtorzyc

    def powielTekstUpper(text: str, ileRazyPowtorzyc=1):
        return text.upper() * ileRazyPowtorzyc

    def powielTekstLower(text: str, ileRazyPowtorzyc=1):
        return text.lower() * ileRazyPowtorzyc

    if bezZmian:
        return powielTekst
    else:
        if czyUpper:
            return powielTekstUpper
        else:
            return powielTekstLower


funkcjaUpper = generatorFunkcji(False, True)

print(funkcjaUpper("abc", 5))

16. obiekt wywolany __call__

jak stworzymy dany obiekt i mam w nim __call__ to bedzie wywolany przy prubie zmiany parametru inicjalizacji obiektu np 

class Func:
    def __init__(self,value):
        self.value = value

    def __call__(self, times):
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value.upper() * times
        else:
            return self.value

liczba = Func(3)
print(liczba(5))    to jest to samo jak print(liczba__call__(5))

17. metody specjalne:

lista1 = [1,2,3]
lista2 = [1,2,3]

lista3 = lista1
lista3.append(4)

print(lista1 is lista3)  #True poniewaz lista3 = lista1   to jest tak naprawde lista3 wskazuje na liste1 - mamy polaczenei do pamieci a nie nowy obiekt

mozemy to ominac poprzez lista3 = lista1[:]  lub skorzystanei z biblioteki copy

class Obiekt:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2



obiekt1 = Obiekt(1, 2)
obiekt2 = Obiekt(1, 2)

print()
print(obiekt1 == obiekt2)  zwruci False

obiekty porownywujemy operatorem is

standardowo porownywanie obiektow kozysta z metody __eq__ ktora mozemy napdissac aby w inny sposob porownywać >> 
    def __eq__(self, other):
        return self.value1 == other.value1 and self.value2 == other.value2
        
 w tym wypadku python bedzie wiedzial jak porownac obiekty poprzez '==' i w tym wypadku print(obiekt1 == obiekt2) #True
 
 == wywoluje >> __eq__  #obiekt1 == obiekt1 >>>to jest >>> obiekt1.__eq__(obiekt2)
 
 __repr__  zwraca techniczne informacje o obiekcie - sluzy do bardziej technicznych prezentacji

__str__ ustawiamy w tej metodzie co ma zwrucic pront od odbiektu

18. przeciarzenie operatorow czyli nadpisywanie metod wbudowanych:

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __add__(self, other):
        zegarek = Clock(self.hours,self.minutes,self.seconds)
        zegarek.addTime(other.hours, other.minutes, other.seconds)
        return zegarek

    def __radd__(self, other):   #  ksiazka1 = Book("abc","dbe",123) ksiazka2 = Book("xyz","zyx",987) ksiazka3 = Book("eee","aaa",333) lista = [ksiazka1,ksiazka2,ksiazka3] print(sum(lista))
        if isinstance(other,Book):
            return self.pages + other.pages
        else:
            return self.pages + other

    def __lt__(self, other):   #  ksiazka1 < ksiazka2:
        if self.pages < other.pages:
            return True
        return False

19 zapisywanie obiektow do pliku

import pickle as pick

zegarek1 = Clock(10,11,12)


try:
    with open("Zegarek.objc",'wb') as file:
        pick.dump(zegarek1,file)
except IOError:
    print("Nie można było utworzyć pliku na dysku")

with open("Zegarek.objc",'rb') as file_pi:
    zegarek = pick.load(file_pi)
    
    
20 unikanie tzw magicznych liczb >> lepiej liczby wydzieli do np stałych w łąściwą nazwą wtedy wiemy co i jak:

NORMAL_RESOLUTION = 600
RESOLUTION_X = 600
RESOLUTION_Y = 600
START_MOUSE_POSITION = -1
SIZE_BOARD = 9

window = sf.RenderWindow(sf.VideoMode(RESOLUTION_X,RESOLUTION_Y),"Kółko i krzyżyk")

21. Asercje

assert jest bardzo wazna poniewaz progrm wywwali sie w miejscu assercji i dostajemy info czemu si ewywalił

   assert 1/(a/b) + 1 >= 0 
    
22. else >> mozna używać w petlach > for i while nie ma przeszód na to

23. import turtle  jest przydatan do pokazania dzialania petli for, uzywana do rysowania

zolw = turtle.Turtle()
zolw.shape('turtle')
colors = ['blue','green','brown','silver','black','purple','pink','gray','red','white']
zolw.color('red','yellow')
for j in range(10):
    zolw.begin_fill()
    for i in range(6):
        zolw.forward(100-10*j)
        zolw.right(120)
    zolw.end_fill()
    zolw.color('red',colors[j])
    zolw.pencolor(colors[j-1])
    zolw.goto(zolw.position()[0]+5,zolw.position()[1]-8)
    zolw.pencolor('red')
turtle.done()

 zolw = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('green')
zolw.shape('turtle')
zolw.color('blue')
size = 10
zolw.penup()
zolw.speed(5)
for i in range(150):
    zolw.stamp()
    size += 1
    zolw.forward(size)
    zolw.right(30)
turtle.done()
    
    
24. import tkinter

import tkinter as t

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

window = t.Tk()
window.title("Różnica silnii")

def closeWindow():
    window.destroy()

t.Label(window,text="Podaj dwie liczby naturalne oddzielone spacją (np. 7 4)").pack(side=t.TOP, padx=10, pady=10)

entry = t.Entry(window, width=10)
entry.pack(side=t.TOP, padx=10, pady=10)

answer = t.Label(window, text="Odpowiedź: ")
answer.pack(side=t.TOP, padx=10, pady=10)

def getValues():
    x, y = [int(x) for x in entry.get().split(' ')]
    result = factorial(x) - factorial(y)
    print(result)
    answer['text'] = "Odpowiedź: " + str(result)


t.Button(window, text="OK", command=getValues).pack(side=t.LEFT)
t.Button(window, text="CLOSE", command=closeWindow).pack(side=t.RIGHT)

window.mainloop()
  
24. documentation in function or methods:

 jezeli pierwsza linijka wewnatrz metody lub funcji jest doc stringiem to jest to traktowane jako dokumentacja, np:
 
 def funkcja(a,b,c):
    """Funkcja funkcja przyjmuje trzy liczby całkowite i zwraca ich sumę
    dalej
    kolejne linie dokumentacji
    """
    return a+b+c
  
  wywołanie dokumentcji >> print(funkcja.__doc__)
  
  
 25. prezentacja danch poprzez matplotlib  -- mozemy sprawdzic porawnosc danych na wykresach
 
import pylab
import math

listaX = []
listaY = []
for i in range(100):
    listaX.append(i/10)
    listaY.append(math.sin(i/10))

pylab.plot(listaX,listaY,'go')
pylab.show()
 
 26 unittest:
 
 tworznie szablonu testu mozn awykonac poprzez najechanie na metode/fukcje + prawy przycisk myszy >> go to >> test

```
