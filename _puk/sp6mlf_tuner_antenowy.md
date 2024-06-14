---
title: Tuner antenowy
puk_category: B
puk_year: 2012
puk_place: 7
author: sp6mlf
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6mlf_tuner_antenowy.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6mlf_tuner_antenowy.jpg
---





 



![](assets/data/img/projects/2012-7-0.jpg) 



Półautomatyczny tuner antenowy wg UR5WHK
----------------------------------------





 Prosty półautomatyczny tuner antenowy, opracowany przez Vasyla Pavluka UR5WHK. Tanie rozwiązanie,

 dedykowane szczególnie konstruktorom-programistom, ponieważ dostępny jest kod źródłowy (assembler)

 oprogramowania mikroprocesora.  


 Poniżej dosłowny opis Jarka SP6MLF ze zgłoszenia konkursowego.






Zacznę od tego, że właściwie to nie lubię tunerów antenowych (a właściwie tunerów fiderowych)... Ale moje tranzystorowe PA je lubi!




##### Spsób działania i użytkowania




Na czym polega „półautomatyka” tego układu? Wybieramy enkoderem z menu jakąś komórkę pamięci, wybieramy jedną z dwóch anten,

manualnie z menu ustawiamy najlepszą kombinację cewek i kondensatorów oraz ustawienie pojemności od strony TX’a lub anteny,

wychodzimy z komórki pamięci i w tym momencie mamy zapisane ustawienia dla danej anteny w konkretnym paśmie i możemy rozpocząć

nową sekwencję strojenia dla innej komórki w innym paśmie lub z inną anteną. Po powrocie do poprzednio zapisanej pamięci skrzynka

jest gotowa do pracy w określonym paśmie. Ustawianie wszystkich pasm dla nowej anteny jest dość żmudne, ale później mamy

komfort pracy porównywalny do automatycznego tunera, zmiana pasma trwa kilka sekund.






Jeżeli pozostawimy skrzynkę wyłączoną to sygnał

przechodzi bezpośrednio (bypass) od wejścia do anteny 1, taką samą sytuację mamy przy włączonej skrzynce po ustawieniu C=0 i L=0, ale możemy wtedy zmienić anteny.




##### Opis urządzenia i uwagi konstrukcyjne




 Przy omawianiu użytych podzespołów i uruchamianiu tunera będę posługiwał się schematem zamieszczonym w miesięczniku Świat Radio nr 11/2010 (rysunek 2).






 Transformator Tr mostka pomiarowego SWR, w oryginale przewidziany jest rdzeń dwuotworowy ale nie uzyskałem z nim dobrych wyników...

 Zastosowałem więc dwa pierścionki z symetryzatorów anten telewizyjnych (bo miałem w szufladzie) około 10-15 zwojów. Diody D1-D4: GD507 (niekrytyczne),

 kondensatory 10H to 10nF.






 Na schemacie jest wzmacniacz operacyjny LM324, będzie on pracował ale wskazania będą o połowę za niskie. Należy

 zastosować wzmacniacz rail-to-rail, ja użyłem MCP604 (dostępny w TME). Zmiana taka wymusza korektę płytki PCB - zamienić należy masę i zasilanie wzmacniacza.






 Rezystory R7-R8 i R9-R10 zmieniamy na wartość 22k.






 Największą trudność sprawiło mi dobranie odpowiedniego enkodera. Dwa posiadane Alpsy nie działały prawidłowo,

 ale znakomicie funkcjonują w tym miejscu trzy zwykłe zwierne przyciski. Ostatecznie znalazłem impulsator o 24 skokach, z przyciskiem, który przy powolnym kręceniu

 przełącza w dwie strony z dostateczną dokładnością. W obwodach zasilania układów scalonych oraz sterowania przekaźników należy dodać (nie wszędzie są) kondensatory

 blokujące 100n, bez nich układ czasem wariuje przy podaniu 100W z nadajnika.






 Mankamentem którego nie udało się całkowicie usunąć są zakłócenia (prążki)

 wnoszone na jednym z pasm przez wyświetlacz LCD 2x24. Nie pomogło ekranowanie, blokowanie zasilania itp...






 Przy zmianie LCD na mniejszy 2x16 zakłócenia znikają!.

 Jestem przekonany, że prążki znikną przy zastosowaniu LCD innego typu.






 Pojemności C1-C7 w układzie dostrajania mają wartości: 20pF, 40pF, 80pF, 160pF, 320pF, 680pF, 1360pF.

 Wymagane pojemności zostały *poskładane* z niebieskich kondensatorów ceramicznych 1kV (stosowanych w przyeteornicach wysokonapieciowych).

 Wlutowany kiedyś kondensator na 500V *poleciał in luft*... Z pewnością lepiej byłoby

 zastosować w tym miejscu kondensatory mikowe (uwaga! rosyjskie „czekoladki” nie nadają się!), ale jest to prosty, tani układ i takie elementy, jakie zastosowano, zupełnie wystarczają.






 Zainteresowanych zapraszam na stronę SP-HM.pl i CQHAM.ru gdzie znajdują się wątki poświęcone temu urządzeniu.






 W domu na co dzień używam tej skrzynki do strojenia anteny W3DZZ przy pracy na pasmach powyżej 7 MHz, pracy CW w paśmie 80 metrów, czasami nawet dostrajam 20-metrowy

 LongWire do pasma 160m (tak! ;-). Mam jeszcze dwie inne skrzynki manualne, ale najczęściej korzystam właśnie z tunera UR5WHK.







#### Odnośniki

[Opis ATU UR5WHK w "Świat Radio" 11/2010 str. 66-67 (plik PDF)](http://www.swiatradio.com.pl/virtual/modules.php?name=Downloads&d_op=getit&lid=30)

[Wątek o ATU UR5WHK na forum cqham.ru](http://www.cqham.ru/forum/showthread.php?4346-%C0%ED%F2%E5%ED%ED%FB%E9-%F2%FE%ED%E5%F0-WHK_AT1-%ED%E0-%C2%E0%F8-%F1%F3%E4)

[Wątek o ATU UR5WHK na forum SP Home Made](http://sp-hm.pl/thread-295.html)

 



{% include swiatradio.html on_page="03/2013 str.51-53" %}

 





 


