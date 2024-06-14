---
title: Warsztatowy miernik mocy w. cz.
puk_category: C
puk_year: 2018
puk_place: 6
author: sp2z
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp2z_warsztatowy_miernik_mocy_w_cz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp2z_warsztatowy_miernik_mocy_w_cz.jpg
---





 



![](assets/data/img/projects/2018-6-0.jpg) 



Warsztatowy miernik mocy w.cz.
------------------------------





 Pomiar mocy w. cz. to jedna z najczęstszych czynności wykonywanych w pracowni radioamatora.

 Celem projektu była konstrukcja miernika mocy w. cz., który zastąpiłby wykorzystywany dotychczas diodowy

 detektor szczytowy, który choć prosty w konstrukcji i użyciu, posiada szereg ograniczeń.






 Miernik stanowi uniwersalny przyrząd pomiarowy przydatny w pracowni każdego radioelektronika.

 Pozwala on na wygodne strojenie np. generatorów i wzmacniaczy, dzięki prezentacji maksymalnego uzyskanego wskazania.

 Prezentacja minimalnego wskazania może okazać się pomocna np. przy konstrukcji filtrów.

 W projekcie przewidziano konieczność podłączania tłumików w celu zwiększenia dostępnego zakresu pomiarowego.

 Wówczas, za pomocą przycisku można wybrać wartość załączonego tłumika, w celu uzyskania dokładnych wskazań.




##### Cechy urządzenia




* zakres dynamiki ok. 70 dBm
* zakres częstotliwości DC-500 MHz (AD8307)
* zasilanie z portu micro USB (zasilacz, powerbank, komputer)
* rozdzielczość pomiaru 0.12 dBm
* czytelny wyświetlacz typu OLED
* prezentacja wyników w jednostkach: dBm, mW, Vpp
* wbudowana obsługa tłumików -40 db, -20 db, -10 db, -6 db, -3 db
* pamięć wskazania maksymalnej i minimalnej mocy
* kalibracja za pomocą multiplatformowej aplikacji okienkowej




##### Schemat




 Schemat elektryczny miernika przedstawiono na rysunku 1.






Sercem urządzenia jest wzmacniacz logarytmiczny firmy Analog Devices - AD8307, który pracuje w szerokim

zakresie częstotliwości i posiada liniową charakterystykę napięcia wyjściowego od przyłożonej mocy.

Pomiar napięcia, konwersja jednostek oraz obsługa peryferiów odbywa się za pomocą układu ESP8266.

Integralną częścią projektu jest aplikacja okienkowa umożliwiająca wygodną kalibrację urządzenia.




##### Opis działania i budowa




Urządzenie oparte jest o układ scalony AD8307 firmy Analog Devices. Jest to wzmacniacz logarytmiczny o bardzo dużym wzmocnieniu,

pracujący w szerokim zakresie częstotliwości (DC-500 MHz). W wyniku pomiaru mocy sygnału w.cz. na wyjściu układu otrzymuje się

sygnał napięciowy proporcjonalny do mocy wyrażonej w dBm. Układ AD8307 charakteryzuje się znakomitą stabilnością temperaturową

(rysunek 2) oraz niewielką zmianą offsetu w funkcji częstotliwości (rysunek 3). W zakresie od 1MHz do 15MHz, nie zaobserwowano

mierzalnych zmian napięcia wyjściowego.






{% include swiatradio.html on_page="11/2018 str. 52-53" %}rnika analogowo-cyfrowego

modułu ESP82662 na platformie NodeMCU3. Algorytm oblicza średnią uciętą, w celu wyeliminowania wyników odstających

i możliwie dokładnego oszacowania rzeczywistej wielkości napięcia. Po wykonaniu konwersji jednostek4,

wynik jest prezentowany na wyświetlaczu OLED sterowanym za pomocą protokołu I2C. Jednocześnie w każdej iteracji zachowywana

i prezentowana jest największa i najmniejsza zmierzona wartość.






Przycisk umożliwia korekcję wskazań o wartość wybranego tłumika.

Ten sam przycisk, wciśnięty w momencie prezentacji ekranu startowego, pozwala na wejście w tryb kalibracji (opis kalibracji w załączonym pliku pdf).





#### Do pobrania

[SP2Z PowerMeter (plik pdf)](assets/data/download/SP2Z_PowerMeter.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 11/2018 str. 52-53

 





 


