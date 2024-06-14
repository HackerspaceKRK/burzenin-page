---
title: Prosty, wielopasmowy transceiver CW
puk_category: A
puk_year: 2012
puk_place: 1
author: sp6fre
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6fre_prosty_wielopasmowy_transceiver_cw.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6fre_prosty_wielopasmowy_transceiver_cw.jpg
---





 



![](assets/data/img/projects/2012-1-0.jpg) 



Wielopasmowy TRX CW
-------------------





 Modularne urządzenie składające się z płyty bazowej odbiornika z nadajnikiem oraz z dodatkowej płytki pośredniej na której można zamontować 3

 komplety obwodów wejściowych i wyjściowych. Odbiornik powstał w wyniku dyskusji na forum SP Home Made na bazie konstrukcji opracowanej w Rosji przez W. Poljakowa.






 Oryginalna konstrukcja jest urządzeniem o bezpośredniej przemianie częstotliwości i unikalnych własnościach dotyczących selektywności przy kluczowaniu detektora sygnałem heterodyny.

 Autorskim wkładem SP6FRE jest zastosowanie systemu ARW z tranzystorem FET w układzie regulacji wzmocnienia o bardzo dobrej charakterystyce regulacji.






 Odbiornik został uzupełniony o część nadawczą co sprawia, że powstał kompletny transceiver CW. Do pracy niezbędny jest sygnał heterodyny,

 który zapewnia "TinyDDS bis" (zob. wątek na SP Home Made).

 






Transceiver wykonany został jako urządzenie modularne składające się z płyty bazowej

odbiornika z nadajnikiem oraz z dodatkowej płytki pośredniej, na której można zamontować trzy

komplety obwodów wejściowych i wyjściowych. W najprostszej konfiguracji urządzenie wymaga

do pracy jedynie obwodów wejścia i wyjścia dla jednego pasma. W układzie nadajnika

zastosowany został pojemnościowy system kształtowania impulsu klucza w bramce tranzystora

polowego oraz monitor m.cz pomocny podczas nadawania.






Automatyką transceivera steruje układ TinyDDS bis, co pozwala na realizację opóźnienia

przy przejściu z nadawania na odbiór, przełączenie częstotliwości nadawania i odbioru o ok. 800 Hz.

Upraszcza to strojenie się do korespondenta. Sterownik syntezy przełącza również automatycznie

wejściowe filtry pasmowe i wyjściowe filtry dolnoprzepustowe, a granice przełączenia częstotliwości

to 5.5MHz oraz 11MHz.






Płytki transceivera oraz generator DDS zamontowane zostały w obudowie metalowej o

wymiarach 140x65x140 mm. Generator DDS wraz z regulatorami wzmocnienia i pokrętłem strojenia

(impulsator) zamontowany został na płycie przedniej, a gniazda wyprowadzone są na tylnej ściance

obudowy.






Zasilanie urządzenia to 12V, najlepiej z akumulatora lub z zasilacza o bardzo dobrej

filtracji ze względu na podatność toru m.cz. na przydźwięki sieci.
{% include swiatradio.html on_page="04/2013 str. 52-53" %}





Klawiatura pozwala na regulację kroku strojenia (klawisz STEP). Można też użyć impulsatora z

wciśniętym klawiszem FUN, zmianę pasma w cyklu 3.5->7->14->3.5 itd. za pomocą klawisza

MODE, wybór VFO za pomocą klawisza F1/F2 oraz zrównanie częstotliwości VFO1 i VFO2 za

pomocą klawisza Fx=Fy.







#### Odnośniki

[Wątek dyskusyjny na SP Home Made](http://sp-hm.pl/thread-1326.html)

[Wątek na cqham.ru o odbiorniku przemiany bezpośredniej US5MSQ](http://www.cqham.ru/trx92_13.htm)

[Tiny DDS (SP6FRE) - wątek na SP Home Made](http://sp-hm.pl/thread-1364.html)

[Tiny DDS na stronie SP6FRE](http://lx-net.pl/hr/dds/tiny_dds.html)

 



![](assets/img/logo/sr_logo_s.jpg)###### 04/2013 str. 52-53

 





 


