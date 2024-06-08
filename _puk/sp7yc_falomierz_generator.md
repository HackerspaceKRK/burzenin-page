---
title: Falomierz generator
puk_category: C
puk_year: 2012
puk_place: 9
author: sp7yc
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7yc_falomierz_generator.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7yc_falomierz_generator.jpg
---





 



![](assets/data/img/projects/2012-9-0.jpg) 



Falomierz-generator
-------------------





 Falomierz–generator jest przyrządem pomiarowym pozwalającym na pomiar parametrów obwodów rezonansowych.

 Może spełniać wiele funkcji. Za pomocą przełącznika można wybrać rodzaj pomiaru: dip-meter, generator modulowany, falomierz.

 Pokrywa zakres od 450 kHz do 200 MHz w siedmiu podzakresach.






 Falomierz–generator jest bardzo czułym przyrządem, szczególnie falomierz. Posiada regulowane wyjście sygnału w.cz. oraz

 generator modulacyjny m.cz. Zwiększa to funkcjonalność urządzenia.




##### Elementy i montaż układu




 Montaż elektryczny wykonany jest na płytce drukowanej. Ze względu na długości ścieżek i zwartość konstrukcji,

 część tranzystorów oraz rezystory i kondensatory są w wykonaniu SMD. Tranzystory generatora w.cz. to dwubramkowe

 tranzystory MOSFET BF968 (SMD). Tranzystory NPN multiwibratora m.cz. też są SMD.






 Generator jest wykonany na dwóch tranzystorach dwubramkowych MOSFET. Ze źródła tych tranzystorów poprzez stopień buforowy

 na tranzystorzepolowym BF245 wyprowadzony jest sygnał wysokiej czestotliwości, który może być podłączony do cyfrowego

 licznika częstotliwości, pomocnego przy skalowaniu urządzenia lub jako źródło sygnału w.cz.






 W obwód źródła szeregowo włączony jest również tranzystor NPN, który stanowi zmienną oporność regulowaną poprzez

 zmianę napięcia na bazie przy pomocy potencjometru 47 k .Potencjometrem tym ustawia się próg oscylacji generatora.

 Na progu oscylacji czułość urządzenia jest największa.

 Napięcie na bramkach drugich generatora jest ustawione na poziomie 4V. Do bramek przyłączony jest również multiwibrator

 modulacyjny m.cz.

 




 Jako kondensator strojeniowy wykorzystano kondensator foliowy pochodzący z popularnych radioodbiorników.

 Należy zwrócić uwagę na pojemności sekcji tych kondensatorów, bo są bardzo różne. Wybrany spośród kilku kondensatorów

 150/90 i 2x27 pF pokrywa cały zakres od 450 kHz do 200 MHz w 7 podzakresach, przy stabilnej amplitudzie sygnału w.cz. w całym zakresie.

 Wszystkie cztery sekcje kondensatora strojeniowego wyprowadzone są na gniazdo.

 


##### Uruchomienie i strojenie




 Podczas procesu strojenia falomierza – generatora gorący koniec cewki łączymy albo z jedną sekcją kondensatora

 albo z kilkoma w zależności od zakresu i żądanego współczynnika pokrycia.

 Połączenia kondensatorów wykonujemy na wtyczce cewek.

 




 Na najwyższym zakresie jest podłączona tylko jedna sekcja kondensatora 27pF, a potem stopniowo na niższych zakresach

 dołączane są pozostałe sekcje. Skalowanie przyrządu przeprowadza się w następujący sposób:

 





* w miejsce skali nakleić kartkę papieru z naniesioną skalą kątową 0-180 stopni (wykonaną na komputerze)
* do wyjścia w.cz. podłączyć miernik częstotliwości
* dla najwyższego zakresu (do 200 MHz) dobrać wymiary cewki (1 zwój) i zanotować wartości kątowe odpowiadające określonej częstotliwości
* dobrać kolejną cewkę, dołączając kolejną sekcję kondensatora obrotowego tak, aby zakres przestrajania zazębiał się i aby amplituda sygnału była w miarę stabilna
* wykonać właściwą skalę w programie rysunkowym na komputerze (np. CadDraw 4)







##### Uwagi dodatkowe




 Nie podaję ilości zwojów poszczególnych cewek, a tylko sposób postępowania,

 bo zależne one będą od pojemności kondensatora obrotowego i wymiarów cewki.

 




 Wymienne cewki wykonane są na wtykach DIN i wklejone w rurkę PCV. Gniazdo kątowe DIN wymiennych cewek wlutowane jest w płytkę PCB

 i połączone krótkimi przewodami z kondensatorem strojeniowym.

 




Dioda 1N4148 w drenie pierwszego MOSFETA służy do odcięcia obwodów wejściowych od układu generatora podczas pracy jako falomierz. Poprawia to w znacznym stopniu czułość falomierza.



{% include swiatradio.html on_page="06/2013 str. 50-52" %}


W układzie detektora (dioda AA118 i tranzystor 2N3904) należy zwrócić uwagę na dobór tego tranzystora. Z posiadanych tranzystorów

ten typ tranzystora pracował najlepiej. Dioda może być inna np. DOG61.






Wzmacniacz prądu stałego posiada regulację czułości (pot. 47k) i wyjście słuchawkowe do odsłuchu sygnału przy pracy jako falomierz.






Falomierz generator może być zasilany z baterii 9V lub z zasilacza zewnętrznego. Kontrola stanu baterii jest wykonana na diodzie LED

i diodzie Zenera 6,8V. Jeżeli napięcie baterii spadnie poniżej wartości napięcia diody Zenera, to dioda LED przestaje świecić.

Przy zasilaniu z zewnętrznego zasilacza działa dodatkowo podświetlenie miernika. Diody w obwodach zasilania służą do odseparowania

baterii i zasilacza zewnętrznego.






 Przełącznik obrotowy 2x4 pozycje służy do wyłączania i przełączania napięć zasilających poszczególnych stopni przyrządu.

 




 Jako obudowę wykorzystałem pudełko od zasilacza impulsowego, dlatego płytka PCB jak i rozmieszenie poszczególnych

 elementów było limitowane wymiarami tej obudowy.

 



#### Do pobrania

[Wzór płytki drukowanej do termotrasferu (plik PDF)](assets/data/download/SP7YC_PCB-falomierz-generator.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 06/2013 str. 50-52

 





 


