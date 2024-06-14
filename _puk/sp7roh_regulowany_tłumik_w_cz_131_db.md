---
title: Regulowany tłumik w.cz. 131 dB
puk_category: C
puk_year: 2013
puk_place: 9
author: sp7roh
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7roh_regulowany_tłumik_w_cz_131_db.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7roh_regulowany_tłumik_w_cz_131_db.jpg
---





 



![](assets/data/img/projects/2013-9-0.jpg) 



Regulowany tłumik w.cz. 131 dB
------------------------------





 Tłumik w.cz. jest jednym z kluczowych elementów wyposażenia pracowni radioamatora. Niestety, tłumiki fabryczne

 są trudno dostępne w przystępnych cenach, dlatego dobrą alternatywą jest wykonanie tłumika we własnym zakresie.

 Taką alternatywą może być opisany poniżej tłumik. Charakteryzuje się on dobrymi parametrami elektrycznymi,

 małymi wymiarami oraz szybkim ustawianiem wymaganej wartości tłumienia.

 




 Tłumik składa się z dwunastu ogniw rezystancyjnych typu π o wartościach tłumienia 1+2+3+5+10+10+10+10+20+20+20+20 dB.

 Ogniwa są łączone szeregowo przez odpowiednio sterowane miniaturowe przekaźniki elektromagnetyczne.

 Tłumienia łączonych ogniw sumują się, co pozwala na ustawienie dowolnej wartości w zakresie 0÷131 dB z krokiem 1dB.

 Rezystory tworzące ogniwa są typowymi rezystorami SMD 0805. Zasilanie tłumika sygnałem w.cz. realizowane jest poprzez złącza SMA.






 Tłumik ma rezystancję charakterystyczną ok. 50Ω i zakres częstotliwości do 200MHz, a maksymalny poziom sygnału

 jaki można podać na wejście wynosi +20dBm (tj. moc 100mW na obciążeniu 50Ω).






 Układ jest zasilany z zewnętrznego zasilacza stabilizowanego 8-12V.

 Pobierany prąd zależy od zadanego tłumienia (liczby załączonych przekaźników), max. 300mA.






 Część sterująca przekaźnikami zbudowana jest w oparciu o popularny mikrokontroler AVR ATmega 8, a program napisany jest w BASCOMIE.






 Nastawy wartości wymaganego tłumienia dokonuje się enkoderem. Wartość ta wskazywana jest wyświetlaczu LCD.

 Układ jest przystosowany do wyświetlacza LCD o organizacji 2x8 znaków lub 1x6 znaków.

 W górnej linijce wyświetlane jest aktualnie ustawione tłumienie, a w dolnej Step 1 lub Step 10.

 Krótkie przyciskanie przycisku enkodera powoduje przełączanie kroku zmiany tłumienia
{% include swiatradio.html on_page="04/2014 str. 46-48" %}
 (Step 1 lub Step 10 i przesunięcie kursora z jedności na dziesiątki i odwrotnie).

 Dłuższe przytrzymanie przycisku (ok. 1 sekundy) powoduje przełączenie tłumienia na 0dB,

 następne dłuższe przytrzymanie powoduje przełączenie do poprzednio ustawionej wartości.






 Płyty, czołowa i tylna wykonane są z cienkiej blaszki aluminiowej, a opisy metodą kalkomanii wodnej i pokryte lakierem akrylowym.

 Obudowa pochodzi z wycofanego z użytku modemu kablowego DSL - THOMSON TCM410.






 Urządzenie zmontowane ze sprawnych elementów startuje od pierwszego włączenia i nie wymaga dodatkowego uruchamiania.







![](assets/img/logo/sr_logo_s.jpg)###### 04/2014 str. 46-48

 





 


