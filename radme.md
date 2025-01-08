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
- Fala zaczepiona po obu końcach: `y(x, t) = A*sin(kx)*cos(ωt)`
- Fala zaczepiona po jednym końcu: `y(x, t) = A*sin(((2n+1)πx)/(2L))*cos(ωt)`
- Fala niezaczepiona: `y(x, t) = 2*A*sin(2*pi*x/L)*cos(ωt)`

## Uruchomienie
Aby uruchomić program należy posiadać środowisko z Pythonem w wersji 3.11 lub wyższej. 
Najpierw należy zainstalować potrzebne paczki za pomocą komendy `pip install -r requirements.txt`.
Następnie należy uruchomić plik `main.py` za pomocą komendy `python main.py`.


## Implementacja
Implementacja została podzielona na dwa pliki:
- `main.py` - plik zawierający kod definiujący działanie interfejsu użytkownika zaimplementowanego w PyQt5
- `physic_functions.py` - plik zawierający funkcje matematyczne potrzebne do symulacji fali stojącej