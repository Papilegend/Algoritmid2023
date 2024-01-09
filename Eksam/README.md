# Eksamiks kordamine 


### Kirjelda Linear Search algoritmi põhiprintsiipi. Millises stsenaariumis on see kõige tõhusam?

Linear Search käib järjendis/massiivis kõik elemendid läbi, võrreldes iga elementi otsitava väärtusega. 

See on kõige tõhusam väikeste ja sorteerimata andmemahtude korral, sest suuremate andmemahtudega muutub linear search, peamiselt lineaarselt elementide läbivaatamise tõttu, ebaefektiivseks. 

### Milline tingimus peab olema täidetud, et Binary Search algoritmi saaks andmekogumil rakendada?

Andmestik peab olema soreeritud.

### Nimeta kaks olulist räsi-funktsiooni omadust

- Tagastab iga sisendi korral erineva räsi
- Tagastab sama sisendi korral alati sama räsiväärtuse
- Jaotab räsiväärtusi ühtlaselt räsitabelis
- Sisendi korral väike muutus tekitab suure muutuse räsis

### Mis on peamine erinevus eraldi aheldamise (separate chaining) ja avatud aadresseerimise (open aadressing) vahel räsitabelis?

Eraldi aheldamisel saab meetod hoida rohkem kui ühe elemendi pesas (Linked listidena või massiividena), aga avatud adresseerimise puhul on igal elemendil oma pesa.

**Eraldi aheldamise** pluss on see, et seda on lihtne rakendada ja lubab piiramatut hulka elemente, kuid nõuab lisamälu viidete jaoks, mis halvendab jõudlust, kui põrgete arv suureneb.

**Avatud adresseerimise** pluss on see, et lisamälu pole vaja, kuid piiratud räsitabeli suurusega jõudlus halveneb, kui räsitabel täitub. 







