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

### Defineeri mõiste "koormustegur" räsitabeli (hash map) kontekstis.

Koormustegur - Räsitabelis salvestatudd elementide arvu ja räsitabeli kogumahu suhe. Määrab ära, millal räsitabelit suurendada 

Koormustegu = Elementide arv / kohtade arv 

### Selgita lühidalt indeksi kaardistamise (index mapping) kontseptsiooni ja selle tüüpilist kasutusjuhtu 

Igal elemendil massiivis, sõnastikus, räsitabelis on vastav indeks, mis määrab tema positsiooni. Kasutatakse peamiselt andmete paremaks organiseerimiseks


### Mis on Jump Search ja kuidas erineb see Binary Search'ist lähenemisviisi poolest?

Jump search on otsingualgoritm, mis kombineerib sorteertiud massiivis hüppamist ja lineaarotsingut. Kui hüppamise järel on leitud element suurem kui otsitav element, siis kasutab algoritm eelmises plokis lineaarotsingut

Peamiselt erineb see Binary Searchist selle poolest, et Jump Search hüppab järjendis edasi ja otsib nii otsitavat elementi, aga Binary Search jagab andmestiku pooleks ja kontrollib otsitavat elementi ning liigub võrdluse tulemuse järel vasakule või paremale 


### Selgita double hashing kontseptsiooni ja too välja üks eelis võrreldes ühekordse räsimisega.

Double hashing on meetod põrgete lahendamiseks räsitabelis, kus kasutakse kaht erinevat räsimisfunktsiooni, et leida järgmine vaba pesa andmestikus.

Double hashingu eelis ühekordse räsimise eest on see, et see võimdaldab vähendada kokkupõrgete arvu ja leida kiiremini järgmine vaba pesa, kui tekib kollisioon. 

### Miks viiakse hash tabelis läbi rehashingut ja milline on selle mõju koormustegurile?

Rehasingut viiakse läbi, et suurendada räsitabeli suurust, kui see hakkab täis minema ning koormustegur muutub suureks. See vähendab koormustegurit.










