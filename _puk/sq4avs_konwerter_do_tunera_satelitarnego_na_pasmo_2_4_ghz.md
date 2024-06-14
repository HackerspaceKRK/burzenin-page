---
title: Konwerter do tunera satelitarnego na pasmo 2,4 GHz
puk_category: A
puk_year: 2017
puk_place: 2
author: sq4avs
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq4avs_konwerter_do_tunera_satelitarnego_na_pasmo_2_4_ghz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq4avs_konwerter_do_tunera_satelitarnego_na_pasmo_2_4_ghz.jpg
---





 



![](assets/data/img/projects/2017-2-0.jpg) 



Konwerter TV-SAT do odbioru ATV w paśmie 13cm
---------------------------------------------





 Układ umożliwia odbiór sygnałów szybkiej telewizji amatorskiej po podłączeniu go do tunera satelitarnego.

 Najciekawszym zastosowaniem konwertera jest użycie go od obioru sygnałów międzynarodowej stacji kosmicznej nadawanych na częstotliwości 2395MHz.

 Konieczność zastosowania konwertera wynika z faktu, że częstotliwość pracy typowych tunerów satelitarnych wynosi 950-2150MHz.

 Układ powstał przez modyfikację układu opracowanego przez IK8UIF.




##### Parametry układu




 Układ zasilany napięciem 12V. Wzmocnienie układu wynosi 42dB, współczynnik szumów 1.6dB.




##### Opis układu




 Schemat elektryczny przedstawiono na rysunku 2.






 Składowe o niskich częstotliwościach redukowane są przez linię mikropaskową na wejściu wzmacniacza MGA działającą jak filtr górnoprzepustowy.

 Wejście wzmacniacza dopasowane jest na minimum szumów odcinkiem cewki wykonanej na laminacie. Sygnał z wyjścia układu MGA filtrowany jest

 w filtrze pasmowoprzepustowym a następnie wzmacniany przez układ INA10386. Funkcję mieszacza częstotliwości pełni układ IAM81008.

 Generator przemiany częstotliwości zrealizowany jest na tranzystorze BFR92. Stabilność częstotliwości generatora zapewnia rezonator

 dielektryczny o częstotliwości znamionowej 1150MHz. Faktyczna częstotliwość pracy generatora wynosi około 1GHz co wynika z wpływu

 pojemności podłączonych do rezonatora ceramicznego.

 




 Rezonator ceramiczny zapewnia wystarczającą stabilność częstotliwości do odbioru sygnałów ATV.

 Lepszą stabilność częstotliwości można uzyskać zastępując rezonator koncentryczny tanim i łatwo dostępnym rezonatorem SAW o częstotliwości 915MHz

 bez zmiany reszty elementów układu. Sygnał wyjściowy jest różnicą częstotliwości sygnału wejściowego i generatora. Współczynnik szumów układu może

 był łatwo zmniejszony przez zastosowanie układu scalonego o mniejszym współczynniku szumów. Drugą możliwością obniżenia współczynnika szumów jest

 zastosowanie tranzystora niskoszumnego w miejsce układu MMIC po niewielkiej modyfikacji wzmacniacze wejściowego.




##### Montaż i uruchomienie
{% include swiatradio.html on_page="03/2018 str. 48-49" %}



 Układ zmontowany ze sprawnych elementów nie wymaga uruchamiania. Poprawność działania można zweryfikować mierząc napięcia stałe

 w charakterystycznych punktach układu. W przypadku stosowania układu MGA85653 bardzo ważne jest, aby czwarta nóżka układu

 scalonego była odgięta do góry i nie była podłączona elektrycznie z układem. Płytka musi być wykonana na laminacie typu FR4 o grubości 0,8mm.

 Przelotki do masy wykonano następująco jako niskoimpedanycjne: wywiercono otwór o średnicy 3mm, od strony masy zalutowana otwór kawałkiem folii

 miedzianej, otwór wypełniono cyną oraz jako przelotki „typowe” srebrzanką o grubości 0,8mm. Dodatkowo masy na obu warstwach płytki drukowanej

 zostały połączone odcinkiem folii miedzianej.





#### Do pobrania

[Projekt PCB w Sprint Layout (plik .LAY)](assets/data/download/SQ4AVS_Konwerter-ATV.lay6)




![](assets/img/logo/sr_logo_s.jpg)###### 03/2018 str. 48-49

 





 


