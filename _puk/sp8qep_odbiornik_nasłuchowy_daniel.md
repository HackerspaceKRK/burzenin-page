---
title: Odbiornik nasłuchowy DANIEL
puk_category: A
puk_year: 2018
puk_place: 1
author: sp8qep
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp8qep_odbiornik_nasłuchowy_daniel.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp8qep_odbiornik_nasłuchowy_daniel.jpg
---





 



![](assets/data/img/projects/2018-1-0.jpg) 



"Daniel" - jednopasmowy odbiornik SSB
-------------------------------------





 Klasyczna konstrukcja jednopasmowego odbiornika z pojedynczą przemianą częstotliwości,

 drabinkowym filtrem kwarcowym, mieszaczach NE612 i VFO z wykorzystaniem generatora DDS.

 Łatwa do powielenia i uruchomienia, moze służyć jako urządzenie treningowe dla początkujacych

 krótkofalowców lub jako odbiornik "wyjazdowo-urlopowy".




##### Parametry funkcjonalne




* odbiornik foniczny (SSB), jednopasmowy (80m/40m/20m)
* dwa stabilne VFO (A/B) - synteza częstotliwości DDS
* miernik siły sygnału (SMETR)
* automatyczna regulacja wzmocnienia (ARW)
* czytelny wyświetlacz typu OLED, przeszklony wierzch obudowy
* zasilanie: 9-15V przy poborze prądu max. 200mA




##### Opis działania i budowa




 Schemat elektryczny miernika przedstawiono na rysunku 1.






Sygnał z anteny podawany jest na filtr pasmowo-przepustowy (BPF) składający się z elementów C1-C6,

L1, TR1, skąd trafia do pierwszego mieszacza zrealizowanego na układzie U1 (NE612). Na drugie

wejście mieszacza podawany jest sygnał z przestrajanego generatora DDS. W wyniku mieszania

otrzymujemy sygnał pośredniej częstotliwości (p.cz.) 10MHz, który kierowany jest do filtra

kwarcowego zbudowanego z elementów X1-X5, C10-C15, R3,R4.






Dopasowanie impedancji wyjściowej mieszacza do impedancji wejściowej filtra kwarcowego zapewnia transformator TR2. Z wyjścia filtra

kwarcowego sygnał p.cz. kierowany jest do drugiego mieszacza zbudowanego na układzie U2 (NE612),

gdzie mieszany jest z sygnałem fali nośnej wytworzonym w generatorze BFO składającym się z

elementów X6, C17-C20 oraz elementów wchodzących w skład struktury układu scalonego U2. Na

wyjściu mieszacza U2 otrzymujemy min. sygnał akustyczny (małej częstotliwości), który jest

wzmacniany oraz filtrowany w układzie ze wzmacniaczem operacyjnym U3A i U3B (NE5532).

Następnie poprzez potencjometr AF GAIN służący do regulacji głośności, sygnał akustyczny trafia do

wzmacniacza m.cz. zbudowanego z wykorzystaniem układu U4 (TDA7052A).






Tranzystory T1 i T2 wraz z elementami pomocniczymi tworzą pętlę układu automatycznej regulacji

wzmocnienia (ARW). Sygnał akustyczny z U3B wzmocniony przez tranzystor T2 i prostowanyw

prostowniku dwupołówkowym na diodach D3, D4 wykorzystywany jest do ładowania kondensatora

C31, który wraz z rezystorami R5 i R2 decyduje o stałej czasowej ARW. Tranzystor T1 pod wpływem

napięcia z C31 powoduje zmniejszenie wzmocnienia układu U1. Potencjometr AGC służy do ustawienia

progu działania układu ARW.






Sygnał m.cz. jest również kierowany za pośrednictwem potencjometru SMETR\_SENS do procesora IC1

(Atmega328). Procesor IC1 realizuje kilka funkcji, min. steruje wyświetlaczem OLED (poprzez

magistralę I2C) na którym wyświetlana jest min. siła sygnału. Procesor również steruje (za pomocą

magistrali SPI) układem U5 (AD9833), który pełni rolę generatora VFO. Przebieg zegarowy dla

AD9833 uzyskiwany jest z generatora kwarcowego OSC1 o częstotliwości 24MHz, natomiast procesor

IC1 (Atmega328) jest taktowany z własnego, wewnętrznego generatora.






Układ U5 (AD9833) wytwarza na swoim wyjściu sygnał o przebiegu sinusoidalnym, jednak jego widmo

zawiera szereg częstotliwości harmonicznych, dlatego zastosowałem filtr dolnoprzepustowy zbudowany

z elementów C42, IND1, C43, IND2, C44, R21. Odfiltrowany sygnał z DDS jest wzmacniany za

pośrednictwem tranzystora T3. Tak ukształtowany sygnał podawany jest na wejście pierwszego

mieszacza U1 (NE612). Rezystory R25 i R26 tworzą tłumik, którym można zmniejszyć poziom sygnału,

{% include swiatradio.html on_page="08/2018 str. 44-50" %}






Część radiowa układu zasilana jest poprzez stabilizator LDO LM2940-8.

Można w tym miejscu zamontować również układ 7808 (układ wyprowadzeń oraz obudowa są

identyczne), jednak wtedy minimalne napięcie zasilania będzie nieco wyższe. Również układ pomiaru

napięcia będzie miał prawidłowe wskazania dla napięć >9V (przy LM2940-8 pomiar napięcia jest

poprawny od 7V).






Część cyfrowa zasilana jest poprzez oddzielny stabilizator LM1117-5.





#### Do pobrania

[RX "Daniel" - instrukcja montażu](assets/data/download/SP8QEP_RX-DANIEL-instrukcja.pdf)

[RX "Daniel" - oprogramowanie dla pasma 80m](assets/data/download/SP8QEP_RX-DANIEL-v174_80m.zip)

[RX "Daniel" - oprogramowanie dla pasma 20m](assets/data/download/SP8QEP_RX-DANIEL-v174_20m.zip)




#### Odnośniki

[Wpisy o RX "Daniel" na blogu SP8QEP](https://sp8qep.wordpress.com/tag/odbiornik-ssb-daniel/)

[Wątek o odbiorniku na grupie SP Home Made](http://sp-hm.pl/thread-3181.html)

 



![](assets/img/logo/sr_logo_s.jpg)###### 08/2018 str. 44-50

 





 


