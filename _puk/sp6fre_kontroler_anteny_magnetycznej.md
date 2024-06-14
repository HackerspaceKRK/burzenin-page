---
title: Kontroler anteny magnetycznej
puk_category: B
puk_year: 2016
puk_place: 8
author: sp6fre
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6fre_kontroler_anteny_magnetycznej.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6fre_kontroler_anteny_magnetycznej.jpg
---





 



![](assets/data/img/projects/2016-8-0.jpg) 



Kontroler anteny magnetycznej
-----------------------------





 Praktyka pokazuje, że antena magnetyczna nie musi być „kłopotliwa” w użyciu, ale

przeciwnie, znakomicie nadaje się na skuteczną antenę przenośną a nawet stosowana może

być stacjonarnie w mieszkaniu w warunkach kiedy założnie innej anteny nie jest możliwe.




##### Parametry funkcjonalne




* Pasywny pomiar dopasowania anteny za pomocą reflektometru SWR
* Wskaźnik położenia (rozwarcia) kondensatora strojeniowego anteny
* Pamięć 9 położeń kondensatora strojeniowego
* Automatyczne dostrojenie anteny do aktualnej częstotliwości pracy
* Możliwość sterowania za pomocą kabla o 8, o 3 oraz o dwóch przewodach (wspólny kabel

 coax zasilający antenę w sygnał RF)
* Zasilanie z sieci 230V oraz akumulatora (napięcie co najmniej 14.4V)




##### Koncepcja rozwiązania




W zależności od wybranego modelu sterowania anteną (za pomocą kabla o 8 przewodów, za pomocą kabla o 3 przewodach lub za pomocą jednego kabla koncentrycznego), obowiązuje odpowiedni system połączeń sterownika z anteną. Zawsze musi istnieć połączenie sygnału w.cz. (RF) nadajnika z anteną za pomocą kabla koncentrycznego, ale w zależności od wybranego modelu sterowania konieczny będzie dodatkowy wzmacniacz sygnału przy antenie.

Ze względu na odporność na silne pole elektromagnetyczne, jako czujnik położenia kondensatora strojącego zastosowany jest zestaw hermetycznego kondensatora oraz magnesu neodymowego 10/4/3 mm.

Główny moduł sterujący posiada cześć pomiarową (miernik poziomu SWR), który wykorzystany jest zarówno przy strojeniu ręcznym jak i automatycznym, dla osiągnięcia dopasowania na częstotliwości pracy.




##### Tryby pracy




* Tryb 1 – pełny kabel sterujący 8(7) przewodów  


 W tym trybie, obok kabla koncentrycznego, łączącego nadajnik z anteną, do strojenia anteny stosowany jest dodatkowy kabel o 7(8)-przewodowy, doprowadzający sterowanie do silnika oraz dla sprawdzania stanu czujnika kontaktronowego.
* Tryb 2 - kabel sterujący o 3 przewodach, z których jeden to masa, drugi zasilanie a trzeci doprowadza sygnał sterujący.  
 Ten tryb wymaga dodatkowego wzmacniacza sygnału przy antenie. Sterowanie odbywa się za pomocą modulacji o częstotliwości ok. 5-6 kHz z rozdzielczością 50 Hz, co umożliwia wydawane do kilkudziesięciu poleceń sterujących.
* Tryb 3 - kabel koncentryczny wykorzystany jest podwójnie, zarówno do transmisji sygnału w.cz. jak i do sterowania wzmacniacza przy antenie.  
 Separację sygnałów zapewniają proste filtry LC. Dodatkowo, sygnał sterujący - po wyprostowaniu - wykorzystywany jest we wzmacniaczu do zasilania wzmacniacza przy antenie.






 Urzadzenie zostało podzielone na bloki funkcjonalne: główną jednostkę

 sterującą, moduł pomiarowy SWR, który jest z nią związany i wzmacniacz antenowy.

Schematy modułów pokazane są na rysunkach 4, 5 i 6.






 Szczegółowy opis modułów opisano w załączonej dokumentacji (plik pdf). W dokumentacji opisano także zastosowany interface połączenia kablowego (8 i 3 przewody), a
{% include swiatradio.html on_page="06/2017 str. 47-51" %}
 także pokazano budowę sprzęgła pomiędzy silnikiem krokowym a kondensatorem

 strojeniowym, jak również wszelkie szczegóły realizacji i plany rozwojowe urządzenia.





#### Do pobrania

[Dokumentacja projektu - opis konkursowy (plik pdf)](/assets/bin/SP6FRE_Kontroler-anteny-magnetycznej.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 06/2017 str. 47-51

 





 


