# Ülesanne 3 

## Separate Chaining 

### Separate Chaining vs Open Addressing (aja- ja ruumikompleksus)

Seperate chaining'ul on ajakompleksus O(N+α), kus α alfa tähendab elementide ja kohtade jagatist. Open Addressing'ul on aga ajakompleksus O(1/(1-α), arvestades, et α < 1. Mõlemal on halvimal juhul ajakompleksus O(n) kui on fikseeritud pikkusega räsitabel ning tabel on peaaegu täis. 
Seperate chainingul on vajab linked listide kasutamise tõttu ruumikompleksust arvestades rohkem mälu, kuid open aadrresing vähem, sest ta ei aseta kunagi mitut elementi samale kohale. 
Mõlemad on efektiivsuselt suhteliselt samal tasandil, kuid kui prioriteediks on väiksem mälukasutus, siis on mõistlikum kasutada open addressing'ut.

### Separate Chaining plussid ja miinused

#### Plussid

- Võrreldes teiste alternatiividega on lihtne loogika
- Hea kaitse halbade räsimisfunktsioonide, mis väljastavad erinevate sisendite puhul palju samu väärtusi, vastu
- Kiire, kui on ühtlane jaotus

#### Miinused

- Keskmisest suurem mäluvajadus ja mälu ebajärjepidevus 
- Kui on teatud indeksitel väga pikad linked listid, siis muutub algoritnm aeglaseks
  
 
