# Ülesanne 1

## Räsimine 

### Põhiidee ja eesmärk 

Räsimine on andmete muutmine läbi mingisuguse funktsiooni (tavaliselt matemaatilise funktsiooni) teistsuguseks andmekujuks, mis on tavaliselt loetamatu.

Räsimise peamine eesmärk on turvalisus ja usaldusväärsus. Peamiselt kasutatakse räsimist andmete rikkumise või muutmise tuvastamiseks ning turvalisuse tagamiseks, näiteks kasutatakse räsimist salasõnade puhul.

### Hea räsifunktsiooni omadused

- Mittejuhuslik - Sama sisendi korral on sama väljund
- Konkreetne pikkus - Erinevalt sisendist väljastab funktsiooni alati sama pika väljundi
- Kiire - Suudab erinevalt sisendist väljastada kiiresti väljundi
- Väike muutus = Suur muutus - Kui kahe sisendil on näiteks üks tähe erinevus, siis nende väljundid on täiesti erinevad
- Tagasi teisendamatu - Räsiväärtust ei saa teisendada tagasi sisendiks
- Kokkupõrkamist vältiv - Kaks erinevat sisendit ei saa kunagi sama räsiväärtus toota
- Krüptograafia teadlik - On suuteline kaitsma krüptograafia vastaste rünnakute vastu

### Kokkupõrgete (collision) tehnikad

 - Eraldi aheldamine (Separate chaining) - Kui tekib teatud räsitud indeksil kokkupõrge, siis räsitabelis pannakse andmed tavapäraselt linked listidena ketti (Nagu nimi ütlebki: "chaining"). Näiteks, kui mul 10 indeksiline räsitabel ja räsides Pauli ja Markuse telefoninumbrit ning nende telefoninumbri indeksi räsiväärtus on 2, siis need pannakse linked listina indeksile 2, kus kumbki nendest väärtustest osutab, olenevalt teostusest, teisele väärtusele.
 - Avatud adresseerimine (Open adressing) - Kasutatakse kolme meetodit: linear probing, quadratic probing ja kahekordne räsimine. Linear probing on meetod, kus samale indeksile räsitud element tõstetakse esimesele suuremale indeksile, mis on kõige lähemal. Quadratic probing on meetod, kus samale indeksile räsitud element tõstetakse ruutväärtuse võrra edasi. Kui ruutu võttes saadud koht on kinni, siis suurendatakse astendajat. Kahekordne räsimine on meetod, kus samale räsitud indeksile saadud element viiakse teisest räsimisfunktsioonist läbi, et saada teistsugune indeks. Tavaliselt avatud adresseerimise puhul viiaksegi meetodeid läbi prioriteedijärjekorras: esmalt linear probing, siis quadratic probing, ja kui ikka ei väldita kokkupõrget, siis räsitakse kahekordselt.
 - Cuckoo räsimine - Kasutatakse erinevaid räsitabeleid ja räsifunktsioone. Kui tekib kokkupõrge, siis viiakse element teise räsitabeli samale indeksile.
 - Robin Hood räsimine - Sarnane linear probingule, kuid kui samale indeksile räsitud uuem element saab endale originaalse indeksi ja samal indeksil olev element peab linear probingu abil uue indeksi leidma. 
 - Dünaamiline muutmine - Olenevalt elementide kogusest, muudab räsitabel enda suurust. 

    
