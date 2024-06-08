---
title: Automatyczny tuner antenowy QRP
puk_category: B
puk_year: 2011
puk_place: 2
author: 3z6aef
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/3z6aef_automatyczny_tuner_antenowy_qrp.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/3z6aef_automatyczny_tuner_antenowy_qrp.jpg
---





 



![](assets/data/img/projects/2011-2-0.jpg) 



tinyAAT - tuner antenowy QRP
----------------------------





 Projekt i wykonane urządzenie to tuner antenowy pracujący w trybie półautomatycznym i automatycznym,

 przeznaczony dla urządzeń QRP o mocy nadajnika do 15W, głównie w czasie wypraw i aktywności terenowych (SOTA, wyprawy zamkowe, itp).




##### Tryby pracy




* AUTO - strojenie automatyczne
* SEMI - strojenie wyzwalane przyciskiem TUNE
* PASS - tuner wyłączony




##### Parametry techniczne




* Zakres częstotliwości: 1,8..30 MHz
* Impedancja wejściowa: 50 Ω
* SWR wejściowy: max. 1,14:1 w całym zakresie częstotliwości roboczych
* Czas strojenia: 1..5 sekund
* Moc minimalna sygnału: 1 W (zalecane 2 W)
* Max. moc przenoszona: 20 W
* Zakres temperatur pracy: -30 .. +70 °C
* Napięcie zasilania: 9..14V
* Pobór prądu: max 10 mA (strojenie), 0,1 mA (czuwanie)
* Masa bez obudowy 170 g, masa z obudową (Hammond): 360 g
* Wymiary 100x120x135 mm (obudowa Hammond)




##### Opis konstrukcji




 Schemat elektryczny pokazano na rysunkach 7 i 8.






 Schemat elektryczny tinyAAT składa się z dwóch części: układu sterowania oraz układu wykonawczego i pomiarowego.

 W skład pierwszej części wchodzi układ scalony mikroprocesora **PIC16LF876** (Microchip) wraz z rezonatorem kwarcowym 4MHz,

 pamięć E2ROM 24C256, bufory 74HC595 (3 szt.), układ sygnalizacji (LED - 3 szt., buzzer), układ zasilania oraz opcjonalny układ

 łącza komunikacyjnego RS485.






 Mikroprocesor zawiera wszystkie bloki, niezbędne do działania urządzenia: przetworniki analogowo-cyfrowe ADC (pomiar napięć V\_REV i V\_FWD),

 licznik częstotliwości (pomiar częstotliwości sygnału), generator akustyczny (komunikaty akustyczne), bufory sterujące LED i

 trzy diody świecące (obrazowanie poziomu SWR), linie transmisji I2C dla obsługi pamięci EEPROM (pamięć nastaw) oraz linie transmisji szeregowej

 (opcjonalne łącze kompatybilne z easyATU-HMG).






 Układ wykonawczy składa się z sieci 8 toroidalnych cewek oraz 8 kondensatorów, przełączanych przekaźnikami bistabilnymi (jednocewkowymi)

 DPDT (podwójne, przełączne). Wartości cewek i kondensatorów są dobrane - w przybliżeniu - w wagach binarnych

 (kolejna wartość jest dwa razy większa niż poprzednia). Dla uzyskania odpowiedniej wartości pojemności i napięcia,

 kondensatory SMD mogą być składane z czterech elementów, łączonych szeregowo-równolegle, natomiast kondensatory przewlekane mogą być składane

 z dwóch - łączonych równolegle.






 Cewki nawinięte są na toroidalnych rdzeniach proszkowych typu T37-2 lub T50-2 (Micrometals, Amidon) drutem nawojowym w emalii (DNE).

 Przyjęto następujące wartości sieci L/C: 0.12, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16 uH oraz 5, 10, 22, 39, 82, 160, 330, 680 pF,

 co umożliwia ustawienie maksymalnej indukcyjności 31.87 uH oraz pojemności 1.33 nF






 Układ pomiarowy napięć fali padającej i odbitej składa się z dwutransformatorowego sprzęgacza Stocktona (Tandem Match Bridge),

 diod prostowniczych Schottky'ego typu 1N5711 (lub BAT85) oraz elementów dzielnika napięciowego i filtracji.

 Transformatory mostka nawinięte są na toroidalnych rdzeniach ferrytowych typu T37-77 (Micrometals).

 Układ pomiarowy częstotliwości to zwykły, diodowy ogranicznik napięcia zbudowany z uniwersalnych diod krzemowych 1N4148 (6 szt.).










 Dyskusja wybranych rozwiązań, sposób montażu, uruchomienia, użytkowania i obsługi zawiera opis konkursowy (plik pdf w sekcji "Do pobrania")






 UWAGA. Kolejne wersje (B i C) tinyAAT z dodatkowymi funkcjonalnościami powstały w latach 2012-2013, ale nie były nigdzie publikowane.

 Autor obiecał publikację na swojej stronie internetowej... Poczekamy, zobaczymy... :-/



 
#### Do pobrania

[3Z6AEF tinyAAT - opis konkursowy (plik pdf)](assets/data/download/3Z6AEF_tinyAAT.pdf)

[tinyAAT - plik .hex dla programatora](assets/data/download/tinyAAT.hex)

[Swiat Radio - 11/2011 str. 47-49](http://www.swiatradio.com.pl/virtual/modules.php?name=Downloads&d_op=getit&lid=42)


#### Opis w "Świat Radio"

{% include swiatradio.html on_page="11/2011 str. 47-49" %}

 





 


