---
title: Uniwersalny wzmacniacz HF - 100W
puk_category: D
puk_year: 2015
puk_place: 9
author: sp9hvw
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp9hvw_uniwersalny_wzmacniacz_hf_100w.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp9hvw_uniwersalny_wzmacniacz_hf_100w.jpg
---





 



![](assets/data/img/projects/2015-9-0.jpg) 



PA HF 100W
----------





 Uniwersalny wzmacniacz mocy na pasma krótkofalowe. Możliwość wykorzystania tranzystorów MOSFET

 w różnych obudowach. Liczne zabezpieczenia i możliwości monitorowania parametrów urządzenia.




##### Opis układu




 Schemat elektryczny przedstawiono na rysunku 3.






 Na wejściu wzmacniacza jest tłumik 2dB (R4, R8, R9), którego tłumienie można dobrać w zależnosći

 od wielkości napięcia po mieszaczu TX-a i BPF. Stopień wzmacniacza na tranzystorze Q1 ma

 wzmocnienie 6dB. Wzmacniacz pracuje w układzie wspólnego emitera. W obwodzie kolektora jest dławik

 L1 (chip-bead) zapobiegający generacji (wzbudzeniu) na wyższych częstotliwościach. Następny stopień

 to tłumik na diodzie PIN i rezystorach R2, R5, R11, którymi można dobrać tłumienie.

 Tłumik jest aktywny jeżeli podajemy stan wysoki >0,7V na bazę tranzystora Q3.






 Tranzystor Q2 steruje poprzez dopasowanie na transformatorze T1 (1:1) stopniem drivera

 na tranzystorach Q4 i Q5, które pracują w układzie push-pull w klasie AB.

 Napięcie biasu podawane jest z napięcia 8V stabilizownego układem 78L08.

 Potencjometrami dostrojczymi P4 i P6 ustawiamy napięcia Ugs dla tranzystorów Q4 i Q5.






 Tranzystory Q4, Q5 nie oddają pełnej mocy i z tego względu nie przewidziano kompensacji

 temperaturowej napięcia bias. W celu poprawienia stabilności pracy tranzystorów zastosowano

 sprzężenie zwrotne dren–bramka i rezystory szeregowe w bramkach tranzystorów Q2, Q4, Q5, Q7, Q8.






 Tranzystory stopnia końcowego Q7, Q8 pracują w klasie AB i mają stabilizacje temperaturową

 realizowaną poprzez termistor NTC, zamocowany do śruby mocującej tranzystor mocy. W

 zależności od temperatury obudowy tranzystora, sterując diodą referencyjną LM431, można

 ustawić nachylenie charakterystyki porzez dobór rezystora R64 w szereg z termistorem NTC.

 Regulację przeprowadza sie potencjometrem P8, tak żeby prąd biasu tranzystorów

 nie przekraczał ustalonego prądu Idq tranzystorów mocy.




##### Zabezpieczenia




 W układzie zastosowano kilka systemów zabezpieczeń i monitorowania pracy urządzenia:






* załączanie wentylatora regulacja ustawienie progu zadziałania

 po przekroczeniu temp dopuszczalnej – włącza się tłumik,
* możliwość ograniczenia mocy (tłumik na diodzie pin),
* monitorowanie prądu PA z możliwością ustawienia progu zadziałania,

 układ działa na zwieranie napięcia biasu do masy (zatrzask na tranzystorach pnp-npn,

 odblokowanie następuje po zwolnieniu PTT),
* stabilizacja temperaturowa napięcia biasu stopnia końcowego na

 LM431 + termistor (możliwość regulacji nachylenia charakterystyki U-biasu),
* zabezpieczenie (transile) przez podaniem napięcia o odwrotnej polaryzacji i przed

 przekroczeniem napięcia dopuszczalnego,
* możliwość podania napięcia >0,7V np. od zbyt dużego SWR, następuje wtedy

 ograniczenie mocy wyjścowej.




##### Układy monitorowania




We wzmacniaczu jest monitorowany prąd pobierany przez stopień mocy. Zrealizowano to na

układzie ZXCT1009 wg aplikacji producenta. W celu zapewnienia minimalnego spadku napięcia

(można dać drut manganinowy) napięcie z układu ZXCT1009 można dodatkowo wzmocnić w LM321

(układ może pracować jako wtórnik emiterowy). Napięcie, które reguluje się poprzez ustawienie

progu potencjometrem montażowym P7, podawane jest na zatrzask realizowany na tranzystorach Q9, Q10.

Wysterowanie tych tranzystorów powoduje zwieranie napięcia biasu do potencjału masy

i tranzystory MOZSFET Q2, Q4, Q5, Q7 i Q8 zostają zablokowane.

Układ pośrednio może chronić wzmacniacz przez zbyt nadmiernym prądem

spowodowanym dużym SWR-em, spowodowanym zwarciem lub przerwą w obwodzie anteny.






PA posiada układ do sterowania wentylatora chłodzenia radiatora na układzi LM358.

Temperatura kontrolowana

{% include swiatradio.html on_page="01/2016 str. 48-50" %} Próg włączenia wentylatora

ustawiamy potencjometrem P9. Po przekroczeniu temperatury dopuszczalnej (80-90 stopni Celsjusza,

ustawiamy potencjometrem P5) jest włączany tłumik na diodzie PIN D1. Moc obniża się do 10W.

Obniżenie mocy można realizować dodatkowo poprzez sterowaniea tłumika, np. jak

będzie pracowała skrzynka antenowa.




##### Konstrukcja




Konstrukcja wzmacniacza mocy została zabudowana na radiatorze typu A4291, aktualnie

produkowanego w Kętach. PCB o wymiarach 165x99 mm została zaprojektowana pod ten

radiator, uwzględniając rozstaw użebrowania umieszczono mocowanie tranzystorów.

W miejscach na tranzystory zostały wyfrezowane otwory, gdzie na podkładkach

z miedzi o wymiarach 11x20 mm (grubosć 3mm) mocowane są tranzystory Q3, Q4, Q5.

Pod tranzystory Q7,Q8 zastosowano podkładkę miedzianą o grubośći 2mm i wymiarach 95x25 mm.






 Więcej szczegółów konstrukcji w załączonym opisie konkursowym.






 Na rysunkach 5 i 6 przedstawiono osiągnięte rezultaty we wzmacniaczu medelowym.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SP9HVW_PA-HF-100W.pdf)




#### Odnośniki

[Opis wzmacniacza na stronie SP9HVW](http://www.sp9hvw.info/wzmacniacze/krotkofalarstwo/)

 



![](assets/img/logo/sr_logo_s.jpg)###### 01/2016 str. 48-50

 





 


