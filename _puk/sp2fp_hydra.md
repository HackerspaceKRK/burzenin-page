---
title: HYDRA - TRX KF CW/SSB 3,5/7/14 MHz
author: sp2fp
tagline: Trzypasmowy TRX CW/SSB przygotowany w formie zestawu części do samodzielnego montażu.
classes: wide
header:
  overlay_image: /assets/images/puk/sp2fp_hydra.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp2fp_hydra.jpg
---

![alt](/assets/images/puk/sp2fp_hydra.jpg)
{: .full}

## Parametry urządzenia
- Pasma pracy 80/40/20
- Modulacja CW- SSB
- Czułość w zależności od pasma 0,8-0,3uV
- Moc nadajnika 20-50wat /12-19 v
- Moc Wzm m.cz. 1,5 wat
- Wbudowany KEYER na attiny85
- Obsługa manipulatora i klucza sztorcowego
- VFO – generator DDS ad9850
- Pojedyncza przemiana z częstotliwością pośrednią 10 MHz
- Filtry kwarcowe dla ssb i cw oraz filtr o regulowanej szerokości przed demodulatorem.
- ARW odbiornika w zakresie 110db
- Mieszacz odbiornika na układzie AD831 wysoka odporność na intermodulację OIP3+20dbm
- Wzmacniacz w.cz. pośredniej AD603 (45dB) reszta wzmocnienia po m.cz. na układzie ssm2166.
- Trzy obwodowe filtry pasmowe odbiornika przełączane przekaźnikami
- Aktywne filtry m.cz. drugiego rzędu w torze odbiorczym i nadawczym oraz filtr telegraficzny m.cz. 700hz
- Tor nadawczy: Kompresor dynamiki ssm2166, modulator i mieszacz na układach ne612
- Stopień mocy RD16 i MRF186
- ALC w torze nadawczym, pomiar mocy padanej i odbitej, zabezpieczenie przed wysokim SWR.
- Rozbudowana synteza częstotliwości realizująca wiele funkcji trxa :
- VFO , RIT , XIT, S-metr , wskaźnik mocy p/o, pomiar nap zasilania przy nadawaniu .
- Nadawanie CW odbywa sie bez przemiany częstotliwości. Synteza generuje częstotliwość nadawaną. Brak lustrzanek sygnału. Miękko narastające i opadające zbocza tonu.
- Funkcja „turbo enkoder” zmieniająca krok przestrajania zależna od szybkości kręcenia impulsatora. Płytka przystosowana dla kilku rodzajów enkoderów.
- Wyświetlacz alfanumeryczny LCD LED 2×16
- Gotowy moduł DDS z układem AD9850
- Wymiary zew. 190x190x70mm. Obudowa typ Z1W plus radiator z wentylatorem sterowany płynnie w zależności od temperatury.
- PCB fabryczne, płyta główna posiada wlutowane maszynowo elementy smd.
- Kit zawiera wszystkie elementy potrzebne do złożenia urządzenia.
- Mikrofon pojemnościowy z wtykiem 4 pin. (gruszka)
- Zasilanie napięciem stałym 11-19V. Prąd przy odbiorze 300mA i nadawaniu do 5 Amperów
- Więcej bieżących informacji na mojej stronie internetowej SP2FP
e-mail: sp2fp (at)wp.pl tel.: 602 376 440

## Opis działania TRX HYDRA
Trx powstał na podstawie doświadczeń zdobytych podczas projektowania trxów "Kaefelek" oraz "Scorpion".

Jest to dość zaawansowana amatorska konstrukcja. Posiada rozdzielony tor odbiorczy i nadawczy dla wysokich częstotliwości i wspólny tor malej częstotliwości oraz modulator/demodulator na jednym układzie. Wzmocnienie toru odbiorczego realizowane jest na małej i dużej częstotliwości z czego: 45dB przypada na p.cz. 10MHz, a 65dB na m.cz. Część nadawcza to dość klasyczny układ zawierający: modulator, filtr kwarcowy, mieszacz, tor wzmacniacza w.cz. i końcówkę mocy z filtrami dolnoprzepustowymi. Wspólnym modułem jest układ kompresora dynamiki ssm2166, który w odbiorniku pełni rolę wzmacniacza z arw dla małej częstotliwości, a w nadajniku działa jako kompresor oraz limiter dźwięku. Konieczność przełączania wielu sygnałów N/O/CW/SSB skłoniła mnie do zastosowania 12 kluczy elektronicznych typu 3157. Efektem takiego przełączania jest szybka i bezgłośna praca. Jedynym mechanicznym przekaźnikiem działającym podczas N/O jest przekaźnik antenowy. Dochodzą jeszcze przekaźniki dla przełączania filtrów LPF i BPF ale one stukają tylko podczas zmiany pasma.

