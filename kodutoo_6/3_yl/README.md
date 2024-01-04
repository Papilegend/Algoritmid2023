# 3.Ülesanne 

## Dijkstra algoritm 

### Kirjeldus 

Dijkstra on algoritm, mille abil saab leida graafis ühest sõlmest kõiki teistesse sõlmedesse kõige lühema tee. Algoritm liigub graafis kõige lühemat teed pidi, uuendades konstantselt andmetabelit, kuhu paneb kõige lühema tee algsõlmest kõikidesse teistesse sõlmedesse kirja. 

### Efektiivne ja mitteefektiivne

### Efektiivne

Dijkstra algoritm on efektiivne, kui graafi servadel pole negatiivseid väärtusi, algsõlmeks on ainult üks sõlm ning graafil on vähem servi kui sõlmesid. 

### Mitteefektiivne

Dijkstra algoritm on mitteefektiivne, kui graafi servadel on negatiivsed väärtused, graafil on rohkem servi kui sõlmesid ning algsõlmeks rohkem kui üks sõlm.


Graafil ei tohi olla negatiivseid väärtuseid, sest see ajab dijkstra algoritmi segadusse ning algoritm hakkab valesid vastuseid ja tsükkleid tootma. Kui graafil on rohkem servasid kui sõlmesid, siis dijkstra ajakompleksus suureneb liiga palju ning teised algoritmid on mõtekamad.
Samuti kehitb see ka selle puhul, kui algsõlmesid, millest lühemat teed tahetakse leida, on rohkem kui üks.
