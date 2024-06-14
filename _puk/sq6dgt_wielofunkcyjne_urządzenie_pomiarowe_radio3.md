---
title: Wielofunkcyjne urządzenie pomiarowe "radio3"
puk_category: C
puk_year: 2017
puk_place: 8
author: sq6dgt
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq6dgt_wielofunkcyjne_urządzenie_pomiarowe_radio3.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq6dgt_wielofunkcyjne_urządzenie_pomiarowe_radio3.jpg
---





 



![](assets/data/img/projects/2017-8-0.jpg) 



Wielofunkcyjne urządzenie pomiarowe "radio3"
--------------------------------------------





 "radio3" to modułowe urządzenie pomiarowe, sterowane komputerem osobistym. W projekcie wykorzystano gotowe

 koncepcje modułów pomiarowych (sond) ogólnie dostępne w internecie, oraz w literaturze radiotechnicznej i prasie popularnej.




##### Możliwości pomiarowe




* pomiar mocy sygnału za pomocą sondy logarytmicznej
* pomiar wartości skutecznej sygnału za pomocą sondy liniowej
* pomiar częstotliwości do 60 MHz z rozdzielczością 16Hz
* pomiar SWR oraz zespolonej impedancji obciążenia (np. anteny)
* zdejmowanie charakterystyki częstotliwościowej czwórnika w trybie

 wobulatora (przemiatanie częstotliwości)






 Pomiary mogą być wykonywane w trybie jednorazowym (wyzwalanie ręczne) lub ciągłym.






 Warstwa prezentacji i kontroli została przeniesiona na stronę

komputera PC, co pozwoliło uprościć układ i obniżyć całkowite koszty. Daje to

również bez porównania większą swobodę w obróbce danych i

implementowaniu warstwy prezentacji.




##### Moduły urządzenia



Urządzenie składa się z następujących modułów (rysunek 3):



* moduł mikrokontrolera STM32F103C8T6 (sterujący)
* sonda logarytmiczna AD8307
* sonda liniowa AD8361
* sprzęgacz kierunkowy AD8302
* częstościomierz
* tłumiki 6/10/20 dB
* wzmacniacz w.cz. LT1252
* generator VFO AD9851/AD9850
* sterownik przekaźników L293D
* zasilacz stabilizowany +5V






 Wszystkie moduły umieszczone są na płytce bazowej, która

 stanowi podstawę rozwojową przyrządu.

 




 Jako mikrokontroler sterujący pracuje układ STM32F103C8T6, któy wybrano ze względu

na dostępność tanich modułów pasujących do podstawek DIL-40. Moduły te mimo niskiej ceny,

mają duże możliwości: moc obliczeniową, wielkość pamięci RAM i FLASH oraz dostępne

peryferia. Można je kupić w Polsce w cenie poniżej 20 zł a od chińskiego

dostawcy nawet kilkakrotnie taniej.






Korzystając z faktu, że STM32F103C8 ma wbudowany interface USB i

podstawowe sprzętowe wsparcie komunikacyjne, zdecydowano się na

wykorzystanie programowej implementacji urządzenia klasy CDC, które jest

rozpoznawane przez system operacyjny host-a jako port/urządzenie

szeregowe. Oprogramowanie sterujące mikrokontrolerem (firmware)

zostało napisane w języku C++ przy użyciu darmowych narzędzi do kompilacji

i uruchamiania.

{% include swiatradio.html on_page="05/2018 str. 48-53 (cz. 1 - konstrukcja), 06/2018 str. 46-51 (cz. 2 - pomiary)" %}




 Jako VFO wykorzystano gotowy moduł DDS na układzie AD9851.

 Dla pozostałych modułów zostały zaprojektowane płytki drukowane (program Eagle)

 i wykonane techniką termotransferu.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SQ6DGT_Radio3.pdf)




#### Odnośniki

[Opis projektu "radio3" na stronie SQ6DGT](https://mindpart.com/strona-glowna/projekty/radio3/)

 



![](assets/img/logo/sr_logo_s.jpg)###### 05/2018 str. 48-53 (cz. 1 - konstrukcja), 06/2018 str. 46-51 (cz. 2 - pomiary)

 





 


