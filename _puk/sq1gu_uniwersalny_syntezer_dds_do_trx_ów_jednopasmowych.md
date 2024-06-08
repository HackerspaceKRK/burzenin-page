---
title: Uniwersalny syntezer DDS do TRX-ów jednopasmowych
puk_category: D
puk_year: 2012
puk_place: 15
author: sq1gu
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq1gu_uniwersalny_syntezer_dds_do_trx_ów_jednopasmowych.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq1gu_uniwersalny_syntezer_dds_do_trx_ów_jednopasmowych.jpg
---





 



![](assets/data/img/projects/2012-15-0.jpg) 



Uniwersalny syntezer DDS do TRX jednopasmowych
----------------------------------------------





 Syntezer wykonany na module AD9850 procesor sterujący ATmega8 i wyświetlacz LED sterowany poprzez MAX7219.

 Syntezer obsługuje się jednym enkoderem z przyciskiem. Z menu można wybrać dowolne pasmo pracy oraz częstotliwość pośrednią.




##### Budowa i działanie układu




Syntezer składa się z dwóch modułów: płytki LCD i płytki DDS/procesora.

Oba moduły zasilane są napięciem 5V. Do płytki procesora podłączamy również 12V –

służy ono do monitorowania stanu zasilania. Jeśli napięcie zasilania spadnie poniżej 8V, to

 procesor zapamiętuje częstotliwość pracy zanim zasilanie całkiem zniknie.

 Jeśli nie podłączymy tego wyprowadzenia to funkcja pamięci będzie nieaktywna i

 przy każdym włączeniu układ będzie się ustawiał na częstotliwości startowej.

 Oczywiście pasmo, krok, częstotliwość pośrednia i jasność będą prawidłowo zapamiętywane.






Procesor steruje wyświetlaczem za pomocą trzech lini sterujących: DIN, CLK, LOAD.

Do płytki procesora podłączony jest enkoder obrotowy z przyciskiem.






Po podłączeniu zasilania, jeśli w pamięci EEPROM procesora nie ma żadnych nastaw,

wyświetla się na wyświetlaczu litera E i następuje inicjalizacja pamięci. Układ jest gotowy do pracy.






Kręcąc gałką zmieniamy częstotliwość, przyciskając przycisk enkodera zmieniamy krok przestrajania (10Hz,100Hz,1kHz,10kHz).

Przyciskając przycisk enkodera dłużej, wchodzimy w regulację jasności wyświetlacza (16 poziomów jasności).




##### Ustawienie pasma i pośredniej




 Wciskamy przycisk enkodera i włączamy zasilanie. Wyświetla się P1 i aktualnie ustawione pasmo.

 Kręcąc gałką wybieramy pasmo. Następnie wciskamy przycisk enkodera i trzymamy aż pojawi się P2,

 puszczamy i pojawia się aktualna częstotliwość pośredniej. Ustawiamy żądaną częstotliwość gałką

 (krótkie naciśnięcie przycisku enkodera zmienia krok).

 




 Przyciskamy przycisk enkodera i trzymamy aż pojawi się P3, gałką wybieramy minus albo nic.

Jeśli minus to częstotliwość pośrednia będzie odejmowana, a jak nic to dodawana.






Ponownie przyciskamy przycisk enkodera i układ przechodzi do normalnej pracy z nowymi nastawami.

{% include swiatradio.html on_page="04/2013 str. 48-49" %}



##### Reset




 Jeśli zajdzie taka potrzeba można wykonać reset procesora i skasowanie nastaw do ustawień fabrycznych.

 Zwieramy pin reset na płytce do masy i włączamy zasilanie. Pojawi się litera E na wyświetlaczu

 i po chwili układ startuje na paśmie 80m z częstotliwościa pośrednią 6 MHz.

 








#### Odnośniki

[Opis syntezera na stronie SQ1GU](http://sq1gu.tobis.com.pl/pl/syntezery-dds/31-syntezer-dds-v3)

 



![](assets/img/logo/sr_logo_s.jpg)###### 04/2013 str. 48-49

 





 


