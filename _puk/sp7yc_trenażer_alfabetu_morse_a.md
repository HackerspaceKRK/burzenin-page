---
title: Trenażer alfabetu Morse'a
puk_category: D
puk_year: 2012
puk_place: 13
author: sp7yc
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7yc_trenażer_alfabetu_morse_a.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7yc_trenażer_alfabetu_morse_a.jpg
---





 



![](assets/data/img/projects/2012-13-0.jpg) 



Trenażer alfatetu Morse'a
-------------------------





 Symulator oparty na procesorze ATmega8, stanowiący kompletne urządzenie do nauki odbioru i nadawania telegrafii alfabetem Morse'a.

 Program dla mikroprocesora napisany jest w języku BASCOM.






 Urządzenie umożliwia:

 

* odbiór znaków alfabetu Morse’a z wybranym tempem w zakresie od 5 do 40 grup/min
* nadawanie kluczem telegraficznym sztorcowym
* nadawanie kluczem telegraficznym automatycznym z wybranym tempem







##### Parametry funkcjonalne




 W trybie odbioru trenażer umożliwia generowanie znaków alfabetu Morse’a w formie grup (po pięć znaków w grupie) w następującej postaci:

 

* tekst literowy (praca ciągła - z wykorzystaniem generatora liczb pseudolosowych)
* tekst cyfrowy (praca ciągła - z wykorzystaniem generatora liczb pseudolosowych)
* tekst mieszany (litery + cyfry około 70 grup - można wpisać własny tekst w programie źródłowym)
* tekst ze skrótami używanymi w łączności telegraficznej (kod Q) ok. 70 grup – można wpisać własny tekst w programie źródłowym
* tekst z przykładową łącznością telegraficzną (QSO) – można wpisać własny tekst w programie źródłowym
* tekst jawny – można wpisać własny tekst w programie źródłowym







##### Opis działania układu




 Sygnał sterujący wychodzący z procesora (wyprowadzenie 6) steruje tranzystor kluczujący (NPN) w takt nadawanych znaków.

 Tranzydtor odblokowuje generator Wiena, wykonany na jednym wzmacniaczu operacyjnym TDA2822.

 Drugi wzmacniacz operacyjny tego obwodu jest wzmacniaczem głośnikowym zasilającym głośnik lub słuchawki.






 Trenażer posiada dwa tryby pracy umożliwiające odbiór z wybranym tempem oraz nadawanie kluczem sztorcowym lub automatycznym.

 Tryb pracy (odbiór lub nadawanie) wybierany jest przełącznikiem.

 Tempo odbioru i tempo nadawania kluczem automatycznym wybierane jest przyciskami.




##### Opis montażu i uruchomienia




 Płytka PCB została utworzona w programie SprintLayout 6.0 i wykonana metodą termotransferu dla pełnej wersji trenażera

 z generatorem Wiena i wzmacniaczem m.cz. na TDA2822. Część połączeń jest wykonana zworkami. Należy zwrócić uwagę na

 zworki znajdujące się pod obwodami scalonymi, należy je wlutować przed wlutowaniem podstawek.






 Na płytce montujemy w pierwszej kolejności obwody związane z TDA2822 (bez tranzystora kluczującego).

 Powinniśmy uzyskać generację tonu w pełnym zakresie akustycznym.

 Warunkiem uzyskania generacji w generatorze Wiena jest dobranie dzielnika sprzężenia zwrotnego między wyjściem (pin 1)

 a wejściem odwracającym (pin 8) wzmacniacza operacyjnego. Można zastosować oporniki o proporcji 1:3 np. 3,3k i 12k,

 lub dioda i dobrany opornik lub inny rodzaj stabilizacji amplitudy generatora.

 




Zasilanie procesora ATmega8 (pin 7 i 8) musi być odblokowane kondensatorem 0,1uF.

Kondensator ten powinien znajdować się blisko wyprowadzeń mikroprocesora.




##### Uwagi końcowe




 Do pracy urządzenia wyświetlacz nie jest konieczny, nie ma wtedy podglądu.






 Można też wykonać trenażer w wersji bateryjnej (3V). Nie montuje się wyświetlacza ze względu na pobór prądu a procesor musi być

 w wersji L (ATmega8L).
{% include swiatradio.html on_page="07/2013 str. 50-52" %}





 Dla wersji bateryjnej można zrezygnować z niektórych funkcji urządzenia (np. klucza, funkcji RESET, *długa kreska*).

 Nie montujemy wtedy zbędnych przycisków i przełączników.

 




 Zamiast potencjometru regulacji tonu 2x47k można zastosować oporniki 2x po 10k i kondensatory 2x10n.






 Jako gniazda klucza użyłem gniazd słuchawkowych stereo typu mini Jack, jedno dla klucza sztorcowego, drugie do automatycznego.

 Na płytce PCB znajduje się również gniazdo do programowania.





#### Do pobrania

[Opis konkursowy (plik PDF)](/assets/bin/SP7YC_Trenazer-Morsea.pdf)

[Wzór PCB do termotranferu (plik PDF)](/assets/bin/SP7YC_PCB-trenazer-Morsea.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 07/2013 str. 50-52

 





 


