---
title: Procesor audio DSP
puk_category: D
puk_year: 2019
puk_place: 19
author: sp6ltp
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp6ltp_procesor_audio_dsp.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp6ltp_procesor_audio_dsp.jpg
---





 



![](assets/data/img/projects/2019-19-0.jpg) 



Procesor audio DSP
------------------





 Wielofunkcyjny moduł przetwarzający sygnały w paśmie akustycznym, przeznaczony głównie

 do cyfrowego przetwarzania sygnału z mikrofonu. Prezentowane urządzenie zostało zbudowane według

 projektu **R6DAN** i **RX9CIM**.






Najważniejsze elementy audioprocesora to:


* wydajny mikrokontroler STM32F746
* wysokiej jakości kodek audio CS4272, zawierający przetworniki ADC oraz DAC o dużym

 zakresie dynamicznym
* kolorowy wyświetlacz TFT o rozdzielczości 320x240 o przekątnej 3,2 cala







Schemat blokowy przetwarzania sygnału przedstawiono na rysunku 4, a schematy elektryczne sterowanika i otoczenia kodeka na rysunkach 2 i 3.




##### Parametry modułów funkcjonalnych audioprocesora




###### Filtr wycinający


* Zakres regulacji częstotliwości 5..1000Hz z krokiem co 5Hz
* Zakres regulacji szerokości filtra 5..300Hz z krokiem 5Hz


###### Bramka szumów


* Regulacja czasu narastania 10..100 ms z krokiem 20 ms
* Regulacja czasu podtrzymania 1..300 ms z krokiem co 1 ms
* Próg wyzwalania 0..100db regulowany co 1dB


###### Kompresor


* Regulacja czasu narastania 10..100 ms z krokiem 20 ms
* Regulacja czasu podtrzymania 1..300 ms z krokiem co 1 ms
* Próg wyzwalania 0..100db regulowany co 1dB


###### Wzmacnienie/tłumienie


* -40dB..+40dB w krokach co 1dB


###### Korektor częstotliwości (equalizer)


* 6 pasm
* regulacja -15dB..+15dB w krokach co 1 dB


###### Pogłos/echo


* opóźnienie 1..100 ms w krokach co 1 ms
* wzmocnienie echa 0..1 w krokach co 0,1


###### Ogranicznik sygnału (limiter)


* Regulacja czasu narastania 10..100 ms z krokiem 20 ms
* Regulacja czasu podtrzymania 1..300 ms z krokiem co 1 ms
* Próg ograniczania 0..10db regulowany co 1dB






 Audioprocesor zasilany jest napięciem 5V, pobór prądu nie przekracza 300mA.
{% include swiatradio.html on_page="12/2019 str. 42-44" %}






![](assets/img/logo/sr_logo_s.jpg)###### 12/2019 str. 42-44

 





 


