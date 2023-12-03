# Ülesanne 4 

## Open Addressing 

### Ülevaade ja võrdlus 

Kasutatakse kolme meetodit: linear probing, quadratic probing ja kahekordne räsimine. Linear probing on meetod, kus samale indeksile räsitud element tõstetakse esimesele suuremale indeksile, mis on kõige lähemal. Quadratic probing on meetod, kus samale indeksile räsitud element tõstetakse ruutväärtuse võrra edasi. Kui ruutu võttes saadud koht on kinni, siis suurendatakse astendajat. Kahekordne räsimine on meetod, kus samale räsitud indeksile saadud element viiakse teisest räsimisfunktsioonist läbi, et saada teistsugune indeks. Tavaliselt avatud adresseerimise puhul viiaksegi meetodeid läbi prioriteedijärjekorras: esmalt linear probing, siis quadratic probing, ja kui ikka ei väldita kokkupõrget, siis räsitakse kahekordselt

### Tehnikate efektiivsus olukordades

Linear probing - Kui räsitabelid on väikesed ja on teada, et ei pea kaua aega elemendile kohta otsima

Quadratic Probing - Kui räsitabelid on mõõdukalt täidetud ning on vaja täituvust säilitada laiaulatuslikult

Double hashing - Kui räsitabelid on peaaegu täiesti täis ning kattuvus oht on suur



