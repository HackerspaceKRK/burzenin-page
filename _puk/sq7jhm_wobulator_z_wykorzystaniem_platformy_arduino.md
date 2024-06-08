---
title: Wobulator z wykorzystaniem platformy Arduino
puk_category: C
puk_year: 2017
puk_place: 9
author: sq7jhm
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq7jhm_wobulator_z_wykorzystaniem_platformy_arduino.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7jhm_wobulator_z_wykorzystaniem_platformy_arduino.jpg
---





 



![](assets/data/img/projects/2017-9-0.jpg) 



Wobulator na platformie Arduino
-------------------------------





 Wersja wobulatora z wykorzystaniem platformy Arduino, w tym przypadku Arduino Mega z ekranem graficznym o rozdzielczości 480x320 pikseli.

 Zastosowanie Arduino umożliwiło wykonanie miernika bez projektowania i lutowania płytki z elementami SMD wysokiej skali integracji.

 




 Wobulator działa w oparciu o skanowanie częstotliwości w zakresie pomiarowym i odczycie napięcia wyjściowego badanego układu,

 które jest podawane i wyświetlane na ekranie. Generator sterujący oparty jest na module DDS. W menu ustawia się częstotliwość

 dolną i częstotliwość górną po czym włączamy skanowanie. Ilość kroków skanowania odpowiada ilości pikseli jaką da się zobrazować na ekranie w poziomie.






 Zakres pracy miernika: od 100kHz do 30MHz.




##### Budowa miernika




 W systemie występują cztery moduły a ich połączenie odbywa się zaledwie kilkoma przewodami.

 W głowicy pomiarowej pracuje analogowy detektor logarytmiczny AD8307. Minimalny poziom sygnału odbierany

 jest na poziomie -80dB w stosunku do sygnału maksymalnego. Zmieniający się poziom napięcia wyjściowego generatora DDS

 w miarę zmian częstotliwości sygnału wyjściowego jest kompensowany programowo.

 

{% include swiatradio.html on_page="07/2017 str. 48-49" %}



#### Odnośniki

[Opis wobulatora na stronie SQ7JHM](https://sq7jhm.pzk.pl/wobulator.html)

 



![](assets/img/logo/sr_logo_s.jpg)###### 07/2017 str. 48-49

 





 


