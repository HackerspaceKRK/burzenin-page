---
title: QAPRSTracker
puk_category: A
puk_year: 2014
puk_place: 3
author: sq5rwu
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq5rwu_qaprstracker.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq5rwu_qaprstracker.jpg
---





 



![](assets/data/img/projects/2014-3-0.jpg) 



QAPRS Tracker
-------------





 QAPRSTracker jest urządzeniem pozwalającym na nadawanie i odbieraniem ramek w ramach sieci APRS.

 Urządzenie pokazuje na wyświetlaczu odebrane i zdekodowane informacje z sieci APRS.

 Przy włączonym nadawaniu po ustaleniu pozycji z GPS następuje periodyczne wysyłanie ramek z użyciem SmartBeaconing.






Oprogramowanie urządzenia bazuje na bibliotece ArduinoQAPRS – w wersji z obsługą

dekodowania danych nazywanej roboczo ArduinoQAPRSPlus. Kod źródłowy zarówno

zmodyfikowanej biblioteki jak i QAPRSTrackera jest dostępny na licencji GNU.




##### Moduły urządzenia




* moduł radiowy na pasmo 2m firmy DORJI, moc 0.5/1W
* modem AFSK - układ TCM3105
* wyświetlacz graficzny NOKIA 5110 (b&w, 84x48px)
* odbiornik GPS uBLOX NEO6-M
* karta SD (pamięć stała)
* moduł Arduino Pro Mini 16MHz z wymienionym stabilizatorem na 3.3V




##### Zasada działania


###### Odbiór




 Moduł DRA818V MOD1 ustawiany jest programowo na odbiór transmisji FM na

 częstotliwości 144.800MHz.






 Sygnał audio z wyjścia AF\_OUT podawany jest poprzez kondensator odsprzęgający C3 na

 wejście RXA modemu TCM3105 US2. Potencjometr R10 - podłączony do wejścia RXB - pozwala

 na regulację biasu sygnału wejściowego, co przekłada się na próg zadziałania detekcji tonów na

 wejściu RXA. Układ tranzystorów T1 do T3 wraz z rezystorami R1 do R7 pozwalają na podawanie

 na wejście TRS zanegowanego sygnału zegarowego z wyjścia CLK układu US2 oraz sygnału na

 wejścia TXR1 i TXR2 – pozwala to na ustawienie odpowiedniej prędkości transmisji danych, oraz

 na przełączanie pomiędzy trybem nadawania i dekodowania danych przez modem.

 Wykryte sygnały mark i space (czyli tony 1200 i 2200Hz) powodują zmianę stanu na

 wyjściu RXD, tak, że ton MARK daje stan wysoki, a SPACE niski. Sygnał ten doprowadzony jest do

 pinu 5 modułu Arduino (US1). Sygnał CLK doprowadzony do pinu 2 wyzwala przerwanie z

 częstotliwością 19,1kHz. W obsłudze przerwania sprawdzany jest stan pinu 5 i następuje dalsze

 dekodowanie pakietów.

 


###### Nadawanie




Moduł DRA818V MOD1 ustawiany jest programowo na nadawanie transmisji FM na

częstotliwości 144,800 MHz.






Po przygotowaniu danych do wysłania następuje załączenie

nadawania poprzez podanie stanu niskiego na wejście PTT w module. Wejście H/L modułu

podłączone jest do napięcia zasilania mikrokontrolera, co wymusza użycie 1W. Podłączenie tego

wejścia do masy zmniejsza moc do 0.5W (katalogowo).

Na wejście TXD układu US2 podawane są kolejne bity do wysłania. Czas trwania

poszczególnych sygnałów reguluje mikrokontroler poprzez odliczenie odpowiedniej ilości przerwań

na pinie 2 US1. Modem na wyjściu TXA udostępnia sygnał audio (tony mark/space, w zależności

od TXD) kktórypoprzez kondensator C4 podawany jest na wejście mikrofonowe MIC\_IN MOD1.




###### Zasilanie




Układ zasilanie jest napięciem 5 V. Wymagana jest wydajność prądowa około 1A, ponieważ

moduł transcivera może pobierać nawet 750mA przy nadawaniu. Nota katalogowa dla DRA818V

przewiduje dla niego maksymalne napięcie zasilania na poziomie 4,5V. Dlatego też w szereg

z zasilaniem włączona została dioda 1N4148 na której następuje spadek napięcia 0.5-0.6V (w

zależności od pobieranego prądu). Dodatkowo kondensatory C1 i C5 filtrują zasilanie do radia.

Standardowo moduł Arduino Pro Mini zasilany jest napięciem 5 V. Na płytce ma on

zamontowany stabilizator zasilania LDO 5V, do którego zasilanie doprowadzone jest na pin RAW.

Został on w prototypie wymieniony na stabilizator 3,3 V które to napięcie niezbędne jest do

zasilania modułu GPS, wyświetlacza i karty SD. Można również zrezygnować z przerabiania

modułu, nie doprowadzać napięcia 5V do wejścia RAW i użyć dodatkowego stabilizatora 3.3V

z którego napięcie należy doprowadzić do pinu VCC Arduino.




##### Szczegóły budowy


###### GPS




Jako odbiornik GPS użyty został układ NEO6-M firmy u-blox. Komunikacja z Arduino

odbywa się za pomocą portu UART po stronie GPS, biblioteki SoftwareSerial po stronie

mikrokontrolera. Praktyka wskazuje jednak na potrzebę użycia innej biblioteki do emulacji portu

szeregowego albo stworzenia własnej implementacji – wbudowana biblioteka powoduje zakłócenia
{% include swiatradio.html on_page="02/2015 str. 49-51" %}
w dekodowania pakietów APRS poprzez naruszenie zależności czasowych w procedurach obsługi

przerwań. Do odbiornika dołączona jest pastylkowa bateria 3 V podtrzymująca pamięć odbiornika po

odłączeniu zasilania – znacznie przyspiesza to ustalanie pozycji po restarcie urządzenia.




###### Wyświetlacz




Do komunikacji z użytkownikiem zastosowany został graficzny wyświetlacz od Nokii 5110.

Jest to popularny i tani wyświetlacz ciekłokrystaliczny, czarno-biały, o rozdzielczości 84 na 48

pikseli, z podświetleniem LED. Sterownik wyświetlacza to układ PCD8544 – do jego obsługi

w środowisku Arduino zastosowano gotową bibliotekę.




###### Karta SD




Jako że mikrokontroler Atmega328p ma małą ilość pamięci RAM, jak i EEPROM do zapisywania

danych użyto karty SD o pojemności 64 MB. Pozwoli to na zapisanie ponad 60 tysięcy pakietów

zanim nastąpi jej zapełnienie. Dla przyspieszenia operacji na danych nie użyto żadnego systemu

plików na karcie – zamiast tego skorzystano z faktu, że karta SD zapisuje informacje w blokach po

512 bajtów i poszczególne pakiety zapisywane są w osobnych blokach.




###### Klawiatura




Jako klawiaturę zastosowano gotowy podzespół klawiatury matrycowej 3×4 klawisze.

Została ona podłączona do układu rezystorów tak, że naciśnięcie klawisza tworzy dzielnik napięcia

które jest następnie mierzone za pomocą wbudowanego przetwornika analogowo-cyfrowego.

Celem obsługi różnych klawiatur i z uwagi na rozrzut wartości rezystorów przy pierwszym

uruchomieniu układu następuje kalibracja klawiatury a dane kalibracyjne zapisywane są w pamięci

EEPROM.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SQ5RWU_QAPRSTracker.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 02/2015 str. 49-51

 





 


