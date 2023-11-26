def linear_search(array, target):
    """Lineaarotsingu funktsioon"""

# For loop käib olenevalt listi pikkusest, kõik elemendid ühe korra läbi
    for i in range(len(array)):
    
    # Võrdleb iga kord elementi otsitava väärtusega: Kui otsitav element on listis, siis väljastab True
        if array[i] == target:   
            return True   

    # Kui otsitavat elementi listis pole, siis väljastab False       
    return False

poe_nimekiri = ["juust", "porgand" , "kanaliha" , "koeratoit", "muna", "torusiil"]
otsitav = "muna"

if linear_search(poe_nimekiri, otsitav):
    print(f"{otsitav} on poenimekirjas")
else:
    print(f"{otsitav} ei ole poenimekirjas")


        
