# Ülesanne 5

## AVL puud 

### Andmestruktuurid ja peamised omadused

AVL puud on binaarotsingu puud, mis suudavad iseennast tasakaalustada läbi kindlate kriteeriumite ja tasakaalutehnikate.

#### Peamised omadused

- Tasakaalutegur - tegur, mis näitab, kas AVL puu on tasakaalus, kaldu paremale või kaldu vasakule. Kui puu on tasakaalus, siis tasakaalutegur jääb vahemikku -1 kuni 1. Kui puu on kaldu paremale, siis tasakaalutegur on ühest suurem, ja kui puu on kaldu vasakule, siis tasakaalutegur on väiksem kui -1
Tasakaalutegurit saab leida nii, et lahutad parempoolse alampuu ja vasakpoolse alampuu pikkused.

- Tasakaalutehnikad - olenevalt tasakaalutegurist, suudab AVL puu ise enda puud tasakaalustada.

### AVL puu vs punane-must puu 

#### Tõhusus

Punane-must puu suudab natukene kiiremini sisestada ja kustutuda elemente, sest tal pole nii jäigad rotateerumistehnikad, kuid samas suudab AVL puu just oma väga struktureeritud tasakaalustamisele kiiremini leida üles otsitavaid elemente. Üldpildis pole nende tõhususel suurt vahet. Mõlemate ajakeerukus on kõige paremas ja halvemas situatsioonis O(log n). 

#### Rakendamine 

Rakendaksin punast-musta puud andmebaasis/failisüsteemis, kus tuleb ette palju sisestamist ja kustutamist ja AVL puud andmebaasis/failisüsteemis, kus tuleb ette palju otsimist.


