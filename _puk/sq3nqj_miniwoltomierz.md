---
title: Miniwoltomierz
puk_category: C
puk_year: 2014
puk_place: 10
author: sq3nqj
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq3nqj_miniwoltomierz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq3nqj_miniwoltomierz.jpg
---





 



![](assets/data/img/projects/2014-10-0.jpg) 



Miniwoltomierz
--------------





 Układ służy do pomiaru napięcia, wykorzystuje niewielką liczbę komponentów i cechuje się

 niezwykle małymi rozmiarami. Zmierzoną wartość napięcia wyświetla za pomocą miniaturowych

 siedmiosegmentowych wyświetlaczy LED.






 Stopień podziału w dzielniku wejściowym jest

 zaprojektowany tak, aby prezentowany woltomierz można było wykorzystać do pomiaru napięć

 stałych w zakresie od -200V do +200V. Pomimo tego, ze względu na budowę urządzenia i

 bezpieczeństwo jego użytkowania zakres bezpiecznie mierzonych napięć jest mniejszy i

 ograniczony względami bezpieczeństwa użytkownika.




##### Budowa układu




 Układ wykonany jest w technologii montażu powierzchniowego, wykorzystuje jedynie dwa układy

 scalone: mikrokontroler oraz przetwornik analogowo-cyfrowy. Pozostałe elementy to jeden tranzystor,

 jedna dioda Zenera, rezystory oraz kondensatory. Schemat układu przedstawiony jest na rysunku 3.

 Zastosowanie niewielkiej liczby niewielkich elementów umożliwiło spektakularne zmniejszenie

 całości urządzenia do wymiarów 20,5mm na 10,5mm i wysokość po zamontowaniu na płytce

 stykowej 11mm.






 Układ zasilany jest napięciem 3,3V. Pobór prądu wynosi około 24mA – większość prądu zużywana

jest przez wyświetlacz LED. Woltomierz ma wejście różnicowe, umożliwia pomiar napięć

zewnętrznych jak też własnego napięcia zasilania (przy dowolnej polaryzacji wejść). Wynik

pomiaru wyświetlany jest na wyświetlaczu czteropozycyjnym bez dodatkowego znaku „minus”. Do

wyświetlania znaku „minus” wykorzystywany jest jeden z segmentów wyświetlacza

odpowiadającego „najstarszej” cyfrze. Takie rozwiązanie upraszcza konstrukcję i umożliwia

wykorzystanie łatwiej dostępnych elementów, jednak ogranicza rozdzielczość wyświetlania dla

wartości ujemnych.






W układzie wykorzystywany jest przetwornik analogowo-cyfrowy o

rozdzielczości 18 bitów, komunikujący się z mikrokontrolerem sterującym za pomocą magistrali I2C.

Zastosowane rozwiązanie umożliwia uzyskanie następujących rozdzielczości:  


1) dla zakresu od -2V do 10V: 1mV  


2) dla zakresu od -20 do 100V: 10 mV  


3) dla zakresu od -200 do 200V: 100mV  




##### Zastosowania
{% include swiatradio.html on_page="02/2015 str. 51-53" %}



Zaletą prezentowanego rozwiązania jest bardzo niewielki rozmiar urządzenia (wielkość układu w

obudowie DIP16) i możliwość instalacji na płytce stykowej. Przyrząd umożliwia łatwy pomiar i

monitorowanie wartości napięć (a z użyciem zewnętrznego rezystora pomiarowego – również

prądów) w układzie budowanym na płytce stykowej. Możliwe jest jego zastosowanie przy

uruchamianiu urządzeń na płytkach stykowych i prezentacja ich działania – można za pomocą

kamery bez problemu objąć układ na płytce i woltomierz.






Przy odpowiednich zmianach oprogramowania możliwe jest przeliczanie wyświetlanych wartości

według zadanego sposobu (pierwiastkowanie, podnoszenie do potęgi, mnożenie przez stały

współczynnik i inne operacje matematyczne). Dzięki temu możliwe jest zastosowanie opisywanego

urządzenia w szerokim spektrum urządzeń, takich jak zasilacze czy mierniki mocy. Możliwe jest

też wygodne zastosowanie go jako wskaźnika wbudowywanego we wszelkiego rodzaju urządzenia

pomiarowe.





#### Do pobrania

[Opis konkursowy miniwoltomierza SQ3NQJ](/assets/bin/SQ3NQJ_miniwoltomierz.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 02/2015 str. 51-53

 





 


