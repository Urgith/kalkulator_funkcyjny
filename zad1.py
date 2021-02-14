'''
Program ten jest graficznym interfejsem do rysowania wykresów. Posiada on:
  -interfejs do rysowania oraz zapisu wykresu funkcji
  -narzędzie do wprowadzania elementów wzoru
  -złożony kalkulator
  -pomoc, opisującą jak należy korzystać z programu
'''
from functools import partial
''' funkcja partial z modułu functools ułatwia nam korzystanie z komendy dla przycisku'''
from tkinter.ttk import *
''' importujemy po to aby wprowadzić Combobox'''
from tkinter import *
''' moduł odpowiedzialny za tworzenie GUI będącego najważniejszą częścią tego programu'''
from numpy import *
''' moduł odpowiedzialny za obliczenia macierzowe oraz funkcje i zmienne matematyczne'''
import pylab
''' moduł pozwalający nam na rysowanie wykresów funkcji'''
import os
''' moduł pozwalający nam operować na plikach i ścieżkach'''
import pydoc
''' moduł tworzący dokumentację'''


class Interfejs():
  '''
  Klasa interfejsu głównego, w którym możemy:
    -wprowadzić wzór funkcji
    -wprowadzić parametry wzoru takie jak:
      -zakresy osi
      -nazwy osi
      -nazwa wykresu
      -dokładność wykresu
      -kolory funkcji
      -legenda, siatka wykresu
	-zapisać wykres
    -ustalić ścieżkę i nazwę pliku jako który chcemy zapisać wykres
    -uzyskać informacje o błędach
    -otworzyć menu pomocy, kalkulatora oraz narzędzia do wprowadzania elementów wzoru
    -wyjść z programu
  '''
  def __init__(self):
    ''' Tworzymy wszystkie wcześniej wspomniane elementy interfejsu'''
    self.root = Tk()

    Interfejs.polozenie(self, 'Rysowanie wykresów', '1050x600+50+0', 'green')
    Interfejs.napis(self, 645, 5, 90, 25, 'Wzór funkcji:')
    Interfejs.napis(self, 645, 40, 100, 25, 'Zakresy osi X:')
    Interfejs.napis(self, 750, 40, 40, 25, 'dolny')
    Interfejs.napis(self, 900, 40, 40, 25, 'górny')
    Interfejs.napis(self, 645, 75, 100, 25, 'Zakresy osi Y:')
    Interfejs.napis(self, 750, 75, 40, 25, 'dolny')
    Interfejs.napis(self, 900, 75, 40, 25, 'górny')
    Interfejs.napis(self, 645, 110, 90, 25, 'Nazwa osi X:')
    Interfejs.napis(self, 645, 145, 90, 25, 'Nazwa osi Y:')
    Interfejs.napis(self, 645, 180, 114, 25, 'Nazwa wykresu:')
    Interfejs.napis(self, 645, 250, 50, 25, 'Kolory:')
    Interfejs.napis(self, 645, 215, 110, 25, 'Ilość pomiarów:')
    Interfejs.napis(self, 670, 395, 65, 20, 'Legenda')
    Interfejs.napis(self, 790, 395, 50, 20, 'Siatka')
    Interfejs.napis(self, 645, 445, 116, 25, 'Ścieżka do pliku:')
    Interfejs.napis(self, 645, 480, 90, 25, 'Nazwa pliku:')
    Interfejs.napis(self, 10, 550, 50, 30, 'Błędy:')

    self.wzor = Interfejs.wejscie(self, 740, 5, 305, 25)
    self.zakresXdolny = Interfejs.wejscie(self, 795, 40, 100, 25)
    self.zakresXgorny = Interfejs.wejscie(self, 945, 40, 100, 25)
    self.zakresYdolny = Interfejs.wejscie(self, 795, 75, 100, 25)
    self.zakresYgorny = Interfejs.wejscie(self, 945, 75, 100, 25)
    self.nazwaX = Interfejs.wejscie(self, 765, 110, 280, 25)
    self.nazwaY = Interfejs.wejscie(self, 765, 145, 280, 25)
    self.nazwa_wykres = Interfejs.wejscie(self,765, 180, 280, 25)
    self.dokladnosc = Interfejs.wejscie(self,765, 215, 280, 25)
    self.kolory = Interfejs.wejscie(self, 765, 250, 280, 25)
    self.sciezka = Interfejs.wejscie(self, 765, 445, 280, 25)
    self.plik = Interfejs.wejscie(self, 765, 480, 280, 25)
    self.bledy = Interfejs.wejscie(self, 70, 550, 550, 30)

    Interfejs.przycisk(self, 920, 560, 120, 30, 'Zakończ program', koniec)
    Interfejs.przycisk(self, 650, 565, 60, 25, 'Włącz', partial(Kalkulator, self))
    Interfejs.przycisk(self, 930, 385, 100, 40, 'Rysuj', partial(Interfejs.rysowanie, self))
    Interfejs.przycisk(self, 780, 515, 100, 40, 'Zapisz', partial(Wykres.zapis, self))
    Interfejs.przycisk(self, 300, 5, 40, 40, '?', Pomoc)

    Interfejs.przycisk(self, 660, 285, 105, 25, 'czerwony', partial(wpisywanie, self.kolory, 'red'), 'red')
    Interfejs.przycisk(self, 770, 285, 105, 25, 'pomarańczowy', partial(wpisywanie, self.kolory, 'orange'), 'orange')
    Interfejs.przycisk(self, 880, 285, 105, 25, 'żółty', partial(wpisywanie, self.kolory, 'yellow'), 'yellow')
    Interfejs.przycisk(self, 660, 315, 105, 25, 'niebieski', partial(wpisywanie, self.kolory, 'blue'), 'blue')
    Interfejs.przycisk(self, 770, 315, 105, 25, 'zielony', partial(wpisywanie, self.kolory, 'green'), 'green')
    Interfejs.przycisk(self, 880, 315, 105, 25, 'błękitny', partial(wpisywanie, self.kolory, 'cyan'), 'cyan')
    Interfejs.przycisk(self, 660, 345, 105, 25, 'fioletowy', partial(wpisywanie, self.kolory, 'purple'), 'purple')
    Interfejs.przycisk(self, 770, 345, 105, 25, 'różowy', partial(wpisywanie, self.kolory, 'magenta'), 'magenta')
    Interfejs.przycisk(self, 880, 345, 105, 25, 'szary', partial(wpisywanie, self.kolory, 'gray'), 'gray')
    Interfejs.przycisk(self, 1005, 285, 25, 25, ';', partial(wpisywanie, self.kolory,';'), 'white')
    Interfejs.przycisk(self, 1005, 315, 25, 25, '←', partial(delete, self.kolory), 'white')
    Interfejs.przycisk(self, 1005, 345, 25, 25, 'C', partial(clear, self.kolory), 'white')

    self.legenda = Interfejs.znaczek(self, 730, 395, 20)
    self.siatka = Interfejs.znaczek(self, 835, 395, 20)
    self.zmiana = Interfejs.wybor(self, 715, 565, 90, 25)
    self.canvas = Interfejs.wykres(self)

    self.root.mainloop()

  def polozenie(self, nazwa, wymiary, kolor):
    ''' funkcja pobierająca obiekt, nazwę, wymiary oraz kolor ustawiająca wszystkie te 3 cechy obiektu'''
    self.root.title(nazwa)
    self.root.geometry(wymiary)
    self.root.configure(background=kolor)

  def przycisk(self, x, y, w, h, napis, f, color='lightCyan3'):
    ''' funkcja pobierająca obiekt, współrzędne X i Y  oraz wymiary, a takze napis, funkcję wywoływaną przez kliknięcie przycisku i kolor-domyślnie jasny niebieski zwracająca przycisk z wymienionymi cechami'''
    return Button(self.root, text=napis, command=f, bg=color).place(x=x, y=y, width=w, height=h)

  def wejscie(self, x, y, w, h):
    ''' funkcja pobierająca obiekt, współrzędne X i Y  oraz wymiary, zwraca pole do wpisywania'''
    wejscie = Entry(self.root, width=15)
    wejscie.place(x=x, y=y, width=w, height=h)
    return wejscie

  def znaczek(self, x, y, s):
    ''' funkcja pobierająca obiekt, współrzędne X i Y  oraz wymiary(s,s), zaznacznik oraz jego wartość'''
    var1 = BooleanVar()
    checkbutton = Checkbutton(self.root, var=var1)
    checkbutton.place(x=x, y=y, width=s, height=s)
    return checkbutton, var1

  def napis(self, x, y, w, h, napis):
    ''' funkcja pobierająca obiekt, współrzędne X i Y  oraz wymiary, a takze napis, zwracająca napis z wymienionymi cechami'''
    return Label(self.root, text=napis).place(x=x, y=y, width=w, height=h)

  def wykres(self):
    ''' funkcja pobierająca obiekt, zwracająca płótno o określonych parametrach'''
    canvas = Canvas(self.root, width=640, height=480, bg='black')
    canvas.pack()
    canvas.place(x=0, y=50)
    return canvas

  def wybor(self, x, y, w, h):
    ''' funkcja pobierająca obiekt, współrzędne X i Y  oraz wymiary, zwracająca pole do wyboru czy ma być uruchomiony kalkulator, czy narzędzie do wprowadzania elementów wzoru, domyślnie wybrane jest narzędzie'''
    combobox = Combobox(self.root, values=('Narzędzie', 'Kalkulator'))
    combobox.place(x=x, y=y, width=w, height=h)
    combobox.current(0)
    return combobox

  def rysowanie(self):
    ''' funkcjapobierająca obiekt, inicjalizująca nowy obiek (wykres)'''
    self.bledy.delete(0, END)
    self.wykres = Wykres(self)


