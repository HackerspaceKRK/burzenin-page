---
title: Tester elementów elektronicznych
puk_category: C
puk_year: 2013
puk_place: 16
author: sq7ovv
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq7ovv_tester_elementów_elektronicznych.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7ovv_tester_elementów_elektronicznych.jpg
---





 



![](assets/data/img/projects/2013-16-0.jpg) 



Tester elementów elektronicznych
--------------------------------





 Popularny tester elementów opracowany przez Karla Kübblera. Umożliwia pomiar elementów półprzewodnikowych (tranzystory, diody) i pasywnych (rezystory, kondensatory).

 Niezbędny do określenia przydatności elementu, przydatny np. do szybkiego określenia wyprowadzeń tranzystora.

 


##### Funkcjonalność testera




 Urządzenie powstało jako tester tranzystorów i szybko zostało rozbudowane o kolejne funkcjonalności. Dziś

 potrafi sprawdzać tranzystory bipolarne, unipolarne, diody, rezystory, cewki, kondensatory, tyrystory oraz

 diody zenera.






 Tester posiada dwa zespoły kontaktów pomiarowych. Jeden 3-stykowy i drugi 2-stykowy. Zespół 2-stykowy

 służy do pomiaru diod zenera. Pozostałe pomiary obsługuje zespół 3-stykowy.






 Pomiar diod zenera jest prosty. Wystarczy do styków zespołu 2-stykowego wpiąć badaną diodę i włączyć

 pomiar przez przytrzymanie klawisza. W czasie trzymania klawisza pracuje przetwornica podająca napięcie

 pomiarowe na gniazdo i badane jest napięcie zenera danej diody. Pomiaru napięcia dokonuje procesor

 Atmega328P, który jest sercem systemu testera. Przetwornica zasila gniazdo pomiarowe napięciem bliskim

 50V i jest to ograniczenie zakresu pomiaru diod zenera. Wynik pomiaru ukazuje się na wyświetlaczu przez

 kolejne kilka sekund i tester się wyłącza. Pomiary diod zenera możemy dokonywać wyłącznie przy zasilaniu

 urządzenia z zewnętrznego zasilacza ze względu na spory pobór prądu przez przetwornicę.






 Pozostałe pomiary są dokonywane w zespole styków pomiarowych 3-stykowym. Wystarczy dowolny element

 badany podłączyć pod zespół styków w dowolnej konfiguracji a tester sam rozpozna rodzaj elementu

 mierzonego, jego konfigurację oraz poda parametry. Dla tranzystora bipolarnego to będzie współczynnik

 wzmocnienia, napięcie złącza baza-emiter oraz poda rozpoznanie typu (NPN czy PNP) i rozkład nóżek (np

 123=EBC).






 Urządzenie mierzy kondensatory w zakresie pojemności 25pF do 100mF (pomiar tych ostatnich

 niestety trwa dość długo).Dla kondensatorów o pojemności powyżej 2uF urządzenie również mierzy ESR

 (ekwiwalentną rezystancję szeregową), co jest ważnym parametrem dla zastosowań w pracy impulsowej

 kondensatora.






 Pomiar indukcyjności odbywa się w zakresie od 10uH do ponad 20H. Zakres pomiaru

 rezystancji to począwszy od 0,1Ω do 50MΩ.






 Zwykłe diody są rozpoznawane i tester pokazuje kierunek włączenia i pod które styki gniazda pomiarowego

 została dioda podpięta oraz jakie jest jej napięcie przewodzenia.




##### Budowa testera




 Urządzenie jest na tyle proste w montażu, że nadaje się znakomicie dla początkujących

konstruktorów. Grube ścieżki oraz duże pady lutownicze ułatwiają pracę i zmniejszają ryzyko

odparzeń druku przy lutowaniu.






 Montaż należy rozpocząć od dokładnego zapoznania się z płytką i rozmieszczeniem elementów.

Przyjmijmy, że góra płytki, to krawędź, na której jest miejsce do wlutowania szyny do podłączenia

wyświetlacza. Wtedy procesor jest poziomo i jego 1-sza noga jest z prawej strony u góry, a

przetwornica jest pionowo z pierwszą nogą na dole. Gniazdo zasilacza zewnętrznego jest w

prawym górnym rogu płytki.






 Kolejność montażu:


{% include swiatradio.html on_page="02/2014 str. 49-51" %}
* Zapoznać się z płytką
* Zainstalować 8 krosów widocznych na stronie opisowej płytki
* Wlutować wszystkie oporniki
* Wlutować podstawki pod układy scalone
* Wlutować potencjometr montażowy
* Wlutować stabilizatory napięć
* Wlutować diody prostownicze separujące zasilania poszczególnych bloków
* Wlutować goldpiny do podłączenia wyświetlacza
* Wlutować kwarc oraz kondensatory
* Wlutować tranzystory oraz cewkę przetwornicy
* Wlutować gniazda pomiarowe lub goldpiny do ich podłączenia
* Wlutować przycisk oraz diodę LED
* Pomierzyć napięcia zasilania układów scalonych (przy wciśniętym przycisku)
* Włożyć układ scalony przetwornicy
* Zmierzyć napięcie na gnieździe pomiaru diod zenera (również przy wciśniętym przycisku)
* Włożyć zaprogramowany procesor
* Wcisnąć przycisk. Powinna się zapalić dioda LED na okres około 10 sekund
* Podłączyć wyświetlacz
* Wcisnąć przycisk i wyregulować kontrast wyświetlacza potencjometrem montażowym









 Płytka testera została przystosowana do obudowy Z7A krajowego producenta. Obudowę trzeba

dostosować przez wycięcie z wnętrza słupków montażowych oraz należy wyciąć odpowiednie

otwory na wyświetlacz, gniazdo zasilania i przycisk oraz zamontować w płycie górnej styki

pomiarowe. Można w tym celu użyć podstawki precyzyjnej dla 10-nóżkowego scalaka. Przydaje

się też czasem płytka stykowa do pomiaru elementów SMD.



 
#### Do pobrania

[Instrukcja montażu testera - wersja 2.02 (plik pdf)](assets/data/download/SQ7OVV_Tester-instrukcja-montazu-v.2.02.pdf)

[Instrukcja obsługi testera (plik pdf)](assets/data/download/SQ7OVV_TESTER-Manual.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 02/2014 str. 49-51

 





 


