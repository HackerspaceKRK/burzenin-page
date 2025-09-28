---
title: Przełącznik antenowy 2x6
puk_category: B
puk_year: 2025
author:
  - sq9nje
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq9nje_przełącznik_antenowy_0.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq9nje_przełącznik_antenowy_0.jpg
gallery1:
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_1.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_1.jpg
gallery2:
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_2.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_2.jpg
gallery3:
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_3.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_3.jpg
gallery4:
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_4.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_4.jpg
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_5.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_5.jpg
gallery5:
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_6.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_6.jpg
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_7.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_7.jpg
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_8.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_8.jpg
  - url: /assets/images/puk/sq9nje_przełącznik_antenowy_9.jpg
    image_path: /assets/images/puk/sq9nje_przełącznik_antenowy_9.jpg

---

Prezentowany przełącznik antenowy pozwala na podłączenie sześciu anten i dwóch transceiverów. Przełącznik może zostać podłączony do sieci WiFi. Oferuje wtedy interfejs webowy, który umożliwia sterowanie za pomocą przeglądarki z wielu stanowisk. Dostępne jest również API dzięki któremu możliwa jest integracja z innymi aplikacjami. Urządzenie posiada również interfejs RS485, który można wykorzystać do przewodowego sterowania przełącznikiem za pomocą prostych komend.

Urządzenie składa się z dwóch płytek drukowanych: modułu przekaźników oraz modułu interfejsów, które zostały zaprojektowane w programie KiCAD.


## Moduł przekaźników

Moduł przekaźników składa się z sześciu jednakowwych sekcji, po jednej dla każdej anteny. Każda z sekcji umożliwia podłączenie anteny do radia 1, radia 2 lub sztucznego obciążenia 50 omów o mocy 2W. Zastosowano popularny układ trzech przekaźników, który uniemożliwia jednoczesne podłączenie obydwóch TRXów do tej samej anteny oraz zapewnia zadowalającą izolację.

{% include gallery id="gallery1" %}

Zastosowane przekaźniki z powodzeniem nadają się do przełączania sygnałów z nadajników o pełnej mocy licencyjnej (1,5kW).

Wszystkie porty antenowe zostały zabezpieczone iskrownikami gazowanymi (GDT) co ma pomóc w zabezpieczeniu wejść radiostacji przed wysokimi napięciami powstającymi podczas niedalekich wyładowań atmosferycznych lub gromadzenia się ładunków elektrostatycznych w antenach. Przełącznik jednak nie powinien być traktowany jako element zapewniający pełną ochronę odgromową.

Izolację między portami TRXów przy wybranych sąsiednich antenach zmierzono za pomocą NanoVNA. Uzyskany wynik to:
lepiej niż 75dB poniżej 10MHz,
lepiej niż 65db poniżej 30MHz,
lepiej niż 50dB poniżej 50MHz.

{% include gallery id="gallery2" %}

## Moduł interfejsów

Głównym elementem modułu interfejsów jest płytka ESP32 DevKit v1. Moduł wyposażony jest również w half-duplexowy interfejs RS485 z automatycznym wykrywaniem kierunku transmisji oraz stabilizator napięcia 5V.

Obok gniazda sygnałów sterujących do podłączenia modułu przekaźników znajduje się dodatkowe złącze SAO (Simple Add-On). W złączu wyprowadzone zostały sygnały magistrali I2C, dwa piny GPIO oraz zasilanie 3,3V i masa. W przyszłości może ono zostać użyte do rozszerzenia możliwości sprzętowych przełącznika np. o wyświetlacz, dekoder pasm itp.

Firmware dla mikrokontrolera ESP32, będącego sercem układu, został napisany przy użyciu frameworku Arduino w środowisku PlatformIO.

## Obudowa

Przełącznik przystosowany jest do montażu w obudowie Gainta G218 z poliwęglanu. Do obudowy została zaprojektowana pokrywa ze wszystkimi niezbędnymi otworami, która następnia została wydrukowana na drukace 3D. W przypadku braku dostępu do drukarki, można wywiercić otwory w głąbszej części obudowy (płytka przekaźników jest zbyt szeroka by zamontować ją do oryginalnej pokrywy).

