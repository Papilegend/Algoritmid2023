# Ülesanne 1

## Min-kuhja ja max-kuhja teoreetilised omadused

### Min-kuhi
- Iga vanema väärtus on väiksem või võrdne oma laste väärtustest
- Tüveelement on kuhja kõige väiksem element

### Max-kuhi
- Iga vanema väärtus on suurem või võrdne oma laste väärtustest
- Tüveelement on kuhja kõige suurem element

## Min kuhja ja max kuhja aja- ja ruumikompleksus

### Ajakompleksus

#### Sisestus 

Mõlemal kuhjal on sisestus puhul ajakompleksus O(log n), sest elementi sisestas mõlema kuhja puhul see element liigub kuhja lõppu, kus tema asukohta korrigeeritakse. O(log n)-i puhul on n kuhjas olevate elementide arv ning seda kompleksust põhjendab ka see, et kuhi kasvab logaritmiliselt.

#### Kustutamine 

Mõlemal kuhjal on kustutamise ajakompleksus samuti O(log n). Põhjendus sarnaneb sisestus ajakompleksuse põhjendusega.

#### Otsimine 

Mõlemal kuhjal on otsimise ajakompleksus O(1), sest otsimise puhul peab algoritm ainult sõlmede väärtusi vaatama, et otsitavat elementi leida.

### Ruumikompleksus

Ruumikompleksus on O(n), kus n on kuhjas olevate elementide arv. 

## Kuhja struktuuri sobivus andmete sorteerimiseks ja prioriteetjärjekordade haldamiseks

### Andmete sorteerimine 

Kuhjade puhul saab kasutada heap sorti, mis loob max-kuhja, mille ta sordib heapify meetodi abil, mida kuhi kasutab ka, kui kuhja on lisatud uus element.

### Prioriteedijärekordade haldamine 

Tänu oma kiirele aja- ja ruumikompleksusele on kuhjades efektiivne hallata prioriteedijärjekordi, mis on suured. 
