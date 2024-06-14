---
title: Miernik pojemności
puk_category: C
puk_year: 2013
puk_nr: 12
author: sq7hjb
tagline: ""
proofread: yes
layout: puk
classes: wide
header:
  overlay_image: /assets/images/puk/sq7hjb_cmeter.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7hjb_cmeter.jpg
---

## Miernik pojemności

Miernik pojemności kondensatorów do 50 mikrofaradów, o większej dokładności odczytu. Konstruktor miernika w opisie projektu podaje możliwość uzyskania dokładności pomiaru około 0,2%.

Układ miernika jest bardzo prosty: mikroprocesor PIC16F628, wyświetlacz LCD 2x16 oraz kilka zewnętrznych elementów R, C.

Zaprojektowana została płytka drukowana PCB z drobną modyfikacją: zamiast potencjometru 10k zastosowany został opornik 9,1k i szeregowo wieloobrotowy potencjometr 1k. Ułatwia to precyzyjną kalibrację przyrządu.

Dodany został także opornik R5 (brak na schemacie), którego wartość można dobrać w zakresie od 100 do 1000 omów, w zależności od wymaganej jasności podświetlania LCD.

### Do pobrania
- [Projekt płytki drukowanej w SprintLayout (plik .LAY)](/assets/bin/sq7hjb_cmeter.lay)
- [Program dla mikroprocesora (plik .HEX)](/assets/bin/sq7hjb_cmeter.hex)

### Odnośniki
- [Oryginalny opis miernika na stronie konstruktora](http://www.romanblack.com/onesec/CapMeter.htm)


{% include swiatradio.html on_page="04/2020 str. 48-53" %}