---
title: EmCom DIGI APRS dla infrastruktury sieci ratunkowej
puk_category: D
puk_year: 2019
puk_place: 21
author: sq9mdd
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq9mdd_emcom_digi_aprs_dla_infrastruktury_sieci_ratunkowej.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq9mdd_emcom_digi_aprs_dla_infrastruktury_sieci_ratunkowej.jpg
---





 



![](assets/data/img/projects/2019-21-0.jpg) 



EmComm DIGI APRS
----------------





 DIGI APRS jest to element infrastruktury RADIOWEJ sieci APRS i ma za zadanie

 przekazywać dane pakietowe pomiędzy stacjami tej sieci.

 Wersja przewoźna którą można uruchomić w terenie klęski żywiołowej, lub na obszarze

 poszukiwań ma za zadanie wspomagać pracę z urządzeń przenośnych i przewoźnych.

 Dzięki możliwości połączenia się z urządzeniem za pomocą sieci WiFi możliwa jest

 równoległa praca operatora z aplikacji APRSIS32 lub APRS Droida






Urządzenie DIGI APRS powstało w odpowiedzi na zapotrzebowanie grup poszukiwawczo-ratowniczych

na Jurze Krakowsko-Częstochowskiej w 2018 roku. Pierwsza wersja DIGI została przetestowana

z powodzeniem podczas kolejnej edycji ćwiczeń wiosną 2019 roku.

Długotrwałe testy terenowe podczas spotkania TAMA APRS 2019 w Bornym

Sulinowie zweryfikowały budowę mechaniczną i tak powstała ostateczna wersja DIGI.




##### Budowa mechaniczna




 Urządzenie jest zamknięte w hermetycznej, łatwej w transporcie, skrzynce wyposażonej

w odpowiednie gniazda zasilania i antenowe. Całość jest konstrukcją zwartą,

gotową do użycia po zasileniu i podłączeniu systemu antenowego.






 Jako bazę montażową urządzenia użyta została walizka ochronna Hard Head o

wymiarach 460mm x 380mm x 170mm. Wszystkie elementy składowe zostały

przymocowane do płyty montażowej wykonanej z polakierowanej sklejki o wymiarach

430mm x 290mm, która stanowi jednocześnie panel frontowy wnętrza skrzynki.




##### Elementy składowe




* zasilacz 12V, 15A
* radiotelefon przewoźny motorola MC2100
* interfejs separująco-sterujący
* raspberry pi v.3 B+
* gniazdo antenowe
* wyłączniki zasilania z podświetlaniem
* gniazda zasilające 12V i 230V
* wyświetlacz LCD Nextion
* karta muzyczna ze złączem USB






Schemat połączeń pokazano na rysunku 2.




##### Rozwiązania programowe




Sercem rozwiązania jest oprogramowanie APRX, które zawiaduje pracą DIGI.

Zamiast sprzętowego modemu TNC użyte zostało oprogramowanie DIREWOLF, które

używa karty muzycznej do dekodowania i enkodowania ramek protokołu APRS.

Sterowanie PTT radia zostało zrealizowane za pomocą złacza GPIO mikrokomputera

raspberry pi.






{% include swiatradio.html on_page="11/2019 str. 47" %}e do zmiany konfiguracji DIGI,

oraz do obslugi wyświetlacza dotykowego.

Dzięki zastosowaniu TNC Proxy wszystkie te aplikacje komunikują się ze sobą.

Zarówno TNC Proxy jak i inne skrypty bazują na bibliotekach napisanych przez Tomka

SQ5T, które są do pobrania z serwisu GITHUB.






Diagram przepływu danych pokazano na rysunku 3.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SQ9MDD_emcom-digi-aprs.pdf)




#### Odnośniki

[Oprogramowanie dla EmCom DIGI APRS (github)](https://github.com/SQ9MDD/EmComm-Off-Grid-DIGI-Project)

 



![](assets/img/logo/sr_logo_s.jpg)###### 11/2019 str. 47

 





 


