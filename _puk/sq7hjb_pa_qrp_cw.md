---
title: PA QRP CW na pasmo 40m
puk_category: A
puk_year: 2013
puk_nr: 7
author: sq7hjb
tagline: ""
classes: wide
header:
  overlay_image: /assets/images/puk/sq7hjb_pa_qrp_cw.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq7hjb_pa_qrp_cw.jpg
---

![alt](/assets/images/puk/sq7hjb_pa_qrp_cw.jpg)
{: .full}

PA QRP CW na pasmo 40m
Prezentowany nadajnik małej mocy zbudowany został z przeznaczeniem dla pasma 7 MHz i pracy emisją CW QRSS (wolna telegrafia)

## Budowa i działanie nadajnika

Schemat nadajnika przedstawiono na rysunku 2.

Tranzystor 2N3904 pracuje w układzie generatora sterowanego rezonatorem kwarcowym 14 MHz. Sygnał z generatora jest dzielony przez 2 w układzie scalonym 7490, tak aby uzyskać częstotliwość 7000,8 kHz. Tranzystor BD135 jest wzmacniaczem, z którego sygnał jest kierowany na filtr dolnoprzepustowy (rysunek 5). Moc wyjściowa w egzemplarzu prototypowym wynosiła 75 mW przy zasilaniu 13,8V. Kluczowanie nadajnika odbywa się przez podawanie napięcia zasilania na kolektor tranzystora BD135 (generator i dzielnik są zasilane bez przerwy).

Układ został zmontowany na płytce drukowanej.

Dławiki zostały nawinięte na przypadkowych rdzeniach ferrytowych, tak aby uzyskać indukcyjnośco ok. 30 mikrohenrów. Transformator wyjściowy zawiera 2x10 zwojów DNE 0,3 na rdzeniu FT37-43. Cewki filtra dolnoprzepustowego zostały wykonane jako powietrzne i zawierają po 20 zwojów drutu DNE 0,3 na plastykowym karkasie o średnicy 7 mm i długości ok. 10 mm.

{% include swiatradio.html on_page="03/2014 str. 46-47" %}