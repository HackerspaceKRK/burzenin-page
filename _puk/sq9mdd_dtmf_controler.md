---
title: DTMF Controler
puk_category: D
puk_year: 2011
puk_place: 7
author: sq9mdd
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq9mdd_dtmf_controler.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq9mdd_dtmf_controler.jpg
---





 



![](assets/data/img/projects/2011-7-0.jpg) 



Sterownik DTMF
--------------





 Prosty, w pełni otwarty projekt sterownika do zdalnego sterowania urządzeniami drogą radiową za pomocą sekwencji DTMF,

 który może być użyty do kontroli stacji bezobsługowych (przemienników amatorskich).


##### Budowa przyrządu




 Schemat elektryczny sterownika przedstawiony jest na rysunku 2.






 Sterownik został zbudowany w oparciu o procesor **ATtiny 2313**, a program sterujący jest napisany w Bascomie.

 Dekodowanie DTMF jest zapewnione sprzętowo za pomocą układu **CMD8870** (MT8870).






 Układ dekodera na liniach Q1..Q4 wystawia sygnały logiczne 0/1 reprezentujące zdekodowany ton.

 Na wyprowadzeniu StD wystawia sygnał o poprawnie zdekodowanym znaku. Sygnał ten wyzwala przerwanie INT1

 procesora Attiny 2313, a także powoduje zaświecenie diody LED, sygalizującą poprawność dekodowania tonów.

 W procedurze obsługi przerwania procesora wykonywana jest obsługa tonów DTMF, która polega na sterowaniu

 przekaźnikami za pomocą tranzystorów wykonawczych BC547.






 Tryb pracy przekaźnika "NC" lub "NO" jest wybierany za pomocą zworek umiejscowionych obok każdego z nich.

 Na płytce znajduje się gniazdo do podłączenia opcjonalnej płytki DCE1, która rozszerza ilość linii

sterujących z 3 do 6, gniazdo "reset" oraz gniazdo dla opcjonalnego interfejsu RS232.






 Instrukcja montażu i uruchomienia oraz tekst źródłowy programu w Bascomie znajdują sie w załączonej dokumentacji konkursowej.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SQ9MDD_Sterownik-DTMF-v.1.1.pdf)




#### Odnośniki

[Opis na stronie SQ9MDD](http://hamspirit.pl/SQ9MDD/?p=120)

[Film obrazujący działanie sterownika](https://youtu.be/_bMdbXwAIQc)

 



{% include swiatradio.html on_page="05/2012 str. 52-53" %}

 





 


