---
title: Kontroler przemiennika
puk_category: D
puk_year: 2014
puk_place: 11
author: sq1gu
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq1gu_kontroler_przemiennika.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq1gu_kontroler_przemiennika.jpg
---





 



![](assets/data/img/projects/2014-11-0.jpg) 



Kontroler przemiennika
----------------------





 Ze względu na lokalizację przemiennika w miejscu trudno dostępnym, kontroler został wyposażony w dekoder

 DTMF z obszerną listą kodów do zarządzania przemiennikiem. Za pomocą radia ręcznego komendami DTMF

 można zmieniać parametry przemiennika oraz wgrywać nowe zapowiedzi. Kontroler podaje zapowiedzi głosowe oraz poziom S-metra.




##### Cechy funkcjonalne




* moduł radiowy na pasmo 2m firmy DORJI, moc 0.5/1W
* retransmisja dźwięku
* zapowiedź głosowa przy otwarciu
* podawanie poziomu sygnału (głosowy s-metr)
* znamiennik telegraficzny przy wyłączaniu
* bikon głosowy i telegraficzny
* przy pracy z akumulatora, wyłączenie komunikatów oraz skrócenie

 czasu TX w celu oszczędzania prądu




##### Sterowanie komendami DTMF lub z komputera




* ustawienie czasu reakcji na otwarcie przemiennika T1
* opóźnienie załączenia nadajnika po puszczeniu PTT T2
* opóźnienie rozpoczęcia komunikatu głosowego T3
* opóźnienie znacznika BIP po zakończeniu nadawania T4
* czas działania przemiennika po zakończeniu nadawania T5
* globalny maksymalny czas nadawania nadajnika T6
* ustawienie poziomu sygnału dla s-metra s3 do s9+
* wybór komunikatu zapowiedzi K1 - K4
* wybór komunikatu bikona K5 - K8
* nagranie zapowiedzi dla s-metra S3 do S9+
* kontrolne odsłuchanie s-metra
* nagranie zapowiedzi przemiennika
* odsłuchanie zapowiedzi przemiennika
* nagranie zapowiedzi bikona
* odsłuchanie zapowiedzi bikona




##### Układy scalone wykorzystane w konstrukcji




* Atmega168 - procesor
* MT8870de - dekoder DTMF
* ISD17240 - magnetofon cyfrowy
* PIC12F683 - detektor 1750HZ
* FT230x - USB konwerter
* NE567 - detektor CTCSS
* LM358- wzmacniacz audio





#### Do pobrania

[Opis konkursowy (plik pdf)](/assets/bin/SQ1GU_Kontroler-przemiennika-v.3.pdf)

{% include swiatradio.html on_page="02/2015 str. 48-49" %}


![](assets/img/logo/sr_logo_s.jpg)###### 02/2015 str. 48-49

 





 


