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

*Kahekordseid rotatasioone on raske mõista teoreetilisel tasandil, sest neid kasutatakse kompleksemates, kus on mängus juba mitu alampuud*
