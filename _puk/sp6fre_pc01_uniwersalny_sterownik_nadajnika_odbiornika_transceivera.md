---
title: PC01 - uniwersalny sterownik TX/RX/TRX
puk_category: D
puk_year: 2017
puk_place: 12
author: 
  - sp6fre
tagline: ""
layout: puk
proofread: yes
classes: wide
header:
  overlay_image: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera.jpg
gallery1:
  - url: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_2.jpg
    image_path: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_2.jpg
  - url: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_3.jpg
    image_path: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_3.jpg
  - url: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_4.jpg
    image_path: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_4.jpg
  - url: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_5.jpg
    image_path: /assets/images/puk/sp6fre_pc01_uniwersalny_sterownik_nadajnika_odbiornika_transceivera_5.jpg
---

Uniwersalny sterownik PC01
--------------------------

PC01 to zespolony sterownik urządzeń radiowych (odbiornik, nadajnik, transceiver), wykorzystujący do sterowania niemal wyłącznie ekran dotykowy kolorowego wyświetlacza, pozwalający na wykorzystanie różnych, dostępnych sygnałów heterodyny oraz oferujący pełny zestaw sygnałów sterujących dla pozostałych elementów układu radiowego.

##### Funkcje układu

* Strojenie z krokiem od 10Hz do 1MHz za pomocą impulsatora lub ekranu dotykowego
* Sygnalizacja binarna rodzaju emisji, stanu O/N, sterowanie do 10 pasm pracy
* Pomiar SWR i mocy na wyjściu z możliwością definiowania punktu odniesienia
* Pomiar siły odbieranego sygnału z kalibracją dla każdej wartości S1-9 oraz S+ i S++
* Pamięć do 9 częstotliwości pracy
* Wbudowany klucz elektronowy




##### Koncepcja rozwiązania

Podstawą układu jest procesor ATmega 128 umieszczony na płytce przejściowej ze złączami szpilkowymi. Płytka główna jest wspornikiem dla wyświetlacza ILI9325 (kolorowy wyświetlacz 320/240 4.3” z ekranem dotykowym) oraz dla impulsatora i dwóch potencjometrów (w założeniu do regulacji wzmocnienia w.cz. i m.cz). Układ zastosowany z dodatkową płytką połączeniową może stanowić wygodny zestaw uruchomieniowy niemal każdego typu urządzenia. Układ zaprojektowany został do współpracy z typową obudową metalową o wymiarze płyty czołowej 65x140 mm. Obudowa ta dostępna jest w trzech wymiarach głębokości co pozwala na budowę urządzeń o różnym stopniu skomplikowania.

Schemat blokowy urządzenia pokazany jest na rysunku 6, schemat elektryczny na rysunku 5.

Pełny opis w załączonej dokumentacji i na stronie internetowej SP6FRE.

{% include swiatradio.html on_page="09/2018 str. 46-50 (cz. 1), 10/2018 str. 42-43 (cz. 2)" %}

{% include gallery id="gallery1" %}

#### Odnośniki

[Dokumentacja PC-01 - opis konkursowy - plik pdf](/assets/bin/SP6FRE_Sterownik PC01.pdf)

[Wątek o sterowniku PC-01 na forum SP Home Made](http://www.sp-hm.pl/thread-2999.html)

