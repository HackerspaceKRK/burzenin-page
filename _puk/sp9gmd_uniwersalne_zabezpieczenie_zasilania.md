--- 
title: Uniwersalne zabezpieczenie zasilania radiostacji 13,8V oparte o LTC4368
puk_category: D
puk_year: 2024
author: 
  - sp9gmd
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sp9gmd-zabezp-004.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sp9gmd-zabezp-004.jpg
gallery1:
  - url: /assets/images/puk/sp9gmd-zabezp-000.jpg
    image_path: /assets/images/puk/sp9gmd-zabezp-000.jpg
gallery2:
  - url: /assets/images/puk/sp9gmd-zabezp-004.jpg
    image_path: /assets/images/puk/sp9gmd-zabezp-004.jpg
gallery3:
  - url: /assets/images/puk/sp9gmd_2.png
    image_path: /assets/images/puk/sp9gmd_2.png
gallery4:
  - url: /assets/images/puk/sp9gmd_1.png
    image_path: /assets/images/puk/sp9gmd_1.png

---


### Uniwersalne zabezpieczenie zasilania radiostacji 13,8V oparte o LTC4368

Układ został opracowany z myślą o modernizacji zasilacza Icom PS-55,
ale szybko zdałem sobie sprawę z szerokiego wachlarza zastosowań.
Układ LTC4368 został opracowany przez firmę Analog Devices. Jego użycie pozwala
zbudować zabezpieczenie przed zbyt niskim, zbyt wysokim napięciem oraz uchroni
odbiornik przed poborem zbyt dużego prądu. Dodatkową zaletą jest wbudowany
mechanizm tłumienia tętnień sieci 50/60Hz. Do działania kość wymaga zaledwie
parunastu elementów zewnętrznych!

Wyobraźmy sobie, że używamy zasilacza liniowego 13,8V w którym któryś z tranzystorów
ograniczających napięcie zostaje przebity. W rezultacie na wyjściu pojawi się pełne
napięcie niestabilizowane.

{% include gallery id="gallery1" %}

Jeżeli zasilacz jest wyposażony np. w układ crowbar widoczny na obrazku powyżej to
powinien on w ok. 100ms przepalić bezpiecznik i zapobiec dalszym uszkodzeniom
powodowanym przez wysokie napięcie. Lecz co się stanie jeśli takiego zabezpieczenia nie
ma bądź np. z powodu wadliwego styku na bramce nie zostanie wyzwolony tyrystor?

Przenieśmy się na chwilę poza mury domu. W naszym gronie jest przynajmniej garstka
osób zasilajacych transceiver z akumulatora samochodowego przy pracy terenowej. Na
pewno komuś zdażyło się zostawić załączone radio, położyć się spać a po przebudzeniu nie
być w stanie uruchomić silnika. Ustawiając próg zadzialania zabezpiecznia przed zbyt
niskim napięciem na np. 11,5V chronimy się przed tego typu nieprzyjemną niespodzianką.

Omówmy zatem działanie układu.

{% include gallery id="gallery3" %}

Rezystory R1-R4 służą do ustawiania progu zadziałania zabezpieczeń OVP oraz UVP. Ich
wartości można wyliczyć z przygotowanego przeze mnie arkusza kalkulacyjnego:
https://docs.google.com/spreadsheets/d/1JJixLXgRfEJ9zyeao0jM5kgU5lX_FztHwGI2o6z92
GI/edit?gid=0#gid=0
Kondensator C2 ustala czas po jakim układ będzie próbował ponownie otworzyć MOSFET
po zadziałaniu zabezpiecznia nadprądowego.
Na płytce przewidziano 6 miejsc na rezystory bocznikujące. Umożliwia to zastosowanie
popularnych rezystorów 0,1Ohm. Zabezpieczenie uruchamia się gdy spadek napięcia na
rezystorze wyniesie 50mV. Zatem montując jeden rezystor 0,1Ohm ustawiamy próg
zadziałania zabezpieczenia na 5A, montując 2 ustalimy zabezpieczenie na 10A itd.
MOSFET został dobrany tak, żeby pracował w obszarze SOA przy prądzie ok. 22A i napięciu
14V wystarczającym dla większości transceiverów o mocy 100W.

Kondensator C3 ogranicza prąd rozruchowy przy uruchamianiu MOSFETa.
Dioda D1 sygnalizuje zadziałanie zabezpiecznia.
Układ został wykonany na dwuwarstwowej płytce z laminatu FR-4. Z uwagi na duże prądy
występujące w ukladzie zastosowano vias stitching. Na płytce umieszczono dwa gniazda
XT60 które umożliwiają łatwe podłączenie układu w terenie.

{% include gallery id="gallery4" %}

Układ złożony ze sprawnych elementów powinien działać od razu. Po złożeniu należy
sprawdzić poprawność działania OVP, UVP oraz OCP.

Do sprawdzenia działania zabezpiecznia nadprądowego można użyć kilku żarówek od
świateł długich (12V 60W) połączonych równolegle lub sztucznego obciążenia.
Na zdjęciu widać zmontowany i uruchomiony układ na wcześniejszej wersji PCB. Niestety
na płytce był błąd – jedno gniazdo XT 60 było odwrócone. Po przylutowaniu go od spodu
układ zadziałał poprawnie.

[Dokumentacja konkursowa](/assets/bin/SP9GMD_D_uniwersalne_zabezpieczenie_zasilania_radiostacji.pdf)


{% include gallery id="gallery2" %}