{% include gallery id="gallery3" %}

Alternatywnie można wykorzystać obudowę aluminiową Gainta BS11, lecz należy wówczas zastosować moduł ESP32 z zewnętrzną anteną WiFi.

## Interfejs webowy

Przy pierwszym uruchomieniu urządzenie startuje w trybie konfiguracyjnym i działa jako access point udostępniający sieć WiFi o nazwie AntennaSwitch. Po podłączeniu do tej sieci użytkownik zostanie przekierowany do captive portalu w przeglądarce internetowej. Jeśli strona nie otworzy się automatycznie, można ją znaleźć pod adresem http://192.168.4.1. Strona pozwala wybrać sieć WiFi, do której urządzenie ma się podłączyć, ustawić hasło do tej sieci oraz nazwę hosta. Po zapisaniu ustawień urządzenie restartuje się automatycznie i następuje próba podłączenia do wybranej sieci WiFi. W przypadku kiedy takie podłączenie się nie powiedzie (np. jeśli sieć nie jest już dostępna), urządzenie przechodzi ponownie w tryb konfiguracyjny.

{% include gallery id="gallery4" %}

Urządzenie wykorzystuje protokół DHCP do pobrania adresu IP. Adres ten można więc sprawdzić wyświetlając aktywne dzierżawy np. na domowym routerze. Dla ułatwienia urządzenie implementuje też protokół mDNS pozwalający na dostęp do niego za pomocą ustawionej nazwy hosta z sufiksem .local. Domyślnie interfejs webowy urządzenia dostępny jest po otwarciu w przeglądarce adresu http://antenna.local.

{% include gallery id="gallery5" %}

Główna część interfejsu składa się z trzech kolumn. Środkowa kolumna Antennas zawiera nazwy lub opisy anten. W kolumnach Radio 1 i Radio 2 znajdują się przyciski umożliwiające wybór anteny podłączonej do każdego trasceivera.

Strona może być otwarta jednocześnie w wielu przeglądarkach, a stan wybranych anten aktualizowany jest w czasie rzeczywistym. Dzięki temu operatorzy każdej z dwóch radiostacji mogą mieć ją otwartą na swoim stanowisku i operować przełącznikiem bez konieczności dodatkowej koordynacji.

W domyślnym trybie przycisk odpowiadający antenie wybranej dla jednego radia jest wyszarzony dla drugiego radia. Istnieje jednak możliwość włączenia trybu, który umożliwia zamianę anten pomiędzy radiami. W tym trybie, jeśli operator radia 1 chciałby skorzystać z anteny aktualnie podłączonej do radia 2, może kliknąć przycisk odpowiadający tej antenie, a przełącznik automatycznie zamieni anteny między radiami (radio 1 zostanie podłączone do anteny pierwotnie podłączonej do radia 2, a radio 2 - do anteny z radia 1). Przełącznik dla tego trybu znajduje się na stronie ustawień dostępnej po kliknięciu przycisku Settings.

Strona ustawień pozwala wpisać nazwy anten podłączonych do przełącznika. Można tam włączyć tryb zamiany anten opisany wyżej, a także tryb do pracy z jednym radiem, który ukrywa kolumne przycisków dla radia 2. Strona ta pozwala też na restart użądzenia, zmianę nazwy hosta oraz zresetowanie ustawień sieciowych.

W lewym dolnym rogu strony głównej znajduje się przycisk pokazujący status połączenia przeglądarki do przełącznika. Jego kliknięcie wyświetla stronę ze szczegółowymi informacjami o stanie urządzenia takimi jak: adres IP, MAC, nazwa sieci WiFi, jakość sygnału WiFi, użycie pamięci, uptime czy aktualnie wybrane anteny.

[Dokumentacja konkursowa](/assets/bin/SQ9NJE_Przełącznik-antenowy-6x2.pdf)

<style>.pretix-widget-item-description {
    display: none;
}
figure img {
  max-height: 500px;
  object-fit: cover;
 }

</style>
