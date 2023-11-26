# Ülesanne 4

## Ternary Search 

### Ülevaade ja printsiibid

Ternary Search ehk kolmikotsing on algoritm sorteeritud massivi puhul, mis jagab teatud valemi järgi massiivi kolmeks võrdseks osaks ning kontrollib ka kas otsitav element on ühest kolmest osast.

### Pseudo-kood

1. Start
2. Saa sisendiks sorteeritud massiiv ja otsitav element
3. Määra ära kõige vasakpoolsem ja parempoolsem väärtus
4. While loop, mille tingimus on, et parempoolne väärtus on suurem või võrdne vasakpoolsest
5. Leia valemi abil m1 = l + [r - l / 3] ja m2 = r - [r - l / 3] kaks punkti, mille abil jagada massiiv kolmeks
6. Vaata, kas otsitav element asub kahel leitud keskpunktil. Kui leidub, siis tagasta indeks.
7. Kui ei leidu, siis võrdle kahte punkti otsitava elemendiga ning olenevalt tõsta vasakut või paremat poolt ja korda while loopi
8. Kui vasakpoolne väärtus muutub, teda tõstes, suuremaks kui parempoolne, siis ei leidu vastavat otsitavat elementi sorteertitud massiivis.
9. Lõpp

### Ternary Search vs Binary Search ajakompleksus

Mõlema otsingualgoritmi keskmine ajakompleksus on O(log n). Ternary Search võib mingil juhul, kolmeks osaks jagamise tõttu, olla kiirem.

### Ternary vs Binary Search tõhusus

Ma arvan, et Ternary Search on oma kolmeks osaks jagamise pärast üldiselt tõhusam kui Binary Search, sest tõenäosus on suurem, et õige element leitakse kiiremini üles.
