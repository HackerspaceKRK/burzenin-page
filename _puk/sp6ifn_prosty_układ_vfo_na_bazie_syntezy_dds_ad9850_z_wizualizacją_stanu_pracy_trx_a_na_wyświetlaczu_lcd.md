---
title: Prosty układ VFO na bazie syntezy DDS AD9850 z wizualizacją stanu pracy TRX-a na wyświetlaczu LCD
puk_category: D
puk_year: 2013
puk_place: 17
author: sp6ifn
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6ifn_prosty_układ_vfo_na_bazie_syntezy_dds_ad9850_z_wizualizacją_stanu_pracy_trx_a_na_wyświetlaczu_lcd.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6ifn_prosty_układ_vfo_na_bazie_syntezy_dds_ad9850_z_wizualizacją_stanu_pracy_trx_a_na_wyświetlaczu_lcd.jpg
---





 



![](assets/data/img/projects/2013-17-0.jpg) 



Prosty układ VFO DDS
--------------------





 Prosty układ VFO DDS na AD9850. Inspiracją projektu były liczne wersje podobnych rozwiązań opisywane na stronach internetowych,

 z których żadne z nich nie stanowiło wersji pełnej, mogącej spełniać więcej niż jedną z funkcji podstawowych.




##### Elementy składowe modułu




 Prezentowany układ posiada budowę modułową z przeznaczeniem do wykorzystania w prostych Trx\_ach. W jego skład wchodzi:






* syntezer na układzie AD9850,
* wzmacniacz sygnału generowanego na tranzystorze 2N3904,
* wyświetlacz LCD 2x16 znaków, obrazujący aktualną częstotliwość pracy Trx\_a, a także aktualny stan pracy Trx\_a, w tym Smetr w formie bargrafu słupkowego
* sterownik na mikroprocesorze ATmega 168P (328P) z oprogramowaniem napisanym w kompilatorze ARDUINO.




##### Opis działania



###### Modulacja SSB



 Trybem domyślnym pracy układu jest stan Rx dla SSB i częstotliwość wyświetlana wynosi 3.700.00 (kHz), z uwzględnieniem przesunięcia pilota Generatora Fali Nośnej nadajnika o 1.500 kHz dla modulacji SSB.

 Częstotliwość generowana DDS jest większa o wartość pośredniej częstotliwości i wynosi 12.688.400 kHz, przy zastosowanym w prototypie Trx\_a filtrze o Fśr = 8,989,900 kHz.

 Po przejściu na nadawanie informacja o tym stanie jest wyświetlenie na wyświetlaczu trybu pracy „Tx”, poprzez podanie na pin „INP Tx” modułu napięcia stałego w granicach 5-12V (z przekaźnika w układzie Trx\_a).





###### Modulacja CW



 Po podaniu napięcia na pin „INP CW” w granicach 5-12V z układu Trx\_a, wyświetlana częstotliwość uwzględnia tym razem różnicę dla Generatora Fali Nośnej

 przy CW tylko o 800 Hz, a generowana przez DDS jest większa o wartość pośredniej częstotliwości dla wykorzystanego filtru jw. Wyświetlona jest również

 informacja na wyświetlaczu LCD o trybie pracy CW i analogicznie o przejściu na nadawanie jak przy SSB.





###### Smetr w formie wizualnej bargrafu



 Kolejną realizowaną funkcją układu jest prosty, wizualny wskaźnik w formie bargrafu, który można wykorzystać jako wskaźnik sygnału Smetra,

 mocy nadawanej własnego nadajnika, lub obie razem, odpowiednio włączając tą funkcje do układu budowanego Trx\_a. Realizowane jest to poprzez

 podanie na pin „US” napięcia z układu ARW odbiornika w granicach 5-0V. Wartości wyświetlane oblicza procesor w zależności od napięcia
{% include swiatradio.html on_page="05/2014 str. 50-51" %}
 podanego na jedno z jego wejść analogowych. Wartości napięcia wejściowego mogą być modyfikowane programowo, w zależności od potrzeb konstruktora.






Prezentowany układ charakteryzuje wysoka stabilność częstotliwości, może on zadowolić każdego konstruktora prostych układów nadawczo-odbiorczych,

a pisane oprogramowanie w otwartej platformie programistycznej ARDUINO pozwala na wprowadzane dowolnych zmian wg własnego uznania.

Poziom sygnału wyjściowego generatora wynosi 3 Vpp/50ohm i wystarcza do wysterowania diodowego mieszacza budowanego odbiornika lub nadajnika.







![](assets/img/logo/sr_logo_s.jpg)###### 05/2014 str. 50-51

 





 


