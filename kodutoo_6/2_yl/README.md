# Ülesanne 2 

## Depth-first search rakendus 

Programmeerimiskeel - Python 3.11.7

## Depth-first searchi aja- ja ruumikompleksus

### Ajakompleksus

Kuna algoritm külastab igat sõlme ja läbib igat serva üks kord, siis ajakompleksus on O(sõlm + serv), kus sõlm on graafi sõlmede arv ja serv on graafi servade arv. Parimal juhul, kui algoritm leiab kohe otsitava elemendi, siis võib ajakompleksus olla ka O(1), aga selle jaoks peab otsitav element olema kas tüvi või tüve naaber. 

### Ruumikompleksus

Nii rekurssiivse kui ka iteratiivse lähenemise puhul on ruumikompleksus O(sõlm), kus sõlm on graafi sõlmede arv. Samuti võib ruumikompleksus olla ka O(1), kui graafis on ainult mõned sõlmed. 
