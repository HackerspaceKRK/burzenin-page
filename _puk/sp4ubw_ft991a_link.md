--- 
title: FT991(A) Link SP4UBW
puk_category: E
puk_year: 2024
author: 
  - sp4ubw
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp4ubw-004.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp4ubw-004.jpg
gallery1:
  - url: /assets/images/puk/sp4ubw-004.jpg
    image_path: /assets/images/puk/sp4ubw-004.jpg
  - url: /assets/images/puk/sp4ubw-005.jpg
    image_path: /assets/images/puk/sp4ubw-005.jpg
  - url: /assets/images/puk/sp4ubw-006.jpg
    image_path: /assets/images/puk/sp4ubw-006.jpg
gallery2:
  - url: /assets/images/puk/sp4ubw-0010.jpg
    image_path: /assets/images/puk/sp4ubw-010.jpg
  - url: /assets/images/puk/sp4ubw-011.jpg
    image_path: /assets/images/puk/sp4ubw-011.jpg
---

Program powstał z powodu braku darmowych programów do sterowania przy pomocy CAT, dostępnych dla popularnych modeli firmy Yaesu: FT-991 oraz FT-991A. 

### Opis programu: 

Program nazywa się FT991(A) Link i pozwala na obsługę radia przez interfejs CAT. Można wykorzystać port COM lub port USB radia. Polecam port USB, dlatego, że jednym przewodem mamy od razu podłączoną do komputera kartę dźwiękową umieszczoną w radiu. 

Program ma zaimplementowane sterowanie radiem, pełną obsługę programowania kanałów pamięci z zapisem do pliku i odczytem, pełną obsługę menu radia, również z zapisem do pliku i odczytem. 

Dodatkowo obsługuje dźwięk z radia do odsłuchu na komputerze. Można obserwować widmo sygnału audio, mierzyć częstotliwość CTCSS, mierzyć sygnał w dowolnym miejscu wykresu przy pomocy kursorów. 

Zostało poprawionych kilka ułomności w funkcjach tych TRXów, takich jak zmiana częstotliwości przy zmianie modulacji, czy przełączanie pomiędzy VFO i kanałami pamięci. Zostały dodane brakujące funkcje, a kolejne pojawią się z czasem. 


{% include gallery id="gallery1" %}

#### Na przykład: 

- podczas skanowania kanałów pamięci, na wyświetlaczu w programie pokazywana jest ostatnia słyszana częstotliwość (lub nazwa kanału) - funkcja, której nie ma w radiu, a która jest bardzo przydatna podczas skanowania kanałów pamięci; 
- szybkie rozpoznawanie tonu CTCSS. Działa zarówno w głównym oknie programu jak i w oknie RX Audio. Czas rozpoznania tonu wynosi około 1⁄4 sekundy. 

Aplikacja posiada tryb jasny i ciemny, do wyboru w menu. Posiada skalowanie – również dostępne w menu. Do testów polecam tryb ciemny, nie męczy wzroku i jest bardzo czytelny. 

Po rozłączeniu kabla USB na belce programu pojawi się komunikat o braku połączenia. Po ponownym podłączeniu radia, odczyt parametrów startuje automatycznie. Program oprócz sterowania zapewnia pełne programowanie kanałów pamięci w radiu. 

Można na bieżąco mieć podgląd wszystkich pamięci i przełączać się między nimi oraz dodawać nowe lub edytować istniejące. Dodatkowo można zapisać wszystkie kanały pamięci do pliku oraz odczytać zapisany plik, edytować kanały pamięci po wczytaniu z pliku i zapisać do radia. 

Kolejną funkcją jest pełna obsługa menu z radia, które również można zapisać do pliku i przywrócić z pliku do radia. 

Podczas używania zakładki menu można zmieniać prędkość komunikacji – program dostosuje się automatycznie do wybranej prędkości. 

Można też dostawać powiadomienia systemowe, jeśli radio odbierze stację. Wygodny sposób aby program działał i nie przesłaniał innych uruchomionych programów. 

Program jest stale rozwijany i może posiadać błędy, za które nie odpowiadam. Każde zgłoszenie użytkowników pozwala eliminować zauważone błędy dlatego zachęcam do zgłaszania błędów i sugestii. 

E-mail jest dostępny z menu w zakładce „Info/Update”. FT991 Link jest do pobrania zawsze pod tym samym adresem w postaci instalatora lub pliku zip, który nie wymaga instalacji. 

Skanowanie antywirusowe zapewnia dysk Google, dzięki czemu mamy pewność, że pobieramy program wolny od wirusów. Link do programu i sprawdzania nowych wersji jest dostępny z menu w zakładce „Info/Update” .

{% include gallery id="gallery2" %}

Program został przetestowany na modelach:
- FT-991
- FT-991A

Z czasem lista modeli zostanie powiększona (FT-950, FTDX-1200, FTDX-10 i inne).

Program został opracowany dla systemu Windows jako aplikacja 32 bitowa, więc powinien działać od Windows XP do Windows 11. 
FT991(A) Link działa poprawnie (został przetestowany na wielu radiach), nie powoduje
ingerencji w radio innej niż dopuszczone komendami CAT, dzięki czemu nie traci się gwarancji
na posiadany sprzęt. Jest darmowy i taki pozostanie. Nie zawiera reklam.

Link do folderu z najnowszą wersją, zrzutami ekranów, opisem zmian: (dysk Google):

https://bit.ly/ft991

[Dokumentacja konkursowa](/assets/bin/SP4UBW_E_FT991Link.pdf)