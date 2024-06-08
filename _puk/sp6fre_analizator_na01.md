---
title: Analizator NA01
puk_category: C
puk_year: 2011
puk_place: 4
author: sp6fre
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6fre_analizator_na01.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6fre_analizator_na01.jpg
---





 



![](assets/data/img/projects/2011-4-0.jpg) 



Analizator NA01
---------------





 NA01 to prosty wielofunkcyjny miernik działający w paśmie od 500kHz do 30MHz, ułatwiający pracę

 konstruktora sprzętu krótkofalarskiego przez zobrazowanie charakterystyk amplitudowych w funkcji częstotliwości,

 umożliwiający pomiar mocy i WFS, pomagający ustalić parametry obwodów rezonansowych, a także pełniący podstawowe funkcje analizatora widma.




##### Budowa przyrządu




 Schemat elektryczny pokazano na rysunku 2.






 Układ oparty jest o mikroprocesor **ATmega32**, działający jako kontroler wyświetlacza, sterownik

układu DDS oraz kontroler logiki systemu. Układ jest niezależny, choć planowane jest połączenie go z

komputerem PC w celu poszerzenia funkcjonalności i jakości obrazowania wyników. Do obsługi

wykorzystywany jest zespół 5 klawiszy. Układ zasilany jest z zewnętrznego zasilacza

12V/0.5A, ale może być również zasilany z wewnętrznej baterii 10\*1.2V/0.7A. Pobór prądu wynosi

ok. 230mA.






 Mikroprocesor ATmega32 steruje generatorem DDS na układzie **AD9834** wypracowując

 częstotliwości pomiarowe oraz ich cykl zmienności w czasie. Sygnał ten jest dalej wzmacniany za

 pomocą układu **AD8014** i wyprowadzony jest na gniazdo wyjściowe miernika skąd

 doprowadzany jest do wejścia badanego układu.






 Wejście miernika to logarytmiczny wzmacniacz sygnału skutecznego **AD8307**, który mierzy

sygnał skuteczny na wyjściu badanego układu. Napięcie na wyjściu AD8307 związane jest z mocą

sygnału wejściowego w relacji 5mV napięcia na 1dB różnicy poziomu mocy na wejściu. Napięcie to

mierzone jest przez mikrokontroler poprzez port A/D o dokładności przetwarzania 10 bitów (1024

kroki dla napięcia 5V) a następnie odpowiednio przeliczane i prezentowane w formie graficznej

jako przebieg mierzonego parametru w funkcji częstotliwości.

{% include swiatradio.html on_page="01/2012 str. 48-53" %}




 Sposób wykonania płytki drukowanej przyrządu oraz użytkowanie przedstawione są w opisie konkursowym.



 
#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SP6FRE_Analizator-NA01.pdf)




#### Odnośniki

[Opis analizatora NA01 na stronie SP6FRE](http://lx-net.pl/hr/netw/na01.html)

 



![](assets/img/logo/sr_logo_s.jpg)###### 01/2012 str. 48-53

 





 