## Tor odbiorczy
Sygnał z anteny doprowadzony jest na obwody dolnoprzepustowe, umieszczone na płytce końcówki mocy, kolejno poprzez przekaźnik trafia na obwody wejściowe odbiornika. Zostały one tak zaprojektowane aby dopasować impedancję anteny do oporności wejściowej mieszacza AD831. Dzięki takiemu rozwiązaniu napięcie wejściowe jest pasywnie ponoszone, uzyskując lepsze parametry szumowe. Dla każdego pasma zostało zaprojektowane inne wzmocnienie. Przy 20m wzmocnienie jest największe i daje wyższą czułość odbiornika, kosztem parametru ip3, dla 40m wzmocnienie jest niższe z lepszą dynamiką, a dla 80m różnica wynosi około 10dB w stosunku do 20m i mamy tutaj zaplanowane tłumienie sygnału z najwyższą dynamiką odbiornika. Nie ma tłumika ani wzmacniacza w.cz. Doskonały w swojej prostocie mieszacz aktywny AD831 pozwala uzyskać wysokie parametry przemiany, jak na amatorskie rozwiązanie. Po nim jest układ dopasowania oporności dla filtrów kwarcowych (T2) dzięki któremu zachowują one swoją charakterystykę. Zastosowane są dwa filtry oddzielne dla CW i SSB. Po filtrze mamy kolejne dopasowanie do wejścia wzmacniacza IC2 realizowane obwodem typu „L”. Wzmacniacz pośredniej AD603 jest niskoszumowym układem o wysokiej dynamice z regulacją wzmocnienia w zakresie 44 dB. Za jego regulację odpowiada sonda logarytmiczna AD8307. Liniowe układy detekcyjne nie spełniały swojej roli, ponieważ kość „Analoga” wymaga logarytmicznego sygnału sterującego względem wzmocnienia. W tej roli doskonale dopełnia się z układem detektora logarytmicznego AD8307. Dopasowanie odpowiedniego zakresu działania zostało dobrane eksperymentalnie i ograniczenie wzmocnienia zaczyna się od poziomu S7-S9 wzwyż. Po wzmocnieniu sygnał trafia na trzy polowy, o regulowanej szerokości filtr kwarcowy, znajdujący się przed demodulatorem. Regulacja szerokości filtru, dostępna jest ręcznie za pomocą potencjometru na front panelu, a jej zakres jest rożny dla emisji cw i ssb. Kolejno trafia on na demodulator ne602 i po demodulacji otrzymujemy dwa sygnały m.cz. w przeciwfazie. Sygnały m.cz. są odpowiednio odebrane przez układ ne5532 (U10) działający w układzie wzmacniacza prądowego o dużej oporności wejściowej. Poprzez układy przełączające doprowadzone zostają do kolejnego wzmacniacza operacyjnego znajdującego się w strukturze kompresora dynamiki SSM2166. Wzmacniacz ten pełni rolę sumatora i pomimo wzmocnienia napięciowego „1” poziom podnosi się o 6 dB dzięki zsumowaniu doprowadzonych sygnałów. Dalszy opis działania procesora dźwięku był by długi, dla dociekliwych polecam notę katalogową. Generalnie pełni on rolę wzmacniacza m.cz. z układem ARW, dającym wzmocnienie 60 dB, a podczas wysokiego poziomu wejściowego limiter zaczyna tłumić sygnał. Możliwość dobrania wielu charakterystyk pracy jest dość zawiła, ale ich krzywe dobiera się poprzez wartości kilku rezystorów zapiętych do układu. W trakcie pracy odbiorczej układ pracuje w pełnym zakresie możliwości. Podczas przełączania N/O zostaje załączane wyciszenie na około 20 mS aby zapobiec charakterystycznemu pykaniu w głośniku. Realizowane jest to za pomocą tranzystorów Q17 i Q22. Po układzie kompresora mamy podwójny filtr dolnoprzepustowy którego charakterystyka jest dopasowana dla modulacji SSB. Przy pracy CW dołączany jest obwód LC 700Hz który dodatkowo zawęża pasmo, a poprzez ten obwód doprowadzony jest sygnał podsłuchu tonu telegrafii w trakcie nadawania. Po tych układach zostaje go wzmocnić do poziomu napięcia głośnikowego i poprzez potencjometr regulacji wzmocnienia doprowadzony jest do układu wzmacniacza LM380 umieszczonemu na płytce front panelu. Umieszczenie nie jest przypadkowe, ponieważ do takiego wzmacniacza łatwo przedostaje się w.cz. nadajnika (stopnia końcowego). Odpowiednio krótkie ścieżki i dobrane pojemności niwelują efekt emisji skrzeczących dźwięków w głośniku podczas nadawania. Oczywiście taki wzmacniacz można odłączać przy nadawaniu dla SSB, ale przy emisji CW mamy podsłuch tonu. Pełne ekranowanie nie zawsze jest możliwe i wymaga specjalnie zaprojektowanej obudowy. Dodatkowe przełączanie może powodować kolejne stuki w głośniku. Ponieważ mamy oddzielne dwa tory wzmocnienia z regulacja arw o całkiem innych poziomach i zakresach napięć to został specjalnie zaprojektowany układ sumatora tych napięć. Zajmuję się tym układ UL14. Po odpowiednim przetworzeniu wypadkowe napięcie doprowadzone jest na wskaźnik bar-grafu syntezy i podczas odbioru pełni rolę „S-metra” To tyle o części odbiorczej.