class Wykres():
  '''
  Klasa wykresu; rysująca, konfigurująca i zapisująca wykres
  '''
  def __init__(self, interfejs):
    '''
    Tworzymy wykres, jego nazwę, a także opisy osi X oraz Y
    Pobieramy zakresy osi oraz dokładność
    Pobieramy kolory oraz wzór funkcji i rysujemy funkcję
    Zapisujemy wykres
    '''
    global wykres

    self.sprawdzanie = True
    self.fig, self.ax = pylab.subplots()
    wykres = self.fig

    pylab.title(entry_get(interfejs.nazwa_wykres))
    pylab.xlabel(entry_get(interfejs.nazwaX))
    pylab.ylabel(entry_get(interfejs.nazwaY))

    try:
      a = float(entry_get(interfejs.zakresXdolny))
    except:
      a = -10
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie wprowadzono wszystkich zakresów. ')

    try:
      b = float(entry_get(interfejs.zakresXgorny))
    except:
      b = 20
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie wprowadzono wszystkich zakresów. ')

    try:
      c = float(entry_get(interfejs.zakresYdolny))
    except:
      c = -10
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie wprowadzono wszystkich zakresów. ')

    try:
      d = float(entry_get(interfejs.zakresYgorny))
    except:
      d = 20
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie wprowadzono wszystkich zakresów. ')

    try:
      self.e = int(entry_get(interfejs.dokladnosc))
      if self.e > 10000:
        self.e = 10000
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'Maksymalna dokładność to 10000.')

      if self.e < 2:
        self.e = 2
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'Minimalna dokładność to 1.')

    except:
      self.e = 1000
      interfejs.bledy.insert(0, 'Nie wprowadzono dokładności rysunku. ')

    if a < b and c < d:
      pylab.axis([a, b, c, d])
      x = pylab.linspace(a, b, self.e)

    else:
      pylab.axis([-10, 20, -10, 20])
      x = pylab.linspace(-10, 20, self.e)

    self.lista_kolorow = Wykres.wzor(interfejs)[1]
    if not self.lista_kolorow[0]:
      self.lista_kolorow[0] = 'blue'

    if Wykres.wzor(interfejs)[0][0]:
      if len(Wykres.wzor(interfejs)[0]) > len(self.lista_kolorow):
        for i in range(len(Wykres.wzor(interfejs)[0]) - len(self.lista_kolorow)):
          self.lista_kolorow.append(self.lista_kolorow[i%len(Wykres.wzor(interfejs)[1])])

      try:
        for i, wykresik in enumerate(Wykres.wzor(interfejs)[0]):
          try:
            pylab.plot(x, eval(wykresik), color=self.lista_kolorow[i], label=wykresik)
          except:
            pylab.plot(x, eval(wykresik)*ones(shape=[1000,]), color=self.lista_kolorow[i], label=wykresik)

      except:
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'We wzorze funkcji została wprowadzona nieznana komenda, nic nie narysowano.')
        self.sprawdzanie = False

    else:
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie wprowadzono żadnej funkcji, nic nie narysowano.')
      self.sprawdzanie = False

    if interfejs.legenda[1].get():
      self.ax.legend()

    if interfejs.siatka[1].get():
      pylab.grid(True)
      pylab.axhline(0, color=(0,0,0), linewidth=0.7)
      pylab.axvline(0, color=(0,0,0), linewidth=0.7)

    Wykres.zapis_canvas(interfejs)
    try:
      if self.sprawdzanie:
        photo = PhotoImage(file='ostatni_wykres.png')
        interfejs.canvas.create_image(0, 0, image=photo, anchor=NW)
    except: pass

    interfejs.root.mainloop()

  def zapis(interfejs):
    ''' funkcja  zapisująca wykres w podanym przez użytkownika pliku i katalogu'''
    global wykres

    interfejs.bledy.delete(0, END)
    Wykres.zmiana_folderu(interfejs)

    if entry_get(interfejs.plik):
      try:
        wykres.savefig(entry_get(interfejs.plik) + '.jpg')
      except:
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'Najpierw musisz narysować wykres.')

    else:
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'Wprowadź nazwę pliku.')

  def zapis_canvas(self):
    ''' funkcja zapisująca wykres jako plik, informuje nas o błędzie, jeżeli coś poszło nie tak'''
    global wykres
    try:
      wykres.savefig('ostatni_wykres.png')

    except ValueError:
      self.bledy.delete(0, END)
      self.bledy.insert(0, 'Wprowadzono błędne kolory.')

  def zmiana_folderu(interfejs):
    ''' funkcja zmieniająca aktualny katalog na katalog podany przez użytkownika, informuje nas o błędzie, jeżeli coś poszło nie tak'''
    try:
      os.chdir(entry_get(interfejs.sciezka))
    except:
      interfejs.bledy.delete(0, END)

      if not entry_get(interfejs.sciezka):
        interfejs.bledy.insert(0, 'Nie wprowadzono żadnej ścieżki, plik zapisano do aktualnego katalogu.')
      else:
        interfejs.bledy.insert(0, 'Podana ścieżka do katalogu nie istnieje.')

  def wzor(interfejs):
    ''' funkcja zwracająca wszystkie wzory i kolory wprowadzone w interfejsie głównym'''
    wzory = entry_get(interfejs.wzor).split(';')
    kolory = entry_get(interfejs.kolory).split(';')
    return wzory, kolory


