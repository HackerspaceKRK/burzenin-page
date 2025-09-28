---
title: ESP32 HamQSL XML Parser – wyświetlacz danych propagacyjnych dla radioamatorów
puk_category: C
puk_year: 2025
author:
  - sq9zaq
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq9zaq_hamqsl_xml_parser_0.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq9zaq_hamqsl_xml_parser_0.jpg
---
ESP32 HamQSL XML Parser to projekt, który łączy świat krótkofalarstwa z nowoczesną elektroniką i programowaniem mikrokontrolerów. Urządzenie, bazujące na popularnym module ESP32, pobiera aktualne dane propagacyjne ze strony HAMQSL.com w formacie XML, a następnie prezentuje je na kolorowym wyświetlaczu TFT. Całość jest w pełni autonomiczna, nie wymaga włączonego komputera, a konfiguracja odbywa się przez wygodny interfejs WWW. Kod źródłowy jest dostępny w repozytorium [GitHub](https://github.com/canislupus11/HamQSL-XML-Parser), co pozwala każdemu na modyfikację i dostosowanie funkcjonalności.

## Pierwsze uruchomienie – tryb konfiguracji

Po włączeniu urządzenia w pierwszej kolejności wykonywana jest obsługa połączenia Wi-Fi. W kodzie odpowiada za to biblioteka WiFiManager, która w przypadku braku zapisanych danych sieciowych przełącza ESP32 w tryb Access Point (AP). Nazwa sieci („HamQSL”) oraz adres IP punktu dostępowego (192.168.4.1) są nadawane automatycznie przez ESPAsyncWiFiManager. Mechanizm działa tak, że urządzenie uruchamia serwer HTTP na porcie 80 i przypisuje mu domyślny adres IP interfejsu AP. Dzięki temu użytkownik, łącząc się z wyświetloną w eterze siecią „HamQSL”, może w dowolnej przeglądarce otworzyć panel konfiguracyjny i wpisać SSID oraz hasło swojej domowej sieci Wi-Fi. Po zatwierdzeniu formularza dane są zapisywane w pamięci flash ESP32 (w obszarze NVS), a urządzenie automatycznie restartuje się i próbuje połączyć z internetem.

## Nawiązywanie połączenia i pobieranie danych

Po pomyślnym zestawieniu połączenia Wi-Fi sterowanie przejmuje moduł odpowiedzialny za komunikację z serwerem HAMQSL.com. W kodzie jest to realizowane przy pomocy obiektów WiFiClientSecure (do obsługi szyfrowanego połączenia HTTPS) oraz HttpClient z biblioteki ArduinoHttpClient. W funkcji odpowiedzialnej za odświeżanie danych, wysyłane jest żądanie GET na adres [https://www.hamqsl.com/solarxml.php](https://www.hamqsl.com/solarxml.php).

Odpowiedź serwera zawiera dokument XML z kompletem aktualnych parametrów propagacji: Solar Flux, liczba plam słonecznych (Sunspots), indeksy K i A oraz oceny warunków dla poszczególnych pasm HF i VHF. XML trafia do bufora pamięci i jest parsowany przy użyciu prostego parsera tekstowego działającego na zasadzie wyszukiwania znaczników <tag> i </tag>. Na przykład, aby odczytać Solar Flux, kod wyszukuje w buforze sekwencję <solarflux> i odczytuje zawartość aż do </solarflux>. Ta metoda, choć prymitywna, jest lekka obliczeniowo i dobrze sprawdza się na mikrokontrolerze.

## Prezentacja informacji na ekranie TFT

Po przetworzeniu danych ich prezentacją zajmują się biblioteki Adafruit GFX i Adafruit ILI9341. W sekcji setup() konfigurowane są piny SPI oraz tryb pracy wyświetlacza, w tym kierunek wyświetlania, który można dostosować do aktualnego ułożenia ekranu w obudowie, zgodnie z wygodą użytkownika (w projekcie – rotacja 3, co odpowiada obróceniu obrazu o 180° względem domyślnego). Funkcja odpowiedzialna za rysowanie ekranu korzysta z fontów z rodziny FreeSansBold, aby zapewnić czytelność przy małych rozmiarach elementów. Kolory przypisywane są w zależności od warunków: zły – czerwony, umiarkowany – żółty, dobry – zielony. Logika w kodzie realizowana jest prostym blokiem if–else, który sprawdza tekstową ocenę propagacji z XML i przypisuje odpowiadający jej kolor w formacie RGB565.

Warunki propagacyjne wyświetlane są w dwóch sekcjach – dla pasm HF oraz dla pasm VHF (6 m, 4 m, 2 m). W przypadku dobrych warunków w paśmie VHF na ekranie pojawia się zielone pole z krótką informacją, co jest możliwe (np. „tropo” lub „aurora”). Oprócz tego w górnej części ekranu znajdują się dane numeryczne: Solar Flux, Sunspots, K-index, A-index oraz X-Ray.

## Cykliczne odświeżanie danych

Interwał odświeżania ustawiony jest w kodzie na 60 minut i tutaj ważna uwaga – autor strony hamqsl.com prosi aby nie pobierać danych częściej ze względu na obciążenie jego serwera. Zresztą częstsze pobieranie danych i tak nie ma sensu, ponieważ zmieniają się najczęściej raz na godzinę.  Interwał zrealizowano to przy pomocy blokującej funkcji delay(), jednak w tym projekcie nie jest to problemem.

## Obsługa błędów i diagnostyka

Podczas pracy urządzenie stale raportuje swój stan przez port szeregowy (via USB) z prędkością 115 200 baud. Informacje obejmują zarówno proces łączenia się z Wi-Fi, jak i wynik pobrania danych czy status parsowania. Jeśli połączenie z siecią nie zostanie nawiązane w ciągu pięciu minut, w kodzie uruchamiany jest watchdog, który wymusza restart mikrokontrolera. Dzięki temu urządzenie może automatycznie odzyskać sprawność po utracie zasięgu lub zmianie parametrów sieci.

## Montaż i uruchomienie

Sprzętowo projekt jest bardzo prosty. ESP32 w wersji DevKitC lub podobnej łączy się z wyświetlaczem TFT 2,8″ ILI9341 przez SPI. Piny MISO, MOSI, SCK i CS definiowane są w sekcji konfiguracji kodu i można je dopasować do własnego modułu. Całość można zamknąć w estetycznej obudowie wydrukowanej na drukarce 3D – na portalu Thingiverse dostępne są  projekty, które mieszczą zarówno ESP32, jak i wyświetlacz.

## Podsumowanie

ESP32 HamQSL XML Parser to połączenie niewielkiego kosztu, prostej konstrukcji i dużej wartości informacyjnej. Radioamatorzy otrzymują w czasie rzeczywistym przejrzystą wizualizację warunków propagacyjnych, a dzięki otwartemu kodowi mogą dowolnie modyfikować zarówno wygląd interfejsu, jak i źródła danych. Projekt jest dobrym przykładem na to, jak za pomocą kilku bibliotek Arduino i mikrokontrolera z modułem Wi-Fi stworzyć praktyczne, codziennie używane narzędzie.


[Dokumentacja konkursowa](/assets/bin/SQ9ZAQ_hamqsl_xml_parser.odt)
