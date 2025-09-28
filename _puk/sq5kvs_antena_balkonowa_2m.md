---
title: Antena balkonowa na 2m
puk_category: B
puk_year: 2025
author:
  - sq5kvs
tagline: ""
layout: puk
proofread: no
classes: wide
header:
  overlay_image: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_2.jpg
  overlay_filter: 0.5
  teaser: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_2.jpg
gallery1:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_0.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_0.jpg
gallery2:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_1.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_1.jpg
gallery3:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_2.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_2.jpg
gallery4:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_3.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_3.jpg
gallery5:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_4.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_4.jpg
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_5.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_5.jpg
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_6.jpg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_6.jpg
gallery6:
  - url: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_szkic.svg
    image_path: /assets/images/puk/sq5kvs_antena_balkonowa_na_2m_szkic.svg


---
## Na co i po co - antena balkonowa VHF

Na co dzień mieszkam w bloku w dużym mieście. Mam loggie a nademną są inni mieszkańcy.
Początkowo postanowiłem odtworzyć antenę typu X-300 lub coś podobnego, ale szybkie pomiary
pokazały że spora część anteny mogła by wystawać sąsiadom z góry, a tego nie chciałem. Stąd
powstał pomysł anteny która byłaby anteną kolinearną (podobnie jak X-200/X300) ale zasilaną
pośrodku, jak zwykły dipol. W ten sposób miałbym do dyspozycji przestrzeń w górę i w dół!
Ostatecznie zdecydowałem się na antenę 3x 1/2λ na częstotliwości 144.5MHz (rozważałem też
antenę 2x 5/8λ która mogła by być równie dobra, choć minimalnie trudniejsza w dopasowaniu).
Odpowiednie przesunięcia fazowe zapewniłem pętlami z drutu miedzianego (2.5mm2) o długości
nieco przekraczającej 1/2λ (dokładne wartości w pliku mmana).

Jako główne elementy anteny użyłem rurek aluminiowych o długości 1m, średnicy 12mm oraz
drutu miedzianego 2.5mm2 Pewnym problemem jest połączenie tych rurek z pewnym dystansem
(około 10-15cm) oraz stabilne ich zamocowanie wraz z podłączeniem pętli fazującej z drutu.
W obecnym rozwiązaniu użyłem rurek PVC (do instalacji wewnętrznych) 1/2” o długości około
15cm, do których przy pomocy śrubek i końcówek oczkowych przymocowałem pętlę fazującą.

Wnioski na pozniej - Gdy będę poprawiał konstrukcję dokonam szeregu zmian - zamiast rurek pvc
- pręt z włókna szklanego (lub innego izolatora o dobrych właściwościach mechanicznych) o
średnicy na ścisk wewnątrz rurek aluminiowych. Zamiast drutu miedzianego 2.5mm2 -
płaskownik aluminiowy mocowany na zaciski do promienników.

## Czy to ma sens

Poświęciłem kilka godzin pracy z oprogramowaniem do modelowania anten - MMana Gall Basic,
co zaowocowało takim projektem anteny:

{% include gallery id="gallery1" %}

Jak pisałem wyżej - jest to 3x 1/2 fali
Symulacje pokazały że w okolicach rezonansu będzie około 300 Omów imepdancji, potrzebne
dopasowanie do 50.
SWR już po dopasowaniu:

{% include gallery id="gallery2" %}

Z symulacji zysku wynika że sens ma i nie jest dużo gorsze od zwykłych stackowanych werticali.

{% include gallery id="gallery3" %}

## Materiały
- 3x Rurka aluminiowa długości 1m, średnica 12mm
- 1x Puszka instalacyjna hermetyczna
- 2x Dławnice kablowe dopasowane do średnicy rurek:
- Około 3m drutu miedzianego 2.5mm2 plus oczka lutownicze
- “Garść” śrubek M3 z podkładkami
- Rurka PVC instalatorska (do wody), grubościenna (średnica wewnętrzna 12mm)
- Gniazdo typu N (lub UC-1, zależnie od preferencji)
- 2x 1/4 lambda przewodu koncentryczneg do dopasowania impedancji anteny do 50Ω. Użyty w oryginale - RG316-50. Dużo można o tym poczytać na stronach DK7ZB lub PA0FRI
[strona PA0FRI](https://www.pa0fri.com/Ant/antennes.htm#E)

{% include gallery id="gallery4" %}

## Jak to złożyć

{% include gallery id="gallery6" %}

## Jak to wygląda po złożeniu

{% include gallery id="gallery5" %}

## Czy działa?
Działa, tak jak może działać wertical, w mieście, w nieoptymalnym położeniu. W czasach dobrej
propagacji udawało mi się zrobić łącność przy pomocy FT817N (czyli 5W), emisją FT8 z Litwą,
południową Polską, Ukrainą, Białorusią. Jak na warunki blokowe oceniam nieźle ## BONUS !
Przypadkiem / nieprzypadkiem, antena ta ma też dające pod rozwagę właściwości rezonansu na
paśmie 10m. Co prawda rezonans jest zbyt wysoko, bo w okolicach 29.0MHz sprawdzić . Nie ma
tu dużego zysku, jest to dipol pionowy skrócony z długości 5m do 3m ale ze skrzynką antenową
i/lub FT8 małą mocą można nadawać.

[Dokumentacja konkursowa](/assets/bin/SQ5KVS_antena_balkonowa_na_2m.pdf)

<style>.pretix-widget-item-description {
    display: none;
}
figure img {
  max-height: 500px;
  object-fit: cover;
 }

</style>
