---
title: Modyfikacja analizatorów z serii NWT
puk_category: C
puk_year: 2013
puk_place: 11
author: sq4avs
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq4avs_modyfikacja_analizatorów_z_serii_nwt.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq4avs_modyfikacja_analizatorów_z_serii_nwt.jpg
---





 



![](assets/data/img/projects/2013-11-0.jpg) 



Modyfikacja analizatora NWT7
----------------------------





 Propozycja kilku modyfikacji układowych popularnych analizatorów NWT7, poprawiających ich funkcjonalność i parametry techniczne.

 




 W ramach projektu wykonano następujące modyfikacje:

 

* Usunięto wzmacniacz na wyjściu generatora DDS, co spowodowało obniżenie poziomu harmonicznych generatora do poziomu harmonicznych

 samego DDS-a. Wzmacniacz MMIC zastosowany w tym miejscu był ich głównym źródłem w oryginalnym układzie, nierzadko

 spotykało się wykonania NWT z poziomem drugiej harmonicznej większym od -30dB względem częstotliwości generowanej,

 co znacznie obniżało dynamikę pomiarową. Wyjście generatora jest wykonane jako symetryczne ,co nie tylko podnosi

 poziom sygnału użytecznego, ale znacznie redukuje poziom sygnałów niepożądanych w widmie syntezera.
* Zastosowano tłumik stały 10dB na wyjściu generatora, co spowodowało poprawę dopasowania i obniżenie poziomu sygnałów

 wyjściowych do około -7dBm. Obniża to ryzyko przesterowania i uszkodzenia badanych układów.
* Na wejściu układu AD8307 zastosowano wzmacniacz ERA-5 o wzmocnieniu 20dB, poprzedzony tłumikiem 6dB.

 Takie rozwiązanie poprawia dopasowanie wejścia i chroni układ wzmacniacza MMIC.

 Zastosowany wzmacniacz chroni kosztowny detektor AD8307 a jednocześnie wzmacnia sygnał mierzony tak, aby go

 dopasować do optymalnego zakresu pracy detektora. Wzmacniacz zastosowany w tym miejscu nie ma już praktycznie

 żadnego wpływu na poziom harmonicznych pokazywanych przez analizator.
* Umieszczenie sondy jako oddzielnego modułu poprawiło ekranowanie między blokami. Najpodatniejszym elementem na uszkodzenie stał się

 teraz tani układ MMIC. W razie potrzeby można szybko wymienić sondę na drugi egzemplar gdyż jest ona łatwo odłączalna.









Zastosowane modyfikacje poprawiają dynamikę pomiarową i zmniejszają poziom harmonicznych w widmie wyjściowym. Poprawiają również izolację

między generatorem a sondą, dzięki rozdzieleniu obu układów. Zmniejszona została również moc wyjściowa generatora, przy zachowaniu czułości porównywalnej

 do układu niemodyfikowanego. Zabezpiecza to mierzone układy przed przesterowaniem. Wzmacniacz MMIC znajduje się teraz na

 *wejściu* sondy z układem AD8307 a nie na *wyjściu* generatora DDS. Ułatwione zostało również serwisowanie całego układu.



 




 


