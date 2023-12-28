"""Depth first search algoritm, mis kontrollib, kas teatud suurlinn on graafis voi mitte"""

graaf = {
    
    "Tallinn": ["Riia", "Helsingi"],
    "Riia": ["Praha", "Varssavi"],
    "Varssavi": ["Berliin", "Viin"],
    "Viin": ["Rooma", "Bern", "Pariis"],
    "Pariis": ["Madrid", "London"],
    "Helsingi": ["Stockholm", "Oslo"],
    "Praha": [],
    "Berliin": ["Amsterdam", "Brussel"],
    "Rooma": [],
    "Bern": [],
    "Madrid": ["Lissabon"],
    "London": [],
    "Stockholm": [],
    "Oslo": [],
    "Amsterdam": [],
    "Brussel": [],
    "Lissabon": [],
    
    }



def dfs(algus, solm, graaf):
    """Depth first search funtksioon, mille 
    sisendiks on algussolm, otsitav solm ja graaf"""


    # Loome kylastatud solmede ja jarjekorra listi 
    kylastatud = []
    jarjekord = []

    # Lisame kylastatute hulka ja jarjekorda esimese solme 
    kylastatud.append(algus)
    jarjekord.append(algus)

    # While loop, mis kestab nii kaua, kui jarjekorras on solmesid
    while jarjekord:

        # Tostame jarjekorrast koige viimasena lisatud solme valja 
        s = jarjekord.pop()

        # Valja tostetud elemendi naabersolmed vaadatakse labi 
        for i in graaf[s]:

            # Kui naabersolmed ei ole veel kylastatud, siis lisame need kylastatute ja jarjekorra hulka
            if i not in kylastatud:

                kylastatud.append(i)
                jarjekord.append(i)

    
    # Kui solm ei ole while loopi lopenuks kylastatute hulgas, siis anna kasutajale sellest teada 
    if solm not in kylastatud:

        return f"{solm} ei kuulu antud juhul Euroopa suurlinnade hulka"
    
    # Kui solm ON while loopi lopenuks kylastatute hulgas, siis anna kasutajale sellest teada
    else: 

       return f"{solm} kuulub antud juhul Euroopa suurlinnade hulka"
    

def main ():

    print(dfs("Tallinn", "Lissabon", graaf))
    print(dfs("Tallinn", "Manchester", graaf))


main()