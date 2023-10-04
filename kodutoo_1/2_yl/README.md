# LIFO dokumentatsioon
## Kasutatud keel: Python 3.10

## Selgitus

Tegime LIFO andmestruktuuri. Kasutasime "last in first outi" tegemiseks erivärvi taldrikuid.
Oletame, et meil on taldriku virn, kus on erivärvi taldrikud. Koodis on see kujutatud listina.
Järgmisena küsime sisendit, kas soovitakse taldrikuid virnast ära võtta või lisada.
If ja elifi abil saame teha kindlaks, millist tegevust kasutaja soovib teha.
Kui kasutaja valib tegevuse 1, siis ta lisab taldrikute stacki mingit värvi taldriku stacki otsa.
Kui kasutaja valib tegevuse 2, siis ta võtab viimasena stacki lisatud taldriku ära.

## Ajaline keerukus

O(1), sest vahet pole kui suur list selles koodis on, tegevus jääb samaks. 
Koodis saab sammuks lugeda listi lisamise ja listist elemendi eemaldamise ning sammude arv on alati sama suur.