class Kalkulator(Interfejs):
  '''
  Klasa Interfejsu Kalkulatora / Narzędzia do wprowadzania elementów wzoru dziedzicząca po Interfejsie, w interfejsie tej klasy możemy:
      -wprowadzać cyfry do Kalkulatora/Narzędzia
      -wprowadzać podstawowe operatory takie jak + - * / do Kalkulatora/Narzędzia
      -wprowadzać operatory pomocnicze takie jak ) ( . ; do Kalkulatora/Narzędzia
      -usuwać wpisaną zawartość (backspace), czyścić całą zawartość z Kalkulatora/Narzędzia
      -korzystać z funkcji trygonometrycznych i hiperbolicznych w Kalkulatorze/Narzędziu
      -wprowadzać zmienne e pi phi oraz zmienną funkcji x do Kalkulatora/Narzędzia
      -obliczać ln log2 i log10, a także pierwiastek, kwadrat (drugą potęgę), funkcję e^, wartość bezwzględną, część całkowitą, czy najzwyklejszą potęgę w Kalkulatora/Narzędzia
  Sam kalkulator oferuje nam także obliczenie wyniku, natomiast narzędzie tylko wprowadza elementy wykresu
  '''
  def __init__(self, interfejs):
    ''' Tworzymy wszystkie wcześniej wspomniane elementy interfejsu'''
    global phi

    self.root = Tk()
    self.wynik = Kalkulator.wejscie(self, 5, 380, 300, 35)
    self.wynik_obliczen = Kalkulator.wejscie(self, 45, 420, 265, 35)

    phi = (1 + 5**0.5)/2

    if interfejs.zmiana.get() == 'Narzędzie':
      Kalkulator.opcja(self, interfejs.wzor, interfejs, 'Narzędzie')
    else: Kalkulator.opcja(self, self.wynik, interfejs, 'Kalkulator')

    self.przycisk_wynik = Kalkulator.przycisk(self, 5, 420, 35, 35, '=', partial(Kalkulator.oblicz, self, self.wynik, interfejs), 'orange')

  def opcja(self, wpisywanie_do, interfejs, nazwa):
    ''' funkcja rysująca wszystkie przyciski oprócz znaku = dla Narzędzia i wszystkie przyciski oprócz x oraz ; dla Kalkulatora, pobierająca obiekt Kalkulatora bądź Narzędzia oraz nazwę Kalkulator/Narzędzie'''
    self.przycisk1 = Kalkulator.przycisk(self, 5, 10, 40, 40, '1', partial(wpisywanie, wpisywanie_do, '1'), 'cyan')
    self.przycisk2 = Kalkulator.przycisk(self, 50, 10, 40, 40, '2', partial(wpisywanie, wpisywanie_do, '2'), 'cyan')
    self.przycisk3 = Kalkulator.przycisk(self, 95, 10, 40, 40, '3', partial(wpisywanie, wpisywanie_do, '3'), 'cyan')
    self.przycisk4 = Kalkulator.przycisk(self, 5, 60, 40, 40, '4', partial(wpisywanie, wpisywanie_do, '4'), 'cyan')
    self.przycisk5 = Kalkulator.przycisk(self, 50, 60, 40, 40, '5', partial(wpisywanie, wpisywanie_do, '5'), 'cyan')
    self.przycisk6 = Kalkulator.przycisk(self, 95, 60, 40, 40, '6', partial(wpisywanie, wpisywanie_do, '6'), 'cyan')
    self.przycisk7 = Kalkulator.przycisk(self, 5, 110, 40, 40, '7', partial(wpisywanie, wpisywanie_do, '7'), 'cyan')
    self.przycisk8 = Kalkulator.przycisk(self, 50, 110, 40, 40, '8', partial(wpisywanie, wpisywanie_do, '8'), 'cyan')
    self.przycisk9 = Kalkulator.przycisk(self, 95, 110, 40, 40, '9', partial(wpisywanie, wpisywanie_do, '9'), 'cyan')
    self.przycisk0 = Kalkulator.przycisk(self, 50, 160, 40, 40, '0', partial(wpisywanie, wpisywanie_do, '0'), 'cyan')
    self.przycisk_plus = Kalkulator.przycisk(self, 140, 10, 40, 40, '+', partial(wpisywanie, wpisywanie_do, '+'), 'cyan')
    self.przycisk_minus = Kalkulator.przycisk(self, 140, 60, 40, 40, '-', partial(wpisywanie, wpisywanie_do, '-'), 'cyan')
    self.przycisk_razy = Kalkulator.przycisk(self, 140, 110, 40, 40, '*', partial(wpisywanie, wpisywanie_do, '*'), 'cyan')
    self.przycisk_dziel = Kalkulator.przycisk(self, 140, 160, 40, 40, '/', partial(wpisywanie, wpisywanie_do, '/'), 'cyan')
    self.przycisk_sin = Kalkulator.przycisk(self, 190, 10, 50, 40, 'sin', partial(wpisywanie, wpisywanie_do, 'sin'), 'light sky blue')
    self.przycisk_cos = Kalkulator.przycisk(self, 250, 10, 50, 40, 'cos', partial(wpisywanie, wpisywanie_do, 'cos'), 'light sky blue')
    self.przycisk_tan = Kalkulator.przycisk(self, 250, 60, 50, 40, 'tan', partial(wpisywanie, wpisywanie_do, 'tan'), 'light sky blue')
    self.przycisk_arcsin = Kalkulator.przycisk(self, 190, 110, 50, 40, 'arcsin', partial(wpisywanie, wpisywanie_do, 'arcsin'), 'light sky blue')
    self.przycisk_arccos = Kalkulator.przycisk(self, 250, 110, 50, 40, 'arccos', partial(wpisywanie, wpisywanie_do, 'arccos'), 'light sky blue')
    self.przycisk_arctan = Kalkulator.przycisk(self, 190, 60, 50, 40, 'arctan', partial(wpisywanie, wpisywanie_do, 'arctan'), 'light sky blue')
    self.przycisk_nawias1 = Kalkulator.przycisk(self, 5, 160, 40, 40, '(', partial(wpisywanie, wpisywanie_do, '('), 'cyan')
    self.przycisk_nawias2 = Kalkulator.przycisk(self, 95, 160, 40, 40, ')', partial(wpisywanie, wpisywanie_do, ')'), 'cyan')
    self.przycisk_kropka = Kalkulator.przycisk(self, 5, 210, 40, 40, '.', partial(wpisywanie, wpisywanie_do, '.'), 'cyan')
    self.przycisk_pi = Kalkulator.przycisk(self, 260, 175, 40, 40, 'pi', partial(wpisywanie, wpisywanie_do, 'pi'), 'dodger blue')
    self.przycisk_e = Kalkulator.przycisk(self, 210, 225, 40, 40, 'e', partial(wpisywanie, wpisywanie_do, 'e'), 'dodger blue')
    self.przycisk_floor = Kalkulator.przycisk(self, 260, 225, 40, 40, 'phi', partial(wpisywanie, wpisywanie_do, 'phi'), 'dodger blue')
    self.przycisk_ln = Kalkulator.przycisk(self, 10, 275, 40, 40, 'ln', partial(wpisywanie, wpisywanie_do, 'log'), 'aquamarine')
    self.przycisk_log2 = Kalkulator.przycisk(self, 60, 275, 40, 40, 'log2', partial(wpisywanie, wpisywanie_do, 'log2'), 'aquamarine')
    self.przycisk_log10 = Kalkulator.przycisk(self, 110, 275, 40, 40, 'log10', partial(wpisywanie, wpisywanie_do, 'log10'), 'aquamarine')
    self.przycisk_sqrt = Kalkulator.przycisk(self, 160, 275, 40, 40, 'sqrt', partial(wpisywanie, wpisywanie_do, 'sqrt'), 'aquamarine')
    self.przycisk_square = Kalkulator.przycisk(self, 210, 275, 40, 40, '^2', partial(wpisywanie, wpisywanie_do, 'square'), 'aquamarine')
    self.przycisk_exp = Kalkulator.przycisk(self, 260, 275, 40, 40, 'e^', partial(wpisywanie, wpisywanie_do, 'exp'), 'aquamarine')
    self.przycisk_absolute = Kalkulator.przycisk(self, 10, 325, 40, 40, '| |', partial(wpisywanie, wpisywanie_do, 'absolute'), 'aquamarine')
    self.przycisk_floor = Kalkulator.przycisk(self, 60, 325, 40, 40, '[ ]', partial(wpisywanie, wpisywanie_do, 'floor'), 'aquamarine')
    self.przycisk_sinh = Kalkulator.przycisk(self, 110, 325, 40, 40, 'sinh', partial(wpisywanie, wpisywanie_do, 'sinh'), 'aquamarine')
    self.przycisk_cosh = Kalkulator.przycisk(self, 160, 325, 40, 40, 'cosh', partial(wpisywanie, wpisywanie_do, 'cosh'), 'aquamarine')
    self.przycisk_tanh = Kalkulator.przycisk(self, 210, 325, 40, 40, 'tanh', partial(wpisywanie, wpisywanie_do, 'tanh'), 'aquamarine')
    self.przycisk_power = Kalkulator.przycisk(self, 260, 325, 40, 40, '^', partial(wpisywanie, wpisywanie_do, '**'), 'aquamarine')
    self.przycisk_delete = Kalkulator.przycisk(self, 95, 210, 40, 40, '←', partial(delete, wpisywanie_do), 'cyan')
    self.przycisk_clear = Kalkulator.przycisk(self, 140, 210, 40, 40, 'C', partial(clear, wpisywanie_do), 'cyan')

    if wpisywanie_do == interfejs.wzor:
      Kalkulator.polozenie(self, nazwa, '310x375+1100+0', 'yellow')
      self.przycisk_x = Kalkulator.przycisk(self, 210, 175, 40, 40, 'x', partial(wpisywanie, wpisywanie_do, 'x'), 'dodger blue')
      self.przycisk_srednik = Kalkulator.przycisk(self, 50, 210, 40, 40, ';', partial(wpisywanie, wpisywanie_do, ';'), 'cyan')

    else:
      Kalkulator.polozenie(self, nazwa, '310x460+1100+0', 'yellow')

  def oblicz(self, wejscie, interfejs):
    ''' funkcja obliczająca to co wprowadziliśmy przez kalkulator pobierająca obiekt i wejście'''
    global phi
    self.wynik_obliczen.delete(0, END)

    if not wejscie.get():
      interfejs.bledy.delete(0, END)
      interfejs.bledy.insert(0, 'Nie ma tu czego liczyć.')

    else:
      try:
        self.wynik_obliczen.insert(0, eval(wejscie.get()))
      except:
        interfejs.bledy.delete(0, END)
        interfejs.bledy.insert(0, 'Wprowadzono błędne dane, nie można przeprowadzić obliczeń.')


