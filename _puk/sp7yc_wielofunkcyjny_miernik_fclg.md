---
title: Wielofunkcyjny miernik FCLG
puk_category: C
puk_year: 2013
puk_place: 10
author: sp7yc
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7yc_wielofunkcyjny_miernik_fclg.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7yc_wielofunkcyjny_miernik_fclg.jpg
---





 



![](assets/data/img/projects/2013-10-0.jpg) 



Wielofunkcyjny miernik FCLG
---------------------------





 Opisywany miernik pozwala mierzyć częstotliwość, częstotliwość rezonansową obwodów LC, indukcyjność, pojemność kondensatorów

 (również kondensatorów elektrolitycznych). Może służyć jako generator częstotliwości do 1 MHz, tester tranzystorów,

 tester rezonatorów kwarcowych.






Miernik został opracowany na podstawie konstrukcji "Частотомер, измеритель ёмкости и индуктивности, генератор", dostosowanej do bieżących potrzeb

przy zachowaniu ogólnej koncepcji budowy. Zrezygnowano z niektórych funkcji i dodane zostały nowe, przydatne w pracach warsztatowych.

Dodana została funkcja pomiaru częstotliwości rezonansowej obwodów LC, a jako preskaler wykorzystano obwód SAB5664.

Zmieniony został układ testera kwarców, zastostowano gniazdo wejściowe BNC częstościomierza przełączane przekaźnikiem

oraz dostosowano układ komutacji do zmienionej konfiguracji. Dodano również prosty sprawdzian tranzystorów,

 pozwalający określić typ tranzystora (NPN/PNP) oraz topografię jego wyprowadzeń.






##### Parametry funkcjonalne





* Pomiar częstotliwości (wejście na gnieździe BNC) w zakresie 0..1000 MHz w dwóch podzakresach F1 i F2.

 Podzakres F1: 0..40 MHz, podzakres F2: 40..1000 MHz.

 Czas bramkowania na zakresie F1: 0,2..1..10 sek. wybierany przyciskiem „+” , ”-„
* Pomiar pojemności w zakresie od 1pF do 10000µF (w trzech podzakresach z

 wykorzystywaniem różnych metod pomiarowych): gniazdo "Lx/Cx" 1pF..1µF, gniazdo "C(µF)>0,1"/zakres\_1 0,1µF..1000µF,

 gniazdo "C(µF)>0,1"/zakres\_2 0,1..10000µF.
* Pomiar indukcyjności w zakresie 0,1µH..5H (gniazdo "Lx/Cx").
* Generacja częstotliwości od 244Hz do 1MHz z cyfrowym odczytem częstotliwości (wyjście na nieździe "Ton").
* Pomiar rezonansu rezonatora kwarcowego oraz rezonansu ze znaną pojemnością

 szeregową (33 pF). Te pomiary są wykorzystywane przy doborze kwarców do filtrów drabinkowych.
* Sprawdzanie rezonansu obwodów LC (np. filtrów p.cz). Jest to bardzo wygodna opcja

 pozwalająca sprawdzić przed montażem rezonans montowanego obwodu i zakres jego przestrajania.

 Częstotliwość rezonansowa wyświetlana jest na wyświetlaczu. Zakres oscylacji generatora do 200 MHz.

 Badany obwód podłączamy do gniazda "Gen HF/RF".
* Określenie wyprowadzeń tranzystorów (E/B/C) oraz typu tranzystora (NPN/PNP).







##### Zasada pracy urządzenia




Podstawowym zespołem miernika jest licznik częstotliwości zbudowany na procesorze PIC16F628A.

Do jego wejścia (pin 3) poprzez układy komutacji (SN74HC153D i 74AC14SC) dołączane są wybrane bloki pomiarowe.

Przy pomiarze częstotliwości F1 sygnał z gniazda wejściowego poprzez bierne styki przekaźnika idzie do wzmacniacza wstępnego

i dalej do układu komutacji.






 Przy pomiarze częstotliwości F2 sygnał przełączany jest na preskaler SAB5664 i po podzieleniu (podział przez 64)

 oraz wzmocnieniu przez tranzystor wzmacniacza wstępnego BF998 przekazywany jest do układu komutacji.

 Zasilanie wzmacniacza wstępnego lub preskalera wybierane jest przełącznikiem „F1/F2”.






Pomiar pojemności (do 1 µF) i indukcyjności zrealizowany jest na komparatorze LM311.

Schemat i zasada pracy były wielokrotnie publikowane. Na uwagę zasługuje tylko wykorzystanie diody zamiast przekaźnika

do przyłączania kondensatora 1nF do obwodu. Sygnał z pinu 7 komparatora poprzez opornik 470 Ω przekazywany jest do układu komutacji.






Pomiar kwarców odbywa się na odrębnym generatorze. Możliwy jest pomiar rezonansu kwarcu poprzez przyłączenie kwarcu między

bazę tranzystora a masę, oraz rezonansu z szeregową pojemnością 33 pF. Te dwa pomiary pozwalają określić parametry

kwarcu do obliczania filtrów drabinkowych.
{% include swiatradio.html on_page="04/2014 str. 48-51" %}





Pomiar rezonansu obwodów LC zbudowany jest na zastępczym układzie diody Lambda. Układ łatwo się wzbudza w szerokim zakresie częstotliwości

 (aż do 200 MHz). Przez przyłączenie do wejścia nieznanego obwodu LC można określić jego częstotliwość rezonansową.

 Bardzo się przydaje przy pomiarze zaekranowanych obwodów np. „kubków” p.cz.

 


##### Oprogramowanie



 Najnowsze wersje oprogramowania (firmware) dla procesora PIC16F628A można pobrać z rosyjskiej strony źródłowej.





 
#### Do pobrania

[Opis konkursowy miernika FCLG (plik .PDF)](/assets/bin/SP7YC_FCLG-meter.pdf)

[Program dla mikroprocesora (ver.2.5 - plik .HEX)](/assets/bin/SP7YC_lcfg2.5auto.hex)




#### Odnośniki

[Oryginalny opis miernika](http://pic.rkniga.ru/shemotehnika/izmeritelnaya-tehnika/242-izmeritel-lcfg-na-mikrokontrollere-pic16f628a.html)

 



![](assets/img/logo/sr_logo_s.jpg)###### 04/2014 str. 48-51

 





 


