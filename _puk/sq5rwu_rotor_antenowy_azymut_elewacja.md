---
title: Rotor antenowy azymut/elewacja
puk_category: B
puk_year: 2015
puk_place: 4
author: sq5rwu
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq5rwu_rotor_antenowy_azymut_elewacja.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq5rwu_rotor_antenowy_azymut_elewacja.jpg
---





 



![](assets/data/img/projects/2015-4-0.jpg) 



Rotor antenowy azymut/elewacja
------------------------------





 Celem projektu było zrealizowanie lekkiego rotora antenowego (w azymucie i elewacji), który może być używany na wyjazdach.

 W tym celu zastosowano obrotnicę do kamer przemysłowych zasilaną napięciem 24V AC (chińskiej produkcji), co sprawdziło się doskonale.




##### Szczegóy budowy




Zaprojektowano i skonstruowano sterownik składający się z modułu wykonawczego sterującego silnikami.

Głównymi elemetami są: sterowanie driverami do silników krokowych z regulacją maksymalnego prądu, odczyt pozycji w elewacji

z użyciem akcelerometru i w azymucie z użyciem kompasu.






 Drugą część stanowi moduł lokalny wyposażony w wyświetlacz LCD, joystick, przyciski sterujące i złącze USB,

 pozwalające na sterowanie rotorem z użyciem protokołu Yaesu. Oprogramowanie sterownika bazuje na kodzie stworzonym

 przez Anthony&apos-ego **K3NG** dla środowiska Arduino (Atmel AVR) i rozwijanego przez krótkofalowców. P

 




 W urządzeniu wykorzystano łatwo dostępne gotowe moduły produkcji chińskiej

 (przetwornice zasilające, drivery silników, moduły akcelerometru i kompasu itd.).






 Bieżące położenie rotora odczytuje się:

 

* w azymucie - za pomocą kompasu cyfrowego HMC5883L, zrealizowanego na module GY-80 - trójosiowy, 12-bitowy kompas o zakresie pomiarowym do 8,1 gausa.
* w elewacji - za pomocą cyfrowego akcelerometru ADXL345, zrealizowanego na module GY-291, co umozliwia trójosiowy pomiar przyspieszenia w zakresie 2..16 G.





Położenie wyświetlane jest wyświetlane jest na tanim i łatwo dostępnym wyświetlaczy LCD NOKIA 3310.






{% include swiatradio.html on_page="03/2016 str. 48-50" %}aw. Cyklicznie co 1 sekundę, moduł sterowania odpytuje moduł wykonawczy

 o bieżące położenie (azymut/elewacja). Informacje te sa wyświetlane na LCD i przekazywane do komputera. Jeśli komputerawyśle komendę nakazującą powrót do określonego położenia,

 to sterownik na podstawie znanej pozycji biezącej, spowoduje odpowiednie obroty góra/dół, prawo/

 /lewo. Następnie kontroluje się, czy pozycja została osiągnięta.






 W dowolnym momencie można przejść na sterowanie ręczne, poprzez przyciśnięcie jednego z cztyerech przycisków lub zadanie

 kierunku joystickiem. Użycie drążka sterującego umożliwia sterowanie prędkością ruchu, któa jest proporcjonalna do

 wychylenia joysticka.







![](assets/img/logo/sr_logo_s.jpg)###### 03/2016 str. 48-50

 





 


