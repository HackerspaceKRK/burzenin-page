---
title: Moduł odbiornika SDR na pasmo KF
puk_category: A
puk_year: 2013
puk_place: 5
author: sq4avs
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq4avs_moduł_odbiornika_sdr_na_pasmo_kf.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq4avs_moduł_odbiornika_sdr_na_pasmo_kf.jpg
---





 



![](assets/data/img/projects/2013-5-0.jpg) 



Odbiornik SDR na pasma krótkofalowe
-----------------------------------





 Podczas konstruowania układu duży nacisk położono na parametry odbiornika. Wykorzystano wzmacniacze różnicowe OPA1632 o niskich szumach i

 niskich zniekształceniach. Dzięki zastosowaniu w torze odbiornika czterech torów diplekserów w konfiguracji filtrów dolnoprzepustowych,

 nie występuje w nim pasożytnicza demodulacja sygnałów AM. Układ współpracuje z filtrami wejściowymi o impedancji 50 om.

 


##### Opis układu




 Schemat elektryczny przedstawiono w załączonym pliku pdf






 Sygnał wejściowy dzielony jest w dzielniku mocy z wykorzystaniem transformatora i kierowany na wejścia mieszaczy.

 Wrota wejściowe mieszaczy są izolowane między sobą. Proces mieszania odbywa się na dwóch mieszaczach zbudowanych na kluczach FST3125.

 Różnicowy produkt mieszania przepuszczany jest przez tory diplekserów pracujących w układzie filtrów dolnoprzepustowych,

 dzięki czemu na wzmacniacze różnicowe wchodzi sygnał o już ograniczonym widmie częstotliwościowym.

 Dzięki niskiej impedancji wejściowej wzmacniaczy układ jest mniej podatny na zakłócenia niż klasyczne układy pracujące z wysoką impedancją wejścia.






 Sygnał z wyjść wzmacniaczy OPA1632 odejmowany jest w klasycznej konfiguracji wzmacniacza odejmującego. Mieszacz sterowany jest czterema

 sygnałami o wypełnieniu 50 procent przesuniętymi w fazie o 90 stopni. Układ formowania sygnału kwadraturowego pracuje na układzie 74LVC74.

 W układzie tym zbadaną modyfikację pokazaną na schemacie w dolnym roku polegającą na wykorzystaniu dodatkowego bardzo szybkiego dzielnika

 wykonanego w technologii ALVC (układy pracujące w tej technologii są znacznie szybsze od standardowych układów LVC) do sterowania układem 74LVC74.

 Układ 74ALVC74 wytwarza sygnał o dwukrotnie niższej częstotliwości, ale przesunięty w fazie o 180 stopni.






 Dwa dodatkowe przerzutniki D układu 74LVC74 wytwarzają sygnał kwadraturowy dzieląc jednocześnie sygnał przez 2 (sumaryczny podział wynosi 4).

 Dzięki zastosowaniu dodatkowego układu scalonego uzyskano znacznie większą dokładność przesunięcia fazowego w porównaniu z powszechnie stosowanymi rozwiązaniami.

 Skutkuje to znaczną poprawą wytłumienia niepożądanej wstęgi bocznej szczególnie na wyższych częstotliwościach (układ modelowy pracował satysfakcjonująco do pasma 50MHz).






 Opisaną modyfikację mogę polecić do wykonania we wszystkich układach wykorzystujących układ 7474 do formowania kwadraturowego sygnału w.cz.,

 wymaga ona tylko dorobienia małej płytki drukowanej. Należy pamiętać, że układ 74ALVC może być zasilany maksymalnie z 3,6V. Błędy wzmocnienia

{% include swiatradio.html on_page="03/2014 str. 50-52" %}zano poniżej. Za błędy fazy odpowiada głównie karta dźwiękowa.




##### Testy funkcjonalne odbiornika




 Odbiornik testowany był z filtrami pasmowymi na dławikach pokazanymi na fotografii 2 i syntezerem na układzie SI570.

 Parametr IP3+ odbiornika wynosi +29dBm na paśmie 3,5MHz przy odstępie sygnałów mierzonych 2,5kHz.

 Czułość około 0,3uV dla pasma 2,5kHz i stosunku sygnał szum 10dB dla karty dźwiękowej EMU0202.







#### Do pobrania

[Schemat odbiornika SDR (plik pdf)](assets/data/download/SQ4AVS_SDR-schemat.pdf)




![](assets/img/logo/sr_logo_s.jpg)###### 03/2014 str. 50-52

 





 


