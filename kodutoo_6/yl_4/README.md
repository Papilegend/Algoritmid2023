# Ülesanne 4 

## Bellman-Ford algoritm

### Kirjeldus

Bellman-Ford algoritm paneb esmalt paika mitme sammulisi käike saab ta teha. Selleks ta kasutab valemit V - 1, kus V on sõlmede arv. 
Iga sammuga ta saab liikuda sammu järjenumbri võrra servi. Kui on samm 1, siis ta saab algpunktist liikuda ühe serva võrra ning enamasti ta ei jõua kõikidesse graafis olevatesse sõlmedesse. 
Kui on juba samm 7 , siis algoritm saab algpunktist liikuda 7 serva võrra teistesse graafis olevatesse tippudesse. Iga sammu läbimisel uuendab ta enda andmetabelit, kus paneb kirja lühema tee algsõlmest teatud teise sõlme.

### Bellman-Ford vs Dijkstra

Dijkstra liigub algsõlmest kõige kaugemasse sõlme, külastades kõiki sõlmi, ning selle teekonna ajal uuendab algsõlmest kõige lühemat teed kõikedesse teistesse sõlmedesse, kuid Bellman-Ford käib V-1 korda graafi läbi ning iga sammu järjenumbriga saab ta samme juurde, millega liikuda serva kaupa kõikidesse teistesse sõlmedesse, samal ajal uuendades kõige lühemat teed algsõlmest kõikidesse teistesse sõlmedesse. Dijkstrat nimetatakse ahneks algoritmiks ja Bellman-Fordi mitteahneks, sest Dijkstra tahab kogu aeg liikuda graafis edasi mööda kõige lühemat teed. 

Dijkstra on kiirem (ajakompleksus O(V + E log V)) kui Bellman-Ford (ajakompleksus O(V * E), kuid Dijkstra ei suuda algoritmi implementeerida negatiivsete servaväärtustega graafis, kuid Bellman-Ford suudab. 

### Negatiivsete tsükklite tuvastamine 

Kui algoritm on V - 1 sammu läbi teinud, siis ta veel teeb ühe lisa sammu, et vaadata, kas graafis esineb mõni tsükkel. Kui sammu läbimisel mõne sõlme lühim tee muutus, siis see tähendab, et graafis on negatiivne tsükkel.

Kuna Bellman-Ford algoritm ei oska nii toime tulla negatiivsete tsükklitega, et tulemused oleksid korrektsed, siis nende tuvastamine hoiab praktikas ära igasuguseid erroreid ja valeinformatsiooni. 
