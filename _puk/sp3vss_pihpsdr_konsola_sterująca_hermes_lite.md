---
title: piHPSDR- konsola sterująca transceiverem Hermes Lite 2
puk_category: D
puk_year: 2025
author:
  - sp3vss
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/SP3VSS_pihpsdr_0.png
  overlay_filter: 0.5
  teaser: /assets/images/puk/SP3VSS_pihpsdr_0.png
---

Kontroler piHPSDR jest kontrolerem zdalnym do transceivera Hermes Lite 2 i innych urządzeń.. Normalnie używam go po połączeniu z komputerem przy pomocy programu SDR Console. Ten duży komputer ma wystarczającą moc, aby obsługiwać oprogramowanie w trybie cyfrowym, rejestratory i wykorzystywać wszystkie niesamowite możliwości naszych radiotelefonów. Ale platforma piHPSDR ma wystarczającą moc, aby łatwo wyobrazić sobie siedzenie w moim ulubionym fotelu, mały kontroler oparty o stolik, nogi w górze, napoje i przekąski pod ręką, może mecz futbolu na dużym ekranie i możliwość swobodnego zajmowania się DX-em lub przeżuwaniem szmat. Tak czy inaczej, taka jest moja wizja i trzymam się jej, jak widać.  Koszty materiałów oscylują w okolicach 500 złotych z wbudowanym dźwiękiem, co jest dalekie od 1200 dolarów za Maestro.

Opracowując mój projekt, chciałem czegoś czystego, kompaktowego, prostego w budowie, niedrogiego i niewymagającego projektowania płytek drukowanych. Oczywiście projekt musiał zawierać cztery enkodery obrotowe, ponieważ jest to charakterystyczny element konstrukcyjny.  Jeśli chodzi o wybór enkoderów, jest ich naprawdę wiele. Chciałem, aby były montowane na panelu, a nie na płytce drukowanej. Koszt był zdecydowanie brany pod uwagę, w przeciwnym razie wybrałbym wyłącznie enkodery optyczne, ponieważ nic nie wydaje się tak dobrze wykonane jak dobrze wykonany enkoder optyczny. Jednak tylko pokrętło strojenia ma enkoder optyczny, pozostałe enkodery to bardzo tanie urządzenia. Przyciski też zostały zamontowane na płytkach uniwersalnych aby obniżyć koszty.

Jeśli chodzi o wymagania dotyczące zasilania, Raspberry Pi, wyświetlacz, interfejsy audio USB i inne elementy pobierają łącznie zaledwie 1,5 A przy pełnej mocy podczas pracy piHPSDR. Zasilacze Raspberry Pi o natężeniu 2,5 A z dobrym kablem wydają się być w porządku. Jeśli widzisz żółtą błyskawicę w prawym górnym rogu wyświetlacza, oznacza to, że Raspberry Pi wykryło stan zbyt niskiego napięcia. Do przechowywania danych karta SD o pojemności 32 GB była oczywistym wyborem, ponieważ pamięć masowa jest tania, więc nie ma sensu jej zaniżać.

Lista materiałów:
- Wyświetlacz 7” HDMI z panelem dotykowym
- Raspberry Pi 4
- 3 enkodery z przyciskiem
- 1 enkoder optyczny
- 16 przycisków podłączonych do MCP23017

Cała konstrukcja jest stworzona przy uzyciu ogólno dostępnych materiałów. Front panel wycięty z Dibond’u, boki obudowy, nówki, gałki, przyciski i ramki drukowane drukarką 3d z materiału PET-G. Zaprojektowane w programie Fusion360.

[Dokumentacja konkursowa](/assets/bin/SP3VSS_pihpsdr.docx)

<style>.pretix-widget-item-description {
    display: none;
}
figure img {
  max-height: 500px;
  object-fit: cover;
 }
</style>
