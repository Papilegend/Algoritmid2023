def binaar(listike, target):
  
    vasakpool = 0
    parempool = len(listike)-1 #viimase numbri indeks
    
    while vasakpool <= parempool:
        keskpunkt = vasakpool + (parempool - vasakpool) // 2  # Keskmise indeks leidmine
        
        if listike[keskpunkt] == target:
            return keskpunkt  # Tagastab indeksi täisarvu järgi
        elif listike[keskpunkt] < target:
            vasakpool = keskpunkt + 1  #Asub Paremal pool 
        else:
            parempool = keskpunkt - 1  #Asub Vasakul pool 
    
    return "Täisarvu ei ole"


# Näite kasutamine:
sort_list = [1, 3, 5, 7, 9, 11, 13, 15] #peavad olema enne juba nö sorteeritud,muidu ei leia üles otsitavat täisarvu, nt kui list on [50,5,7,8], siis kood ei tööta
otsitav_täisarv = 5
vastus = binaar(sort_list, otsitav_täisarv)
print(vastus)  # Väljund milline indeks täisarvul on