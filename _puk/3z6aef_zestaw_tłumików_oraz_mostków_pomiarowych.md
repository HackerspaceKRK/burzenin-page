---
title: Zestaw tłumików oraz mostków pomiarowych
puk_category: C
puk_year: 2010
puk_place: 3
author: 3z6aef
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/3z6aef_zestaw_tłumików_oraz_mostków_pomiarowych.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/3z6aef_zestaw_tłumików_oraz_mostków_pomiarowych.jpg
---





 



![](assets/data/img/projects/2010-3-0.jpg) 



Zestaw tłumików oraz mostków pomiarowych
----------------------------------------





 Pomocnicze urządzenia i przyrządy pomiarowe stanowią nieodzowne uzupełnienie domowego laboratorium

 i są wręcz niezbędne przy niektórych pomiarach. Oczywiście, przyrządy pomocnicze są produkowane przez różne firmy,

 ale w praktycznej działalności radioamatora są one zazwyczaj wykonywane samodzielnie.




##### Zakres projektu



Wykonano kilka wybranych pomocniczych przyrządów, które powinny być łatwe do zbudowania i są obowiązkowym wyposażeniem domowego laboratorium:



* Regulowany tłumik pomiarowy
* Kalibrator poziomu mocy
* Sprzęgacz kierunkowy
* Tłumik do pomiarów mocy




##### Regulowany tłumik pomiarowy




Stopnie tłumika wykonano w jako 8 niezależnie włączanych stopni w konfiguracji PI o następujących wartościach tłumienia: 1, 2, 2, 6, 10, 20, 20, 20 [dB].

Umożliwia to ustawienie dowolnej wartości tłumienia w zakresie do 81 dB z krokiem 1 dB. Zakres pomiarowy jest wystarczający do większości pomiarów,

jedynie w niektórych przypadkach trzeba się posiłkować dodatkowymi stopniami tłumienia. Dokładność przyrządu, wynikająca z zastosowania dobrej

jakości rezystorów MMELF 1% jest również zadowalająca, natomiast zmierzony SWR dla wejścia tłumika nie przekracza wartości 1:1,03

w całym zakładanym zakresie częstotliwości pracy od 0 do 30 MHz.






Jako przełączniki zastosowano typowe „dalekowschodnie” przełączniki DPDT. Zmierzone pojemności międzystykowe wynoszą dla tego przełącznika 0,2 .. 0,3 pF.

Obudowa tłumika jest podwójna: wewnętrzną wykonano z kawałków laminatu FR-4 o grubosci 1,5 mm, zaś przegrody między sekcjami z blachy stalowej

ocynowanej o grubości 0,2 mm. Zewnętrzna obudowa wykonana jest z kształtownika aluminiowego (25x45 mm, profil C) o długości 150 mm.

Boki oraz pokrywkę obudowy wykonano z blachy aluminiowej o grubości 2 mm. Do połączenia boków z profilem C użyto domowej metody „spawania”

palnikiem gazowym z użyciem stopu AluWeld.




##### Kalibrator poziomu mocy




Kalibrator poziomu mocy jest prostym generatorem, na którego wyjściu jest sygnał przemienny (przebieg prostokątny) o ściśle określonym poziomie napięcia.

Zakładając standardowe obciążenie 50 omów, można w ten sposób kalibrować poziom mocy – z precyzją wystarczającą do amatorskich pomiarów.

Kalibrator zaprojektował Bob Kopski K3NHI, a opis układu ukazał się w dwumiesięczniku QEX (Jan/Feb 2004).






Kalibrator został skonstruowany na bazie typowego generatora CMOS 10 MHz, stosowanego w sprzęcie komputerowym. Uzupełniony o stabilizator

napięcia zasilania (z baterii 9V) oraz tłumik 20 dB na wyjściu, dostarcza określonego poziomu przebieg prostokątny, którego poziom można

