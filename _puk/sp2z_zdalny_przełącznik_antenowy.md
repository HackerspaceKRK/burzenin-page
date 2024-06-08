---
title: Zdalny przełącznik antenowy
puk_category: B
puk_year: 2019
puk_place: 5
author: sp2z
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp2z_zdalny_przełącznik_antenowy.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp2z_zdalny_przełącznik_antenowy.jpg
---





 



![](assets/data/img/projects/2019-5-0.jpg) 



Zdalny przełącznik antenowy
---------------------------





 Urządzenie do przełączania pomiędzy antenami przy wykorzystaniu już istniejącej infrastruktury.

 Priorytetem konstrukcyjnym była łatwość integracji z istniejącą instalacją antenową,

 w szczególności brak konieczności prowadzenia dodatkowych przewodów do zasilania i sterowania.




 Urządzenie ma za zadanie umożliwić przełączania pomiędzy antenami przy wykorzystaniu

 już istniejącej infrastruktury. Priorytetem jest łatwość integracji z istniejącą instalacją antenowa,

 w szczególności brak konieczności prowadzenia dodatkowych przewodów do zasilania i sterowania urządzeniem.

 




 Schemat układu przedstawiono na rysunku 1.

 




 Urządzenie oparte jest o układ ESP82661 wyposażony w moduł WiFi z wyprowadzonym złączem antenowym,

 pozwalającym na wpięcie zewnętrznej anteny. ESP8266 ma zaimplementowany stos TCP/IP.

 Firmware (napisane w języku microPython2) umożliwia uruchomienie serwera DHCP oraz prostego

 serwera www o podstawowych

 funkcjonalnościach. Formularz publikowany przez urządzenie jako strona www (interfejs użytkownika

 przedstawia rysunek 3), pozwala na wybranie przycisku, który

 wyzwala przełączenie przekaźników przez mikrokontroler.

 




 Urządzenie zasilane jest przez fider antenowy za pomocą sprzęgacza. Po podłączeniu

 zasilania moduł ESP-12 rozsyła informację o dostępności punktu dostępowego o nazwie

 AntennaSwitch. Dostęp do sieci wifi zabezpieczony jest protokołem WPA2. Po wprowadzeniu
{% include swiatradio.html on_page="2/2020 str. 47-48" %}
 hasła użytkownik dostaje dostęp do sieci wewnętrznej, w której pod adresem 192.168.4.1

 uruchomiona jest aplikacja sterująca przełącznikiem antenowym. 




 Dodatkową funkcjonalnością przełącznika antenowego jest pomiar

 temperatury wewnątrz obudowy za pomocą termometru cyfrowego DS18B20.

 



#### Do pobrania

[Opis konkursowy projektu (plik pdf)](assets/data/download/SP2Z_ZdalnyPrzelacznikAntenowy.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 2/2020 str. 47-48

 





 


