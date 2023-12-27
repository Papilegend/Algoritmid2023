"""Breadth first search kood, mis otsib välja graafist kas Tallinnast saab sõita rongiga teise Euroopa linna või mitte"""

from collections import deque 

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


def bfs (graaf, algus, solm):
    """Funktsioon, mis kaib BFS algoritmi abil terve graafi labi
    ja kontrollib, kas teatud element on selles graafis voi mitte"""
    
    
# Loome ühe listi, kuhu funktsioon paneb graafis läbi käidud elemendid ja ühe järjekorra, kuhu ta lisab elemendid, mis on järjekorras ülevaatamiseks

    kylastatud = []
    jarjekord = deque()
    
# Graafi tüvi listatakse kohe külastatud elemendiks ja järjekorras esimeseks

    kylastatud.append(algus)
    jarjekord.append(algus)
    
# While loop, mis kestab nii kaua, kui järjekorras on elemente

    while jarjekord:

# Jarjekorras esimene element visatakse järjekorrast välja
        s = jarjekord.popleft()

# Järjekorrast välja visatud elementi vaadatakse, kas tal on naabersõlmesid

        for i in graaf[s]:
            
# Kui naaber sõlmed on olemas ja neid pole veel vaadatud, siis listatakse need külasatatute hulka ja

            if i not in kylastatud:
                
                kylastatud.append(i)
                jarjekord.append(i)
                
    
# Kui sõlm pole külastatute hulgas siis prindi see välja

    if solm not in kylastatud:
         
        print(f"Tallinn-{solm} marsruuti pole olemas")
        
# Kui sõlm on külastatute hulgas siis prindi see välja

    else:
        
        print(f"Tallinn-{solm} marsruut on olemas")
                    
                   

def main():
    
    
    bfs(graaf,"Tallinn", "Lissabon")
    bfs(graaf,"Tallinn", "Istanbul")
                              
        
main()       
        
        