## Tor nadawczy
W zależności od emisji, niektóre podzespoły nadajnika pełnią różne funkcje. Zacznę od SSB. Sygnał z mikrofonu poprzez flirt RC, który zapobiega przedostawaniu się w.cz., podawany jest na wzmacniacz kompresora dynamiki. Rezystor nastawny R56 pełni rolę regulacji wzmocnienia tego stopnia w zależności od poziomu sygnału z mikrofonu. Kolejne stopnie ssm2166 działają tak jak w torze odbiorczym ale ustawienie poziomu kompresji jest znacząco zredukowane. Rezystor R157 i tranzystor Q21 zmniejszają jej wartość. Kolejno tak jak w odbiorniku poprzez aktywny podwójny filtr dolnoprzepustowy, sygnał podawany jest na modulator (IC1). Aby nie było różnic częstotliwości N/O celowo został zaprojektowany jeden kwarcowy generator fali nośnej podłączony do NE602. Sygnał DSB poprzez wtórnik emiterowy (który bardzo ułatwił wykorzystanie poziomu sygnału wyjściowego z ne602) podawany jest na opisany w odbiorniku układ dopasowania oporności i podany na filtr kwarcowy SSB. Filtr może mieć szerokość 2,4-2,8 kHz oraz wykonany jako 6 lub 8 polowy o różnej stromości zboczy. Po filtrze sygnał SSB trafia na mieszacz nadajnika realizowany na układzie NE602 (IC5). Do mieszacza doprowadzony jest też sygnał heterodyny. Zmieszane sygnały z dobrze wytłumionym vfo otrzymywane są na wyjściach układu. Kolejny wtórnik emiterowy (T13) poprawił i wyrównał poziomy na wszystkich zakresach. Dodatkowy obwód LC w jego kolektorze stanowi pułapkę dla sygnału ssb 10MHz którego wiązka przedostawała się na końcówkę mocy. Poziom 10tki był około 45dB niższy jak sygnał użyteczny a po dodaniu pułapki uzyskalem kolejne 25 dB tłumienia. Nie wpłynęła ona na poziomy sąsiednich częstotliwości pasmowych 7 i 14MHz. Teraz sygnał należy odfiltrować z niepotrzebnej lustrzanej częstotliwości. Nietypowo zaprojektowałem aktywny wzmacniacz pasmowy z regulacją wzmocnienia w szerokim zakresie które jest wykorzystane podczas działania ALC. Jego wejście to równoległe obwody LC przełączane diodami, kolejno układ kaskody feta j310 i tranzystora bipolarnego NPN. Zastosowany fet ma dużą oporność wejścia która mocno nie obciąża obwodów. W jego źródle znajduje sie rezystor 100 Ohm który bardzo poprawia liniowość pracy i daje dużą odporność kaskody na przesterowanie. Z kolektora tranzystora T8, do którego podłączane są kolejne obwody LC, sygnał jest prowadzony na wzmacniacz prądowy Q15,T9 i trafia na bazę predrivera opartego o tranzystor 2SD882. Do obwodów LC dołączone są rezystory dzięki którym poziomy wzmocnienia – wyższe wzmocnienie dla niższych częstotliwości – są odpowiednio tłumione i wyrównane w całym zakresie pracy . Rezystory w bazach i brak pojemności w emiterach (sprzężenie prądowe-szeregowe) skutecznie poprawiają liniowość a sam predriver nie ma elementów indukcyjnych. Dołączany układ LC na wyjściu dodatkowo poprawia selektywność pasma 20m ponieważ w jego widmie znajduje sie lustrzana częstotliwość przemiany około 4 MHz której nie wytłumią wyjściowe filtry dolnoprzepustowe. Teraz CW. W tym trxie synteza podczas trybu CW zmienia generowaną częstotliwość . Dla odbiornika jest to klasyczne VFO przesunięte o częstotliwość przemiany a przy nadawaniu generuje sygnał bezpośredni widziany na wyświetlaczu. czas przełączenia około 1mS. Pomijane są obwody po ddsie i jego sygnał trafia prosto na mieszacz nadajnika który pełni rolę regulowanego wzmacniacza (potencjometru elektronicznego). Sygnał kluczujący poprzez szereg elementów RC i tranzystor Q10 moduluje mieszacz nadawczy w tak sygnału telegraficznego. Na jego wyjściu otrzymujemy użyteczny sygnał telegraficzny z płynnie narastającym i opadającym zboczem nie powodującym stuków o oborniku korespondenta. Dalej sygnał jest wzmocniony jak przy ssb, ale tranzystor predrivera jest kluczowany w emiterze poprzez T1 i T11 aby lepiej wytłumić pozostałości fali nośnej w przerwach titania. Dławik L39 został dodany w celu braku zmian składowej stałej – podczas kluczowania płynie taki sam prąd poprzez tranzystor kluczowany. Kilka słów o działaniu toru ALC. Zaprojektowany tor nadawczy jest dobrany z niedużym naddatkiem wzmocnienia, wystarczającego do pokrycia nierówności na danym paśmie. Moc TRXa jest celowo zależna od napięcia zasilania. Przy 12v 20 wat , przy 18-19v 50 wat. Do układu U16 zostaje doprowadzone napięcie zasilania które jest referencyjne dla mocy wyjściowej. Dostarczone są tez napięcia z mostka SWR, całość jest tak dobrana aby podczas nadawania emitować zadaną moc wyjściową, chyba że podniesie sie poziom fali odbitej i układ zredukuje napięcie sterujące wysyłane na kaskadowy wzmacniacz toru nadawczego i moc zostanie obniżona. Dzięki temu mamy zabezpieczoną końcówkę mocy.

## Końcówka mocy
Tranzystorem końcowym jest MRF186. Wykonanie w technologii LDMOS ma swoje zalety i wady. Wielką zaletą jest łatwe sterowanie bramek, nie wymagające dużej mocy sterującej. Wadą jest łatwe uszkodzenie tych bramek podczas przesterowania lub nieumiejętnego lutowania. Podczas różnych testów uszkodziłem kilka egzemplarzy i wszystkie uszkodzenia dotyczyły bramki wejściowej. Sygnał w.cz. z płytki głównej dociera na driver pracujący w klasie A z prądem spoczynkowym 250mA Tranzystor RD16 wzmacnia go do odpowiedniego poziomu, po nim zastosowałem pi filtr ograniczający pasmo powyżej 15 MHz tak aby jak najmniej harmonicznych podać na tranzystor końcowy. Sygnał zostaje odseparowany galwanicznie i symetryzowany względem bramek. Po wzmocnieniu w „mrfie” trafia na transformator mocy, który zespala obydwa kanały i doprowadza go jako sygnał niesymetryczny do obwodów dolnoprzepustowych typu podwójne PI, przełączanych przekaźnikami dla każdego pasma. Na koniec poprzez mostek SWR dociera do gniazda antenowego UC1.