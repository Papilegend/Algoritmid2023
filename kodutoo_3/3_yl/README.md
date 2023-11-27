# Ülesanne 3

## Jump Search

### Ülevaade ja printsiibid

Jump search on otsingualgoritm, mis kombineerib sorteeritud masiivis hüppamist ja lineaarotsingut. Otsingualgoritmis määratakse kindel hüppamisvahemik, ja kui mingi hüppamise järel on leitud element suurem kui otsitav element, siis kasutab algoritm eelmises blokis tagurpidi lineaarotsingut. 

### Pseudo-kood

1. Start
2. Saab sisendiks sorteeritud massiivi n ja otsitava elemendi
3. Paneb paika hüppamisvahemiku: sqrt(n)
4. While loop, mille tingimus on, et leitud element on väiksem kui otsitav element
5. Kontrollib, kas esimene element massiivis on otsitav
6. Hüppab paika pandud hüppamisvahemiku järgi massiivis edasi
7. Kontrollib, kas leitud element on suurem kui otsitav element
8. Kui on, siis kasutab lineaarotsingut eelmises blokis
9. Kui otsitavat elementi ei leidnud peale lineaarotsingut, siis element puudub selles sorteeritud massiivis
10. Lõpp

### Ajaline kompleksus (vs Binary search, Linear search)

Jump Search'i ajaline kompleksus oma hüppamise tõttu on O(sqrt(n)). Võrreldes Binary Search'iga on ta natukene aeglasem, kuid kiirem kui Linear Search. Linear Search'i on aga mõtekam üldse kasutada sorteerimata andmemahu puhul.

### Stsenaarium (Kus võib olla Jump Search efektiivsem võrreldes Linear Search'i ja Binary Search'iga)

Jump Search võib olla efeketiivsem kui Linear ja Binary Search kui andmed on sorteeritud ning andmestruktuur on koostatud Linked Listi järgi.
