# Ülesanne 4.

## Punase-Musta Puu (Red-Black Tree) ülevaade 

### Andmestruktuur ja põhimõtted

Punane-must on binaarotsingu puu, kus kõik puu lehed on kas mustad või punased, mis suudab peale sisestamist ja kustutamist ennast tasakaalu viia.

#### Põhimõtted 

- Iga sõlm on punast või musta värvi
- Tüvi on alati musta värvi
- Punased sõlmed ei saa omada punaseid lapsi
- Igast sõlmest teise sõlme liikudes peab tee peale jääma sama palju musti sõlmi
- Kõige pikem tee tüvest ei ole suurem kui kahega korrutatud lühema tee pikkus

### Punane-must puu vs binaarne otsingupuu 

- Mõlemad on tasakaalus olekus O(log n) ajakompleksusega, kuid kui nad peaksid tasakaalust välja minema, siis punane-must puu suudab säilitada O(log n) kompleksust, aga binaarne otsingupuu mitte, sest punane-must puu on suuteline ennast iseseisvalt tasakaalustama.
- Jõudlus ja efektiivsus on samuti kaldu punase-musta puu poole, sest binaar otsingupuu võib peale mitut lisamist ja kustutamist väga tasakaalust välja minna, mis rikub tema jõudlust
- Esimese kahe punkti tõttu ongi mõtekas kasutada pigem punane-must puud suuremate andmebaaside loomisel, sest see suudab stabiilselt hoida logaritmilist ajalist kompleksust, mida binaarne otsingupuu ei suuda.

### Punase-musta puu tasakaalustamine ja värvireeglid 

- Punase ja musta värvireeglid on peamine põhjus, miks puu suudab hoida lograitmiliselt kompleksust. Eriti on oluline see, et punasel sõlmel ei saa olla punaseid lapsi, aitab tasakaalustamisele palju kaasa.
- Tasakaalustamise tehnikad:

  1. Kui sisestatud sõlm on puu tüvi, siis see on automaatselt musta värvi.
  2. Kui sisestatud sõlme onu/tädi on punane, siis muuda sisestatud sõlme vanema, onu/tädi ja vanavanema värv.
  3. Kui sisestatud sõlme onu/tädi on must ja tekib külili keeratud kolmnurga kuju puusse, siis liiguta sisestatud sõlme vanemat sisestatud sõlmest vastassuunas.
  4. Kui sisestatud sõlme onu on must ja tekib sirge puusse, siis liiguta sisestatud sõlme vanavanema sisestatud sõlmest vastand suunas ja muuda sisestatud sõlme vanema ja (endise) vanavanema värvi. 

Need kõik tehnikad hoiavad punast-musta puud tõhusana ja tasakaalus

- Puu konstante samasuguse struktuuri hoidmine aitab punasel-mustal puul hoida stabiilset kompleksust, mis omakorda hoiab stabiilset tõhusust


  


