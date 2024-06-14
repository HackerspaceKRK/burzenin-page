---
title: Rozszerzenie zakresu pracy wobulatora NWT7 do 200 MHz.
puk_category: C
puk_year: 2012
puk_place: 10
author: sq4avs
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq4avs_rozszerzenie_zakresu_pracy_wobulatora_nwt7_do_200_mhz.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq4avs_rozszerzenie_zakresu_pracy_wobulatora_nwt7_do_200_mhz.jpg
---





 



![](assets/data/img/projects/2012-10-0.jpg) 



Rozszerzenie zakresu pracy analizatora NWT7 do 200 MHz
------------------------------------------------------





 Jednym z najbardziej przydatnych przyrządów w pracowni każdego radioamatora jest wobuloskop,

 a jedną z najchętniej wykonywanych konstrukcji tego typu jest układ NWT7. Główną wadą NWT7

 jest niska maksymalna częstotliwość pracy, wynosząca około 50 MHz. Zakres ten można jednak

 bardzo niskim kosztem rozszerzyć nawet do 200 MHz.




##### Opis działania układu




Sercem opisanego urządzenia jest układ powielacza częstotliwości ICS502. Układ ten wykorzystuje do powielania częstotliwości pętlę fazową.

 Koszt układu jest niższy niż 2 zł za sztukę. ICS502 był stosowany jako mnożnik (powielacz) częstotliwości w starszych płytach głównych

 komputerów. Może on powielać częstotliwość wejściową 2; 2,5; 3; 3,33; 4 i 5-krotnie, zależnie od wybranej konfiguracji stanów logicznych

 na wyprowadzeniach 6 i 7 (sygnały S0 i S1). Na wyjściu CLK (wyprowadzenie 5) dostajemy sygnał o poziomach logicznych CMOS i odpowiednio

 powielonej częstotliwości wejściowej. Sygnał z analizatora NWT7 jest za mały aby wysterować układ ICS502, dlatego jest wzmacniany we

 wzmacniaczu, wykonanym na tranzystorze BFR92, do poziomu zapewniającego prawidłowe wysterowanie powielacza.






 Układ ICS502 dostarcza na wyjściu CLK przebieg prostokątny o wypełnieniu bardzo zbliżonym do 50%, dlatego w widmie tego sygnału,

 oprócz częstotliwości podstawowej, występują praktycznie tylko nieparzyste jej wielokrotności. Częstotliwości będące nieparzystymi

 wielokrotnościami częstotliwości podstawowej łatwo usuwa się filtrami dolnoprzepustowymi o częstotliwościach odcięcia odpowiednio

 90 i 160MHz. Przełącznikiem P1 wybiera się krotność powielania częstotliwości przez układ ICS502 (2 lub 4 razy) oraz odpowiedni

 filtr dolnoprzepustowy. W układzie filtru zastosowano cewki SMD o rozmiarze 1008. Dopasowanie impedancyjne do wejścia filtru

 dolnoprzepustowego i ograniczenie poziomu sygnału wejściowego dla wzmacniacza MMIC typu MSA1105 zapewnia układ dzielnika

 rezystorowego R6, R7.

 




 Wzmacniacz MMIC izoluje w pewnym stopniu filtry od badanego układu, izolację tę poprawiają również tłumiki 3dB znajdujące się

 na wejściu i wyjściu wzmacniacza. Zaletą zastosowanego wzmacniacza jest jego duża liniowość i stosunkowo niski koszt.




##### Montaż




 Układ należy zmontować na dwustronnym laminacie szklano-epoksydowym o grubości 0,8 mm i zamknąć w obudowie ekranującej.

 Poprawnie zmontowany układ nie wymaga uruchamiania. Zakres częstotliwości pracy układu można rozszerzyć do 200 MHz

 stosując w miejsce układu ICS502 układ 3NB3020 o innej konfiguracji wyprowadzeń, wymaga to oczywiście przeprojektowania płytki.

 W tym wypadku filtry należy przeliczyć odpowiednio na 110 i 200 MHz. Częstotliwości filtrów dolnoprzepustowych

 tłumią też parzyste wielokrotności częstotliwości wyjściowej, poprawiając widmo wyjściowe sygnału powielacza.

 


