---
title: Miernik antenowy
puk_category: C
puk_year: 2015
puk_place: 6
author: sq7jhm
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq7jhm_miernik_antenowy.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7jhm_miernik_antenowy.jpg
---





 



![](assets/data/img/projects/2015-6-0.jpg) 



Miernik antenowy
----------------





 Mikroprocesorowy miernik antenowy do pomiaru impedancji anteny Z oraz współczynnika dopasowania SWR.

 Zakres pomiaru od 1,6 MHz do 30 MHz. Dodatkowo wskaźnik poziomu naładowania akumulatora (zużycia baterii zasilającej).

 Konstrukcja miernika oparta jest o rozwiązania konstrukcyjne i teoretyczne rozważania **VK5JST**.






##### Zasada działania miernika




 Działanie miernika jest oparte o pomiar impedancji metodą porównawczą. Układ szeregowo połączonej impedancji anteny

 Z = RA ± jXA z wzorcowym opornikiem bezindukcyjnym R=50Ω zasilany jest z generatora sygnałowego o częstotliwości

 przestrajanej w zakresie od 1,6MHz do 30MHz.








 Napięcia ADC podawane są na wejście mikroprocesora. Z położenia modułów napięć można wyprowadzid wzory do obliczenia VRA i VXA.

Wykresy wskazowe obrazują dwa krańcowe stany: obciążenie rezystancyjne, kiedy antena jest w rezonansie oraz obciążenie reaktancyjne,

 kiedy antena wykazuje obciążenie reaktancyjne pojemnościowe lub indukcyjne.




Generator, opornik wzorcowy i zestaw antenowy są połączone szeregowo w obwodzie zamkniętym - stąd łatwo można obliczyć wartośd

prądu występującego w obwodzie. Mając prąd można obliczyć składowe RA oraz XA impedancji Z oraz wartość SWR.

Obliczone wartości i mierzona częstotliwości generatora obrazowana jest na ekranie LCD.




##### Kalibracja miernika




 Miernik wymaga kalibracji. Należy podłączyć wzorcową oporność bezindukcyjną 50Ω i dokonać korekty wartości oporników

 oznaczonych gwiazdką tak, aby na ekranie uzyskać wartości 50Ω możliwie w całym zakresie częstotliwości KF.






 Miernik zasilany jest z akumulatora Li-Jon o napięciu 3,7V. Napięcie to jest podnoszone do wartości 5V za

 pomocą przetwornicy Step-Up.





{% include swiatradio.html on_page="01/2016 str. 51" %}
Koszt elementów miernika nie przekracza 150zł (obudowa 10zł, wyświetlacz 12zł, akumulator 8zł, gniazdo BNC 2zł,

ATmega8 6zł, 74HC74 1zł, 74HC132 1zł, LTC1799 12zł, pot. 10k/obr 16zł, pot. 50k/A 2zł, podstawki 4zł,

kondensatory 1zł, oporniki 1zł, gałki 7zł).









#### Odnośniki

[Opis miernika na stronie SQ7JHM](https://sq7jhm.pzk.pl/swrmeter.html)

[Miernik antenowy VK5JST](http://www.vk5jst.com/)

 



![](assets/img/logo/sr_logo_s.jpg)###### 01/2016 str. 51

 





 


