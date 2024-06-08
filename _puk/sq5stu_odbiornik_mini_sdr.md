---
title: Odbiornik mini SDR
puk_category: A
puk_year: 2013
puk_place: 6
author: sq5stu
tagline: ""
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq5stu_odbiornik_mini_sdr.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq5stu_odbiornik_mini_sdr.jpg
---





 



![](assets/data/img/projects/2013-6-0.jpg) 



Odbiornik mini SDR
------------------





 Uniwersalny odbiornik SDR wykonany na podzespołach SMD. Konstrukcja części

 odbiorczej oparta o projekty YU1LM. Oprócz pracy na jednym paśmie, dzięki

 wbudowanemu mikrokontrolerowi jest możliwa praca na kilku pasmach. Przy

 wykorzystaniu DDS na AD9850 - praca do 10MHz, a po użyciu układu Si570 - praca do

 50Mhz. Przełączanie zakresów za pomocą przycisku lub poprzez RS232. Odbiornik

 posiada wyjście sterujące do rozbudowy. Można podłączyć zewnętrze filtry pasmowe

 sterowane przekaźnikami, wyświetlacz LCD, mierzyć napięcie itp.




##### Budowa układu




 Schemat elektryczny przedstawiono na rysunku 2.






 Konstrukcja podzielna jest na bloki. Głównym z nich jest Odbiornik SDR, który wzorowany

 został na opracowaniach YU1LM.

 Po przetestowaniu kilku konstrukcji wybrałem najlepiej działającą i najłatwiejszą w

 uruchomieniu. Częstotliwość pracy odbiornika to 1/4 częstotliwości generatora. Główny

 generator pracuje na częstotliwości 14,7456 MHz, co po podzieleniu daje częstotliwość

 3,6864 Mhz. Szerokość pracy odbiornika zależy od częstotliwości próbkowania karty

 dźwiękowej naszego komputera. Próby wykorzystania zwykłej karty pracującej do 44,1

 kHz dały słabe wyniki. Lepsze karty montowane w notebookach pozwalają na

 próbkowanie z częstotliwością 48 kHz, co wydaje się minimalnym, sensownym

 wyposażeniem. Wyjście audio odbiornika podłączamy zwykłym kablem stereofonicznym

 do wejścia liniowego naszej karty. Wejście mikrofonowe z reguły dawało zbyt

 zniekształcony dźwięk. 2 jumperki w okolicy złącza audio pozwalają na wybranie

 wzmocnienia stopnia wyjściowego.






 Aby konstrukcja była rozwojowa i pozwalała na własne eksperymenty na płytce znajdują

 się dodatkowe bloki (rysunek 3).






Standardowy Generator (pole ciemno-fioletowe) pracuje po ustawieniu jumperka Źródło f

w pozycji jak pokazano na zdjęciu. Odbiornik mini-SDR ma jednak znacznie więcej

możliwości niż praca w jednym paśmie i to ograniczonym możliwościami naszej karty

dźwiękowej.






Dzięki dodaniu bloku Procesora możliwe jest sterowanie chińską syntezą na układzie

AD9850. Pracuje ona do 40Mhz, co pozwala na pracę odbiornika w zakresie 0-10 Mhz.

Mamy więc do dyspozycji już 3 pasma: 160 m, 80m i 40 m. Jumper Źródło f powinien być

przestawiony na wyższą pozycję, natomiast w syntezie niezbędne jest ustawienie poziomu

zadziałania komparatora (niebieski potencjometr), aby przebieg wyjściowy był prostokątny.

{% include swiatradio.html on_page="03/2014 str. 47-50" %}




Przełączenie jumpera na kolejny poziom pozwala na wykorzystanie wyjścia

sinusoidalnego syntezy, które jest filtrowane.

Aby przełączać pasma i zakresy zastosowano mikro switch Wybór pasma oraz 6

kolorowych led pokazujących zakres ustawionych częstotliwości. Układ może być

sterowany także z komputera za pomocą RS232C. Wówczas możemy podać dowolną

częstotliwość dostępną z syntezy.






Kolejna opcja to wykorzystanie popularnego układu Si570 pracującego do 200 MHz.

Dostępne są także wersje pracujące powyżej 1 GHz. Płytka zawiera stabilizator 3V3 oraz

konwerter poziomów pozwalający na użycie tych popularnych układów.





#### Do pobrania

[Opis konkursowy (plik pdf)](assets/data/download/SQ5STU_Mini-SDR.pdf)




#### Odnośniki

[Film z testu odbiornika Mini-SDR.](https://www.youtube.com/watch?v=pWD13Cj4b2w)

 



![](assets/img/logo/sr_logo_s.jpg)###### 03/2014 str. 47-50

 





 


