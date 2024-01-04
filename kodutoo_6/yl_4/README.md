# Ülesanne 4 

## Bellman-Ford algoritm

### Kirjeldus

Bellman-Ford algoritm paneb esmalt paika mitme sammulisi käike saab ta teha. Selleks ta kasutab valemit V - 1, kus V on sõlmede arv. 
Iga sammuga ta saab liikuda sammu järjenumbri võrra servi. Kui on samm 1, siis ta saab algpunktist liikuda ühe serva võrra ning enamasti ta ei jõua kõikidesse graafis olevatesse sõlmedesse. 
Kui on juba samm 7 , siis algoritm saab algpunktist liikuda 7 serva võrra teistesse graafis olevatesse tippudesse. Iga sammu läbimisel uuendab ta enda andmetabelit, kus paneb kirja lühema tee algsõlmest teatud teise sõlme.

## Negatiivsete tsükklite tuvastamine