class Pomoc(Interfejs):
  ''' Klasa interfejsu pomocy dziedzicząca po Interfejsie'''
  def __init__(self):
    ''' funkcja tworząca podpowiedzi dla użytkownika w postaci napisów (Label z tkinter)'''
    self.root = Tk()
    Pomoc.polozenie(self, 'Pomoc', '642x255+50+107','yellow')

    Interfejs.napis(self, 5, 5, 632, 20, 'W polu "Wzór funkcji" należy wpisać funkcje o zmiennej x oddzielone ";".')
    Interfejs.napis(self, 5, 30, 632, 20, 'Wzór obsługuje wiele funkcji np. trygonometryczne, we wzorze korzystamy z nawiasów "(" i ")".')
    Interfejs.napis(self, 5, 55, 632, 20, 'W polach nazw oraz zakresów wpisywane dane są oczywiste (dolny < górny !).')
    Interfejs.napis(self, 5, 80, 632, 20, 'Wartości domyślna zakresu dolnego to -10 a górnego to 20.')
    Interfejs.napis(self, 5, 105, 632, 20, 'W polu "Kolory" należy wpisać kolory kolejnych funkcji oddzielone ";".')
    Interfejs.napis(self, 5, 130, 632, 20, 'W polu "Ilość pomiarów" należy wpisać wartość od 1 do 10000, wartość domyślna to 1000.')
    Interfejs.napis(self, 5, 155, 632, 20, 'Kolorowe przyciski wstawiają kolor, przycisk ← to "backspace", a przycisk "C" usuwa wszystko.')
    Interfejs.napis(self, 5, 180, 632, 20, 'W polu "Ścieżka do pliku" zmieniamy ścieżkę zapisanego obrazka, w polu nazwy analogicznie.')
    Interfejs.napis(self, 5, 205, 632, 20, 'W polu "Błędy" dostajemy informacje o błędach i ewentualne wyjaśnienia działania programu.')
    Interfejs.napis(self, 5, 230, 632, 20, 'Przycisk "Włącz" uruchamia szczegółowy kalkulator lub narzędzie do wpisywania wzoru.')


def koniec():
  ''' funkcja wyłączająca cały program'''
  import sys
  sys.exit()


def entry_get(entry):
  ''' funkcja pobierająca pole tekstowe, zwracająca wartość tego pola'''
  return entry.get()


def wpisywanie(wejscie, napis):
  ''' funkcja pobierająca pole tekstowe i napis, wpisująca napis do pola do wpisywania'''
  wejscie.insert(get_info(wejscie), napis)


def clear(wejscie):
  ''' funkcja pobierająca pole tekstowe i czyszcząca jego całą zawartość'''
  wejscie.delete(0, END)


def delete(wejscie):
  ''' funkcja pobierająca pole tekstowe i działająca na nim jak backspace'''
  dane = wejscie.get()
  kursor = get_info(wejscie)
  wejscie.delete(0, END)
  wejscie.insert(0, dane[:kursor - 1])
  wejscie.insert(kursor, dane[kursor:])
  wejscie.icursor(kursor - 1)


def get_info(wejscie):
  ''' funkcja zwracająca aktualną pozycję myszy w polu funkcji kalkulatora'''
  return wejscie.index(INSERT)


if __name__ == '__main__':
  Interfejs()
