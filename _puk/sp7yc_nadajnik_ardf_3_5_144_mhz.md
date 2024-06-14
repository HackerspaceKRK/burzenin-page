---
title: Nadajnik ARDF 3,5/144 MHz
puk_category: A
puk_year: 2014
puk_place: 1
author: sp7yc
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7yc_nadajnik_ardf_3_5_144_mhz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7yc_nadajnik_ardf_3_5_144_mhz.jpg
---





 



![](assets/data/img/projects/2014-1-0.jpg) 



Nadajnik ARDF 80m/2m
--------------------







##### Dane techniczne




* zasilanie 12 V
* pobór prądu w czasie nadawania na paśmie 3,5 MHz – 600 mA
* pobór prądu w czasie nadawania na paśmie 144 MHz – 200 mA




##### Elementy obsługi




* Przełącznik obrotowy 4-pozycyjny „cykl nadawania” pozwala wybrać w ilu minutowym cyklu pracują lisy.

 Jeżeli wybierzemy cykl 2 min. to aktywne mogą być tylko lisy MOE i MOI, jeżeli wybierzemy cykl 3 min,

 to aktywne mogą być tylko lisy MOE, MOI, MOS itd. Jeżeli popełnimy pomyłkę w określeniu cyklu i ilości lisów

 to sterownik uprzedzi nas o tym poprzez szybkie miganie diodą LED.
* Przełącznik obrotowy „numer lisa” 8-pozycyjny pozwala wybrać znak lisa: MOE, MOI, MOS, MOH,MO5.

 Te znaki są programowo związane z cyklem nadawania i alarmem na diodzie LED w przypadku nieprawidłowego ustawienia.

 W pozycji 6 przełącznika nadawany jest w sposób ciągły znak MO, w pozycji 7 znak MOU - 1 minutę nadaje, 1 minutę przerwa.

 Pozycja 8 przełącznika to TEST nadajników.
* Przełącznik obrotowy 4–pozycyjny „Delay” pozwala wybrać start opóźniony: 0, 30, 60 lub 90 min.
* Przycisk RESET - start nadawania w zaprogramowanym cyklu i ustawieniu.
* Przełącznik 144/3,5 MHz – wybór pasma.




##### Nadajnik 3,5 MHz




 Nadajnik 3,5 MHz nie odbiega od publikowanych często rozwiązań. Tranzystor BC i obwód HEF4001 pełni rolę kluczowanego generatora.

 Stopień końcowy na tranzystorze 2SC2166 ( z niewielkim radiatorem) i filtr wyjściowy to również rozwiązanie standardowe.

 W stopniu końcowym bardzo dobrze pracują tranzystory stosowane w CB. Na wyjściu nadajnika znajduje się obwód dopasowania

 (kondensator 250 pF i cewka 4,4 uH) do anteny „long wire” – 10 m. Przy korzystaniu z anteny 50 omowej na 3,5 MHz elementów tych się nie montuje.




##### Nadajnik 144 MHz




 Nadajnik 144 MHz jest trzystopniowy. Stopień pierwszy na tranzystorze 2N2222 to generator z obwodem rezonansowym w kolektorze zestrojonym na 48 MHz.

 Stopień drugi na tranzystorze BFW16 to powielacz/driver strojony na 144 MHz. Stopień końcowy na tranzystorze BSX60 lub BFW16.

 Tranzystory drivera i PA muszą być wyposażone w radiatory.

 Modulator na tranzystorach BD139 i BC547 moduluje prądami kolektora drivera i PA.




##### Sterownik




 Sterowanie nadajnikami zapewnia procesor Attiny 2313. Z powodu niewystarczającej ilości portów w procesorze zastosowałem rozszerzenie na diodach.

 Ponieważ procesor znajduje się w pobliżu stopni końcowych nadajników, a obawiałem się szkodliwego indukowania się napięć na portach to profilaktycznie

 dla usztywnienia napięcia na portach, wszystkie porty są podciągnięte do plusa 5V opornikami 4,7 k.

Program procesora napisany jest w BASCOMIE.




##### Wielofunkcyjna dioda LED




 Podczas prawidłowej pracy nadajnika dioda LED błyska co sekundę.

 Przy nieprawidłowym ustawieniu przełączników „cykl nadawania” i „numer lisa” dioda LED błyska w szybkim tempie.

 Przy wykorzystaniu funkcji Delay podczas oczekiwania na opóźniony start dioda błyska w rytmie „trzy krótkie - jeden długi”

 przez cały czas oczekiwania. Po odliczeniu wybranego czasu opóźnienia nadajnik uruchamia się automatycznie i pracuje zgodnie z wybranymi ustawieniami.

 


##### Uruchomienie - nadajnik 144 MHz




* przełącznik „numer lisa” ustawić na TEST
* sprawdzić i zestroić obwód generatora 48 MHz (np. przy pomocy GDO)
* w miejsce anteny podłączyć obciążenie 50 omów, (lub szeregowo dwie żaróweczki 2,4V/0,1A)
* posługując się wbudowanym wskaźnikiem dostrojenia i GDO dostroić do rezonansu wszystkie obwody
* można dla kontroli odsłuchiwać sygnał na odbiorniku






 Strojenie przebiega bezproblemowo bez objawów jakichkolwiek sprzężeń. Przy zachowaniu wymiarów cewek, jak na schemacie,

 nie ma potrzeby regulowania indukcyjności. Stroimy tylko trymerami.




##### Uruchomienie - nadajnik 3,5 MHz




* podłączyć antenę (10 m rozwieszonego przewodu) lub opornik około 800 omów / 1..2 W
* przełącznik „numer lisa” ustawić na TEST
* dobrać wartość kondensatora 250 pF (z gwiazdką) na maksymalną moc.

 Jeżeli rdzenie i kondensatory we filtrze wyjściowym będą takie jak na schemacie, to nie ma potrzeby dalszego strojenia.
{% include swiatradio.html on_page="01/2015 str. 46-48" %}
 Jeżeli nie, to elementy filtra trzeba dobierać eksperymentalnie, bo filtr ten w znacznym stopniu wpływa na moc oddawaną przez nadajnik.




##### Obudowa





 Zastosowano typową obudowę Kradex Z59 o wymiarach:

 * wysokość 58,4 mm
* szerokość 115,3 mm
* długość 125,5 mm





#### Do pobrania

[Projekt PCB w Sprint Layout (plik .lay)](/assets/bin/SP7YC_Nadajnik-ARDF.lay)

[Mozaika PCB do termotransferu (plik pdf)](/assets/bin/SP7YC_Nadajnik-ARDF_PCB.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 01/2015 str. 46-48

 





 


