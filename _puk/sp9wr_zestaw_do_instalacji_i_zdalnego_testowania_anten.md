---
title: Zestaw do instalacji i zdalnego testowania anten
puk_category: B
puk_year: 2014
puk_place: 6
author: sp9wr
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp9wr_zestaw_do_instalacji_i_zdalnego_testowania_anten.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp9wr_zestaw_do_instalacji_i_zdalnego_testowania_anten.jpg
---





 



![](assets/data/img/projects/2014-6-0.jpg) 



Zestaw do instalacji i zdalnego testowania anten
------------------------------------------------





 Na przedmiotowy zestaw składają się dwa rozwiązania:

 

* Uniwersalny trójnóg dla masztu antenowego
* Prosty układ do zdalnego bezprzewodowego pomiaru porównawczego natężenia pola emitowanego przez dwie anteny





 Rozwiązania te, przydatne w technice KF jak i UKF mogą być stosowane indywidualnie, jednakże ich zestawienie pozwala na szczególnie efektywną realizację zamierzonego celu t.j. testowania skuteczności i kierunkowości anten zwłaszcza w terenie, najlepiej otwartym, który jest najlepszym miejscem w aspekcie wiarygodności testów i pomiarów.




##### Uniwersalny trójnóg dla masztu antenowego




 Zasadniczym założeniem konstrukcyjnym trójnogu pod maszt antenowy była możliwość przewiezienia

 go w bagażniku samochodu, szybkiego zamontowania masztu przez jedną osobę a następnie wykorzystywania

 bez konieczności stosowania odciągów.

 




 Konstrukcja trójnogu jest wykonana z elementów żelaznych – posiada więc odpowiednią wagę, co

 razem z stosunkowo dużą rozpiętością trzech nóg podstawy (3x1m) oraz możliwością utwierdzenia

 w terenie końcówek tych nóg np. „śledziami” namiotowymi zapewnia odpowiednią stabilnośc i niewrażliwośc

 na podmuchy wiatru.

 




 Nogi są wkładane i mocowane śrubami do „trój rozdzielacza” do którego górnej części przyspawana jest gruba płyta blaszana

 z wyfrezowanym półokrągłym rowkiem. Dzięki temu gruby pręt żelazny na który bezpośrednio zakłada się pierwszą

 rurkę-segment masztu jest mocowany z możliwością ustawienia masztu w zakresie kątów od zera (pion) do ok.30 stopni od pionu.

 Ułatwia to instalację w terenie pochyłym lub na pochyłym dachu. W tym drugim przypadku na końcówki nóg poleca się

 nałożyc miękkie rurki gumowe zapobiegające przed uszkodzeniem pokrycia dachowego.

 




 Pręt nośny posiada górną częśc stoczoną gładko celem nałożenia pierwszego segmentu masztu w postaci rury fi zewn. 32mm

 z możliwością obrotu segmentu i tym samym łatwego, ręcznego obracanie masztu i anteny co jest istotne dla anten

 o charakterystyce kierunkowej, od prostego dipola poczynając.

 




 Wykorzystuję ten trójnóg do mocowania masztu o wys. 5 do 7m, złożonego z segmentów łatwych do przewiezienia w aucie,

 przy czym dolne segmenty są wykonane z rur żelaznych-patrz stabilnośc masztu.

 Z uwagi na transport autem waga odgrywa tu rolę drugorzędną.






##### Układ do zdalnego bezprzewodowego pomiaru porównawczego natężenia pola emitowanego z dwóch anten




Układ umożliwia zdalne (do 5km, opcjonalnie więcej), bezprzewodowe uaktywnienie nadawania z jednej lub dwu anten,

 a następne pomiar natężenia pola do oceny np. kierunkowości anteny lub różnicy skuteczności jednej anteny względem drugiej.

 Nie trzeba przekonywac jak cenna jest taka możliwośc dla krótkofalowców-eksperymentatorów antenowych,

 zwłaszcza jeśli może być prosta i tania w realizacji.






Zasadę funkcjonowania układu zilustrowano na rysunkach 2 i 3, które zawierają schemat blokowy oraz ideowy układu.






 Układ elektroniczny zlokalizowany jest w dwóch małych skrzyneczkach z których RCB („Remote Control Box”)-

 jest zasadniczą skrzynką zdalnego sterowania, połączoną z druga skrzynką A1/A2 S ( „A1/A2 Switch”),

 w której typowy przełącznik antenowy AS łączy poprzez styki przekaźnika P-ANT urządzenie nadawcze

 z jedną z anten A1 lub A2.






Uwaga: Skrzynka A1/A2 S może być eksploatowana na stałe przy TRX jako przełącznik dwóch anten,

zaś skrzynkę RCB dołącza się na czas testów i pomiarów.






 Tak skonfigurowany układ może funkcjonowac samodzielnie lub z dodatkiem w postaci popularnego zestawu dwóch

 radiotelefonów typu „walkie-talkie”. W tym drugim przypadku, który jest dogodniejszy i bardziej optymalny,

 algorytm funkcjonowania wygląda następująco:






