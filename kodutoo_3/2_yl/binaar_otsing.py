def binary_search(array, target):
    """ Binaarotsingu funktsioon, mis leiab otsitava väärtuse täisarvulisest sorteeritud listist"""

    # Panen paika listi kõige esimese ja viimase indeksi, parem poolsest indeksist on lahutatud üks maha, sest list algab 0-ist mitte 1-st
    left = 0
    right = len(array) - 1

    # While loop, mis kestab nii kaua, kuni vasakpoolne väärtus on suurem kui parempoolne väärtus, 
    # sest kui vasakpoolne väärtus on suurem, siis see tähendab, et ei ole enam otsinguruumi
    
    while left <= right:

        # Arvutan array keskmise indeksi
        mid = (left + right) // 2

        # Kui keskmisel indeksil olev väärtus on otsitavaga sama, siis väljasta indeks
        if array[mid] == target:
            return mid
        
        # Kui keskmine väärtus on suurem otsitavast, siis nihuta parempoolset väärtust keskmisest ühe võrra alla poole
        elif array[mid] > target:
            right = mid - 1

        # Kui keskmine väärtus on otsitavast väiksem siis liiguta vasakpoolset väärtust keskmisest ühe võrra üles poole
        else:
            left = mid +1

    # Kui vasakpoolne väärtus läheb suuremaks kui parempoolne, siis tagasta see 
    
    return "Sellist väärtust ei ole selles listis"


integer_array = [3, 4, 10, 15, 22, 43, 78]
target = 11

print(binary_search(integer_array, target))
