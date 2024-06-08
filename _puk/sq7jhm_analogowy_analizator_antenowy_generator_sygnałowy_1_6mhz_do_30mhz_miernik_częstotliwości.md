---
title: Analogowy analizator antenowy + generator sygnałowy 1,6MHz do 30MHz + miernik częstotliwości
puk_category: C
puk_year: 2011
puk_place: 5
author: sq7jhm
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq7jhm_analogowy_analizator_antenowy_generator_sygnałowy_1_6mhz_do_30mhz_miernik_częstotliwości.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7jhm_analogowy_analizator_antenowy_generator_sygnałowy_1_6mhz_do_30mhz_miernik_częstotliwości.jpg
---





 



![](assets/data/img/projects/2011-5-0.jpg) 



Analogowy analizator antenowy
-----------------------------





 Wielofunkcyjny przyrząd pomiarowy umożliwia wyszukanie częstotliwości rezonansowej anteny (zestawu antenowego) przez pomiar impedancji w całym paśmie KF,

 generowanie napięć oraz pomiar częstotliwości w zakresie KF za pomocą cyfrowego miernika częstotliwości.




##### Funkcje urządzenia




Przyrząd może pracować w całym zakresie krótkofalowym jako:


* analizator antenowy do pomiaru impedancji w zakresie 10–450 Ω
* miernik częstotliwości od 10 kHz do 30 MHz
* generator funkcyjny o zakresie 1,7–30 MHz





##### Budowa i działanie




Schemat ideowy przyrządu jest pokazany na rysunku 3.






Głównym elementem przyrządu jest układ scalony **LTC1977**, który generuje sygnał o częstotliwości od 1,7 MHz do 30 MHz.

Zmiana częstotliwości odbywa się przez zmianę wartości szeregowo połączonych rezystorów: 3,3 kΩ, potencjometru 47 kΩ/A

(zgrubne ustawienie częstotliwości w zakresie 1,7–30 MHz) oraz potencjometru wieloobrotowego 2,2 kΩ (dokładne ustawienie częstotliwości).

Amplitudę sygnału generatora można zmieniać w zakresie od 0V do 1,0V za pomocą potencjometru 1 kΩ/A.






Na wyjściu generatora jest włączony cyfrowy miernik częstotliwości zbudowany według konstrukcji **DL2YHF** (kit rozprowadzany przez Łukasza **SQ2DYL**).

Miernik ma czułość około 50 mV i impedancję wejściową około 5 kΩ. Można zastosować dowolny inny miernik częstotliwości o maksymalnej częstotliwości

pomiaru co najmniej 30 MHz.






Właściwy analizator antenowy do pomiaru impedancji zestawu antenowego tworzy mostek rezystorowy (2×150Ω + 50Ω) i układ pomiarowy z prostownikiem

diodowym (BAT42). Zastosowana metoda porównawcza napięcia jest oryginalnym pomysłem autora (przed pomiarem przeprowadza się kalibrację do oporności wzorcowej

50 omów).




Wewnątrz obudowy przyrządu znajduje się akumulator 12V pozwalający na pracę przez około 10 godzin oraz wewnętrzna ładowarka z zasilaczem buforowym

230 V/AC. Urządzenie ma również sygnalizator akustyczny rozładowanego akumulatora.







#### Odnośniki

[Opis analizatora na stronie SQ7JHM](https://sq7jhm.pzk.pl/swrmeter.html)

 [12/2011 str. 52-53](http://www.swiatradio.com.pl/virtual/modules.php?name=Downloads&d_op=getit&lid=43)

{% include swiatradio.html on_page="12/2011 str. 52-53" %}