W radiotelefonie TX przy którym znajduje się miernik M natężenia pola naciskamy przycisk tonu wywoławczego.

W radiotelefonie RX usytuowanym w pobliżu nadajnika (transceivera TRX) sygnał tonu z wyjścia słuchawkowego podawany

jest na detektor D w skrzynce RCB. Po przekształceniu na napięcie stałe sygnał poprzez człon czasowy T1 zapewniający

 czas trwania sygnału ok.6 sek. steruje przekaźnik P-TX , który w trybie cw uruchamia na ten czas nadajnik.

 Inne zestyki tego przekaźnika uruchamiają za pośrednictwem członu T2 opóźnienia czasowego ok.3 sekund

 przekaźnik P-ANT znajdujący się w skrzynce A1/A2 S co powoduje ,że podczas pierwszych trzech sekund sygnał

 nadawany jest z anteny A1 zaś w kolejnych trzech sekundach z anteny A2. W efekcie uzyskujemy łatwe, bezpośrednie

 porównywanie skuteczności obu anten w danym miejscu pomiaru.






 W razie braku radiotelefonów przełącznikiem S w skrzynce RCB wybieramy opcję z sterowaniem z multiwibratora MU,

 co zapewnia samoczynne, okresowe, np. co 15 sekund aktywowanie nadajnika na czas 6 sekund za pośrednictwem

 przekaźnika P-TX a dalej działanie układu jest identyczne do wyżej opisanego.






 Wyżej wymienione czasy można oczywiście ustawic według własnego uznania.






 Mając tak skonfigurowany układ bierzemy do ręki miernik natężenia pola (plus radiotelefon „walkie-talkie”)

 i obchodzimy lub wygodniej objeżdżamy autem w odpowiednim promieniu nasze drogie sercu anteny realizując testy i pomiary.

 Jako miernika natężenia można z powodzeniem wykorzystac, zwłaszcza dla celów porównawczych, odbiornika z

 S-metrem. Ja używam Tecsuna PL660.






 Układ elektroniczny według przytoczonego schematu blokowego może być zrealizowany na bazie elementów scalonych

 (rozwiązanie elegantsze) lub też z wykorzystaniem typowych tranzystorów NPN i PNP.

 Z uwagi na łatwiejsze dla ogółu krótkofalowców wykonawstwo jak i dostępnośc elementów przedstawiam

 schemat ideowy wg. drugiego wariantu.






 Jak widac na załączonym schemacie ideowym w skrzynce RCB do wzmacniacza na tranzystorach T3 i T4

 sterującego przekaźnik P-TX podłączany jest poprzez przełącznik S detektor sygnału wywoławczego z radiotelefonu

 "walkie-talkie” (dioda Schottky D2, kondensator C3 rezystor R7) lub multiwibrator na tranzystorach T1 i T2.






 Elementy R2/C1 , R3/C2, R7/C3 realizują stale czasowe odpowiednio: 6 s, 15 s, 6s.

 Człon czasowy umożliwiający z opóźnieniem 3 s wysterowanie przekaźnika P-ANT przełączającego anteny w skrzynce A1/A2 S

 zbudowany jest na tranzystorach T5 i T6 oraz elementach R9/C4 ustalających czas 3 s.






 Dioda Schottky D3 służy do szybkiego rozładowania kondensatora C4.






 W skrzynce A1/A2 S ustawiamy na czas testów/pomiarów przełącznik antenowy AS w pozycji A1,

 co umożliwia samoczynne przełączanie przekaźnikiem P-ANT po czasie 3 s anteny A1 na antenę A2.






 Uwaga: polecam przy okazji realizacji skrzynki A1A2 S dodatkowe proste i tanie rozwiązanie polegające na tym,

 że przełącznik antenowy AS posiada pozycję „O” (obie anteny wyłączone), co razem z opcjonalnym przekaźnikiem PB,

 którego styki wykonawcze automatycznie zwierają obie anteny do masy po wyłączeniu stacji (brak napięcia zasilającego +12V)

 chroni TRX na wypadek wyładowań atmosferycznych.

 Jak już nadmieniłem skrzynka A1/A2 S może i powinna być używana na stałe przy TRX.





##### Dane techniczne podstawowych elementów składowych układu




* TX, RX - typowe, popularne radiotelefony „walkie-talkie”
* T1,T2,T3,T4,T5 – tranzystory npn, np. BC547B
* T6 – tranzystor pnp, np. BC 557
* P-TX – mini przekaźnik na 12V
* P-ANT – przekaźnik 12V z srebrzonymi stykami, 5A (cena ok. 4 zł)
* Mini przełącznik 3-pozycjny (ok. 3 zł)
* Opcjonalny przekaźnik PB – parametry jak P-ANT














 


