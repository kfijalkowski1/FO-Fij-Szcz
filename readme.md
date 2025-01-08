# Fala stojąca w strunie

## Wstęp
Projekt został wykonany w ramach przedmiotu FO - Fizyka ogólna.
Zadanie polegało na symulacji fali stojącej w strunie. Zasymulowane zostały 3 rodzaje takich fal:
- Fale zaczepione po obu końcach
- Fala zaczepiona po jednym końcu
- Fala niezaczepiona
Dla każdego z tych typów fal został zdefiniowany wzór matematyczny wyliczany na podstawie:
- x - położenie punktu na strunie
- t - czas
- a - amplituda fali
- n - liczba falowa
- l - długość struny
- v - prędkość fali
Kolejne typy fal mają następujące wzory:
- Fala zaczepiona na obu końcach: `y(x, t) = A*sin(kx)*cos(ωt)`
- Fala zaczepiona na jednym końcu: `y(x, t) = A*sin(((2n+1)πx)/(2L))*cos(ωt)`
- Fala niezaczepiona: `y(x, t) = 2*A*sin(2*pi*x/L)*cos(ωt)`

## Implementacja
Implementacja została podzielona na dwa pliki:
- `main.py` - plik zawierający kod definiujący działanie interfejsu użytkownika zaimplementowanego w PyQt5 z użyciem matplotlib-a
- `physic_functions.py` - plik zawierający funkcje matematyczne potrzebne do symulacji fali stojącej


## Uruchomienie
Aby uruchomić program należy posiadać środowisko z Pythonem w wersji 3.11 lub wyższej. 
Najpierw należy zainstalować potrzebne paczki za pomocą komendy `pip install -r requirements.txt`.
Następnie należy uruchomić plik `main.py` za pomocą komendy `python main.py`.

Po uruchomieniu programu wyświetla nam się wizualizacja fali, którą możemy edytować w czasie żeczywistym za pomocą pól na dole. Jesteśmy w stanie również wybrać typ generowanej fali.

### Rodzaje fal
W ramach niniejszego projektu zostały zaprojektowane trzy modele fal stojących

#### Fala stojąca zaczepiona na obydwu końcach
![Fala stojąca zaczepiona na obydwu końcach](documentation/standing_wave_fixed_on_both_ends.gif)

#### Fala stojąca zaczepiona na jednym końcu
![Fala stojąca zaczepiona na jednym końcu](documentation/standing_wave_fixed_on_one_end.gif)

#### Fala stojąca która nie jest zaczepiona
![Fala stojąca niezaczepiona](documentation/standing_wave_not_fixed.gif)