bardzo łatwo skalibrować precyzyjnym miernikiem napięcia stałego, np. SANWA PC5000.




##### Mostek pomiarowy w.cz.




Wykonano dwa mostki pomiarowe: pierwszy jako przystawkę do analizatora NWT-500, a drugi jako przystawkę do analizatora VNA-N2PK (zob. fotografia tytułowa).






Pierwszy mostek zbudowano z rezystorów metalizowanych 50 omów, 0,6W 1%. Transformator został nawinięty bifilarnie,

9 zwojów drutem DNE 0,3 mm na rdzeniu złożonym z dwóch rdzeni Amidon T37-43, przy których osiagnięto najlepszą kierunkowość mostka

(wypróbowano również rdzenie T37-77 oraz T50-61 osiągając gorsze rezultaty). Montaż wykonano techniką przestrzenną bezpośrednio na złączach BNC.

Obudowa jest zrobiona z kształtowników aluminiowych (profile C: 25x45 mm oraz 25x117 mm) odpowiednio dociętych.

Zewnętrzne wymiary obudowy wynoszą: 117x45x25 mm. Rozmieszczenie gniazd RF-in oraz DET jest tak dobrane, aby można było podłączyć mostek

do analizatora NWT-500 za pomocą krótkich adaptorów BNC (male-male).




Zmierzona kierunkowość mostka: 35 dB przy 1,8 MHz, 38 dB przy 3,5 dB i nie mniej niż 40 dB dla częstotliwości 7..30 MHz.




 Drugi mostek wykonano na płytce PCB zaprojektowanej przez Ivana VE3IVM. Jako transformator wykorzystano gotowy tranformator T1-6T (Mini Circuits),

 zaś 50 omowe oporniki to 1% elementy SMD. Całość zabudowana jest w obudowie typu 1590A firmy HAMMOND i wyposażona w złącza typu SMA (female).

 Aby móc wykorzystywać mostek również z kablami zakończonymi wtykami BNC, mostek jest wyposażony w adaptory (przejściówki) SMA-BNC.


Zmierzona kierunkowość mostka: co najmniej 43 dB w zakresie od 0,1 do 25 MHz i co najmniej 46 dB w zakresie od 25 do 50 MHz.


##### Tłumik do pomiarów mocy




Górne ograniczenie zakresu sond wejściowych popularnych NWT-7/NWT-500 wynosi +10dBm, zaś miernik mocy OZ2CPU ma maksymalny zakres do 1W.

Do pomiarów większych mocy z użyciem mierników o ograniczonym zakresie pomiarowym, konieczne jest użycie tłumików.






Tłumik wykonano na podstawie opisu z miesięcznika ARRL QST, nr 01/2001 w artykule W.Haywarda W7ZOI i B.Larkina W7PUA.

Przyrząd obniża moc doprowadzaną do sondy wejściowej miernika mocy o 40 dB, zatem rozszerza zakres NWT-7/NWT-500 do 100W,

co jest już zupełnie wystarczające w większości przypadków.






Tłumik wykonano z rezystorów metalizowanych 0,6W 1%. Zastosowano 3\*820 omów oraz 50,1 omów. Jako obudowę wykorzystano fabryczne

pudełko typu 1590A firmy HAMMOND (wymiary zewnętrzne ok. 90x30x35 mm). Zastosowano gniazda typu BNC, połączone linią paskową,

która została zrobiona z kawałka (15x20 mm) dwustronnego laminatu FR-4 o grubości 0,8 mm. Obie strony laminatu połączone są na

krawędziach paskami blachy ocynowanej o grubości 0,2 mm.





#### Do pobrania

[Ham Lab Set - opis konkursowy (plik pdf)](assets/data/download/3Z6AEF_HamLabSet.pdf)

[12/2010 str. 55-57](http://www.swiatradio.com.pl/virtual/modules.php?name=Downloads&d_op=getit&lid=31)

{% include swiatradio.html on_page="12/2010 str. 55-57" %}




 


