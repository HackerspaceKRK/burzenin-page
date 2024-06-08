---
title: VFO DDS z wyświetlaczem graficznym do transceivera wykonane z gotowych modułów z kodem open source
author: sp9mrn
classes: wide
layout: puk
tagline: ''
header:
  overlay_image: /assets/images/puk/sp9mrn_vfo_dds.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp9mrn_vfo_dds.jpg
---

![alt](/assets/images/puk/sp9mrn_vfo_dds.jpg)
{: .full}

## VFO DSS z gotowych modułów
Podstawowym założeniem projektu było wykonanie taniego i powtarzalnego VFO do samodzielnie konstruowanych transceiverów. Początkowo miało to być urządzenie jednopasmowe, w którym można samodzielnie skonfigurować zakresy przestrajania i częstotliwość pośrednią, jednak w trakcie pisania okazało się, że bez większych problemów można wykonać generator na wszystkie pasma. Urządzenie zostało wyposażone w system CAT odpowiadający standardowi CI-V firmy ICOM. Do współpracy z komputerem nie jest potrzebny żaden dodatkowy interface, ponieważ Arduino Nano będące sercem urządzenia posiada wbudowany port USB.

Dodatkowym założeniem było wykorzystanie wyświetlacza graficznego, mniejszego niż typowy wyświetlacz znakowy 2x16. Obecnie jest to wyświetlacz z Nokii 5110 - tani i łatwo dostępny. Docelowo ma to być wyświetlacz OLED o przekątnej 0,96’’.

Podstawowe moduły konstrukcyjne omawianego urządzenia to: sterownik Arduino Nano, wyświetlacz oraz moduł generatora DDS oparty na AD9850. Dodatkowo zastosowano samodzielnie wykonany moduł klawiatury analogowej oraz prosty enkoder z przyciskiem z którego wymontowano zapadkę i kilka pojedynczych włączników TACT. Montaż został wykonany na wielostykowej płytce prototypowej.

Sterownik jest zasilany z portu USB współpracującego komputera.

W celu umożliwienia zastosowania taniego enkodera o małej liczbie kroków wykorzystano centalny przycisk, który służy do cyklicznego przełączania kroku strojenia syntezy. Jeżeli zastosowany zostanie precyzyjny enkoder o większej ilości kroków na obrót (niestety dużo droższy) wówczas procedura zmiany kroku strojenia może zostać pominięta.

Oprogramowanie zostało napisane w środowisku Arduino IDE z wykorzystaniem gotowych bibliotek obsługujących zastosowane komponenty. Obsługę LCD zapewniają biblioteki Adafruit. Charakterystyczne jest użycie dwóch bibliotek z których biblioteka GFX odpowiedzialna za grafikę jest niezależna od biblioteki obsługującej konkretny sterownik wyświetlacza.

Oprogramowanie pozwala na sterowanie dziewięcioma pasmami za pomocą dwóch wirtualnych niezależnych VFO, a każde z VFO zapamiętuje nastawy częstotliwości dla poszczególnych pasm. Możliwa jest praca “split” - czyli różne częstotliwości dla nadawania i odbioru. Zastosowane rozwiązanie daje możliwość pracy crossband.

Sterowanie urządzeniem odbywa się za pomocą następujących klawiszy: bandUP, bandDOWN, SPLIT, A/B, A=B, MODE. Klawisz wyboru VFO pełni podwójną funkcję - przy dłuższym przytrzymaniu wyrównuje częstotliwość VFO pomocniczego do VFO głównego.

Oprogramowanie pomimo swojej funkcjonalności obarczone jest podstawowym błędem wynikającym z chęci dostosowania się do klasycznego układu VFOA/VFOB. Takie rozwiązanie utrudnia rozwijanie oprogramowania i będzie w najbliższym czasie przerobione do pracy w systemie MAIN/SUB VFO.