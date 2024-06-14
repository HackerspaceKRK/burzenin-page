---
title: Płyta główna TRX 1-500MHz
puk_category: A
puk_year: 2012
puk_place: 2
author: sp7nj
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp7nj_płyta_główna_trx_1_500mhz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp7nj_płyta_główna_trx_1_500mhz.jpg
---





 



![](assets/data/img/projects/2012-2-0.jpg) 



Płyta główna TRX 1..500 MHz
---------------------------





 Zaprojektowana płyta główna jest podstawowym zespołem transceivera **OMEGA** przewidzianego

 do pracy w zakresie od 1 do 500 MHz. Tak szeroki zakres uzyskano poprzez

 zastosowanie mieszaczy diodowych ADE-1 w torze nadawczym i odbiorczym.

 Rozdzielenie torów nadawczego i odbiorczego uprościło konstrukcję i sposób uruchamiania.

 


##### Część odbiorcza




Sygnał z anteny poprzez zespół filtrów pasmowych i przekaźnik przełączający

doprowadzony jest na wejście wzmacniacza w.cz. wykonanego na scalonym układzie

MMIC. W egzemplarzach modelowych zastosowano układy scalone S868. Współczynnik szumów układu wynosi 2,9 dB przy P1db równym 13dB.

Wzmacniacz zapewnia wzmocnienie ok. 20dB. Znormalizowana impedancja we/wy 50 omów pozwala

na łatwe dopasowanie układu do filtrów pasmowych i mieszacza odbiornika.






Następnie sygnał podawany jest na mieszacz diodowy ADE-1. IP3 wynosi 15 dBm, a wzmocnienie przemiany -5dB.

Dopasowanie mieszacza do impedancji filtru kwarcowego wykonane jest poprzez obwód

rezonansowy z dzielnikiem pojemnościowym.






Po filtrze kwarcowym następuje wzmocnienie sygnału na częstotliwości pośredniej,

na wzmacniaczu wykonanym na dwóch układach MMIC (2xS868). Wyjście ostatniego układu

połączone jest bezpośrednio do ukladu ADE-1 pełniącego funkcję *produkt detektora*.






Dalej sygnał podawany jest na uklad scalony SSM2166 - niskoszumny wzmacniacz m.cz. i ukladu automatyki.

Układ pracuje doskonale w tej funkcji, zapewniając duże wzmocnienie 60dB,

niski poziom szumów własnych i odpowiednią stałą czasów zadziałania automatyki.






Pomiędzy produkt detektorem a układem SSM2166 znajdują się złącza umożliwiające

opcjonalne podłączenie filtrów niskiej częstotliwości i wskaźnika SMETR-a.






Wzmacniacz mocy m.cz. wykonano na układzie LM380 zapewniając moc wyjsciową 1W przy impedancji głośnika 8 omów.




##### Część nadawcza




Sygnał z mikrofonu podawany jest na wzmacniacz wykonany na układzie scalonym

TL072. Wzmacniacz kształtuje pasmo przenoszenia w zakresie od 250 Hz do 2,7 kHz,

zapewniając wzmocnienie 23 dB.





{% include swiatradio.html on_page="01/2013 str. 48-52" %}
Ze wzmacniacza mikrofonowego sygnał jest podawany na uklad ADE-1, który pełni funkcję modulatora.

Po modulatorze sygnał doprowadzony jest do filtru kwarcowego i na wzmacniacz pośredniej częstotliwości,

 wykonany na układzie MMIC S868. Wzmacniacz połączony jest do mieszacza na układzie ADE-1. Po mieszaczu sygnał

kierowany jest poprzez przekaźnik na filtry pasmowe. Filtry pasmowe są wspólne dla toru nadawczego i odbiorczego.

Napięcie wyjściowe w.cz. na obciążeniu 50 omów wynosi 0,6 Vpp.






 W egzemplarzach modelowych częstotliwość pośrednia wynosi 10 MHz.

 Na płytce można zastosować różne filtry kwarcowe,

 na przykład 2,4kHz w torze odbiornika i 2,7kHz w torze nadawczym.

 Dodatkowo PCB wyposażona jest w złącza umożliwiające łatwą wymianę

 filtrów kwarcowych.






Zasilanie płytki: od 10V do 15V, wymiary: 70x120 mm.





#### Do pobrania

[Schemat elektryczny płytki (plik PDF)](/assets/bin/SP7NJR_1-500MHz.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 01/2013 str. 48-52

 





 


