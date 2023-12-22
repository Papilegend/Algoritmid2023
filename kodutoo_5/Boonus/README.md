# Boonusülesanne

## Binaarpuude tasakaalustamise algoritmid

### Punane-must binaaotsingu puu 

1. Kui sisestatud sõlm on puu tüvi, siis see on automaatselt musta värvi.
2. Kui sisestatud sõlme onu/tädi on punane, siis muuda sisestatud sõlme vanema, onu/tädi ja vanavanema värv.
3. Kui sisestatud sõlme onu/tädi on must ja tekib külili keeratud kolmnurga kuju puusse, siis liiguta sisestatud sõlme vanemat sisestatud sõlmest vastassuunas.
4. Kui sisestatud sõlme onu on must ja tekib sirge puusse, siis liiguta sisestatud sõlme vanavanema sisestatud sõlmest vastand suunas ja muuda sisestatud sõlme vanema ja (endise) vanavanema värvi.


### AVL puu 

#### Ühene rotatsioon

- Vasak roatsioon - Kui tasakaalutegur on suurem kui 1 ehk puu on paremale poole kaldu, siis vaadeldava sõlme parem laps saab alampuu tüveks. Vasakpoolne puu osa läheb pikemaks ja parempoolne puu osa läheb lühemaks. 
- Parem rotatsioon - Kui tasakaalutegur on väiksem kui -1 ehk puu on vasakule poole kaldu, siis vaadledava sõlme vasak laps saab alampuu tüveks. Vasakpoolne puu osa läheb lühemaks ja parempoolne puu osa läheb pikemaks.

#### Kahene rotatsioon 

- Vasak-parem rotatsioon - Kui tasakaalutegur on suurem kui 1, kui vaadeldava sõlme vasaku alampuu paremale lapsele lisati sõlm
- Parem-vasak rotatsioon - Kui tasakaalutegur on väiksem kui -1, kui vaadeldava sõlme parema alampuu vasakule lapsele lisati sõlm 

*Kahekordseid rotatasioone on raske mõista teoreetilisel tasandil, sest neid kasutatakse kompleksemates olukordades, kus on mängus juba mitu alampuud*

### Splay puud 

- zig (vasak või parem rotatsioon) - Kui vaadeldav element on vasak või parem elemenn, millel pole vanavanemat.
- zig-zig (mitu korda vasak või parem rotatsioon) - Kui vaadeldav element on ühel joonel oma vanema ja teiste eelkäijatega ühel joonel.
- zig-zag (vasak/parem ja parem/vasak rotatsioon) - Kui vaadeldav element on vasak või parem laps ning ta vanem on parem või vasak laps.

*Splay puul pole eesmärk olla tasakaalus, vaid tuua peale sisestamist, kustutamist või otsismist teatud element tüveks. Näiteks, kui otsitavat elementi ei leita, siis puu viib kõige saranasema elemendi otsitavale elemendile puu tüveks.*

### B-tree

- Poolestamine - Kui sõlme suurus läheb lubatust suuremaks, siis sõlm tehakse kaheks sõlmeks
- Liimimine - Kui kustutamise tõttu on kahel sõlmel lubatust väiksem suurus, siis need pannakse kokku
- Jagamine - Kui kustutamise tõttu on ühel sõlmel lubatust väiksem suurus, aga ühel sõlmel lubatud suurus, siis lubatud suurusega sõlm annab mingi koguse võtmeid teisele sõlmele

*B-tree ei püüa säilitada traditsioonilist tasakaalus olekut ning ei ole ka binaar otsingupuu tüüp*


## Nende puude jõudluse optimeermine erinevates rakendustes

### Punane-must binaarotsingu puu

Kasutatakse oma logaritmilise ajakompleksuse abil programmeerimiskeelte kompilaatorites, operatsioonisüsteemides, faili süsteemides, masinõppes jne. Punase-musta puu pikkuse tasakaalu ning logaritmilise ajakompleksuse tõttu on see stabiilne ja kindel tööriist.

### AVL puu

Kasutatakse sarnaselt punase-musta puudele andmebaasides, sest samamoodi on AVL puudel logaritmiline kompleksus ning suudab iseennast tasakaalustada, aga varasemalt õpitust teeb AVL puu vahepeal üleliigseid rotatsioone, et ennast tasakaalu viia, ning sellepärast on punane-must binaarotsingu puu populaarsem. 

### Splay puu

Leiab kasutust andmebaasi rakendustes, kus teatud elemendid peavad olema konstanselt kättesaadavad. Splay puu suudab tihti otsitud elemente hoida juurele lähedal, mis vähendab otsinguaega ja parandab sellega jõudlust. 

### B-tree 

Kasutatakse faili süsteemides, andmebaasides, kus B-tree suudab vähendada puu pikkust/sügavust pannes andmed ühte sõlme. 



