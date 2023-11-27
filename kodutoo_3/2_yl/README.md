# Ülesanne 2 

## Binaarotsing

### Binaarotsing vs lineaarotsing ajakompleksus

- Binaarotsingu puhul ajakompleksus kasvab massiivi kaheks jagamise abil logaritmiliselt - O(logN)
- Lineaarotsingu puhul ajakompleksus kasvab lineaarselt elementide kasvamisega korrelatsioonis -  O(n)

#### Võrdlus

Binaarotsing on efektiivsem kui lineaarotsing, sest tema ajakeerukus on O(logN), kuid nende ajakompleksus sõltub suuresti probleemi kontekstist.


### Binaarotsing kasulikum kui lineaarotsing näide

Binaarotsing on kasulikum, kui massiiv, millest on vaja midagi otsida, on sorteeritud. Näiteks, kui oleks vaja leida 1000 inimese nimega andmebaasist kindel nimi, mis asub teadaolevalt andmabaasi teises pooles, siis kindlasti on mõtekas kasutada binaarotsingut, mitte lineaarotsingut, sest lineaarotsing hakkaks täiesti otsast nimesid läbitöötlema, mis on ebaefektiivne sellises stsenaariumis.
  
