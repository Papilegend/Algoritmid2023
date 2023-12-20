# Ülesanne 3 

## Binaarne otsingupuu

### Andmestruktuur ja selle põhielemendid

Binaarne otsingupuu on binaarpuu, millel on alati vasak laps väiksem kui vanem ja parem laps suurem kui vanem. 
Tüvest vasakule jäävad elemendid on alati väiksemad kui tüvi ja tüvest paremale poole jäävad elemendid on suuremad kui tüvi.

#### Põhielemendid 

- Tüvi, millel pole kunagi ühtegi vanemat.
- Sõlm, millel on alati maksimaalselt kaks last ja unikaalne väärtus.
- Vasak laps ja parem laps, kus vasak laps on alati väiksem kui parem laps.

### Tasakaalustamata puude mõju BST tõhususele nign selle optimeerimine 

#### Mõju 

See mõjutab ajakeerukust, sest BST kasutab otsimisel, kustutamisel ja lisamisel puu pikkust efektiivsuse säilitamiseks, aga kui puu on tasakaalustamata, siis see muutub pigem juba linked listiks ning vajab pea kõikide toimingute tegemiseks terve puu läbi töötlema.

### Optimeerimine 

- Rotateerumine - aitab puul teatud tehnikatega tasakaalu saavutada.
- Puude kasutamine, mis tasakaalustavad ennast ise nagu Punane-Must puud ja AVL puud.
  