##### Konfiguracja NWT




 Aby układ prawidłowo wyświetlał częstotliwość mierzoną, podczas pracy z powielaczem częstotliwości należy

 odpowiednio skonfigurować program WinNWT. W opcji "Ustawienia/Konfiguracja", w oknie "Limit częstotliwości" należy

 wybrać "Mnożnik częstotliwości" (w zależności od pozycji przełącznika: 2 lub 4) oraz maksymalną częstotliwość pracy urządzenia.

 Ustawienie tej opcji spowoduje automatyczne przeliczenie częstotliwości mierzonej. Układ umożliwia wybranie stopnia powielenia

 od 1 do 10 z krokiem co 1 oraz 16, 32 i 64, co umożliwia rozszerzenie zakresu pomiarowego do zakresu pojedynczych GHz -

 po zmianie układu pętli fazowej i detektora na np. AD8313.






 Układ w swej podstawowej konfiguracji umożliwia pomiar charakterystyk amplitudowo-częstotliwościowych aż do 480MHz

 z wykorzystaniem nieparzystych harmonicznych układu ICS502. Tłumienie filtru w paśmie przepustowym (tzw. tłumienie wtrącenia)

{% include swiatradio.html on_page="03/2013 str. 48-49" %}ślić przez porównanie badanego filtru z filtrem wzorcowym.

 W tym wypadku należy ustawić krotność powielania w oprogramowaniu "razy 6" a sam wynik pomiaru pomnożyć 2 razy,

 krotność powielania sygnału przez układ ICS502 wynosi w tym wypadku 4 (niestety, oprogramowanie NWT nie umożliwia

 ustawienia stopnia powielenia "razy 12" co umożliwiłoby bezpośredni odczyt częstotliwości mierzonej na ekranie komputera).

 Oczywiście w tym wypadku filtry dolnoprzepustowe układu ICS502 zostają pominięte, zaś sygnał odbiera się na wyprowadzeniu 2.

 




 Przy pomiarach z wykorzystaniem harmonicznych, amplituda sygnału na wyprowadzeniu 2 jest większa, niż na wyjściu współpracującym

 z filtrami dolnoprzepustowymi, ale jest całkowicie bezpieczna dla wykorzystywanego analizatora.

 Strojenie z wykorzystaniem harmonicznych wymaga od użytkownika uwagi, aby nie zestroić układu na innej częstotliwości,

 jednak przy odrobinie wprawy nie stanowi to żadnego problemu, gdyż odpowiednie harmoniczne są mocno odległe od siebie. P

 onieważ pasmo zastosowanej pętli fazowej układu ICS502 wynosi około 10 kHz, należy w oknie Ustawienia NWT (główne okno pomiarowe)

 ustawić wartość Przerwy na 1000 us. Parametr ten określa, co jaki czas będzie wykonywany pomiar.

 To opóźnienie jest konieczne dla ustabilizowania pętli PLL na nowej częstotliwości mierzonej, po zmianie częstotliwości DDS-a.

 


##### Inne zastosowania




Układ powielacza częstotliwości przy ustawionym współczynniku „x4” umożliwia wykorzystanie tanich układów scalonych syntezerów

DDS AD9850, AD9851 w układach fazowo-homodynowych, wymagających częstotliwości VFO czterokrotnie wyższej od częstotliwości odbieranej.

Dodatkową zaletą układu w takiej aplikacji jest usunięcie z widma sygnału DDS szeregu sygnałów pasożytniczych (ang. *spurs*).






 Na zakończenie chciałbym podziękować Waldkowi **3Z6AEF** za wszelkie uwagi oraz Krzysztofowi **SQ8Z** za wspólne eksperymenty.







![](assets/img/logo/sr_logo_s.jpg)###### 03/2013 str. 48-49

 





 


