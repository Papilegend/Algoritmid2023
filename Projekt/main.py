import tkinter as tk
from tkinter import ttk

def dijkstra(graaf, algus, lopp, kaal='kaugus'):
    jarjekord = [(0, algus, [])] 
    kulastatud = set() 

    while jarjekord:
        jarjekord.sort() 
        (kulu, solm, tee) = jarjekord.pop(0) 
                                             
        if solm not in kulastatud: 
            kulastatud.add(solm)
            tee = tee + [solm] 

            if solm == lopp: 
                return tee, kulu

            if solm in graaf: 
                for naaber, kaare_andmed in graaf[solm].items():
                    uus_kulu = kulu + kaare_andmed[kaal]
                    jarjekord.append((uus_kulu, naaber, tee))

    return None

# Naite kasutamine:
graaf = {
    "Tallinn":  {"Helsingi" : {"kaugus": 90,   "hind": 100},  "Pariis"  : {"kaugus": 1800,  "hind": 130},  "London"   : {"kaugus": 1820,  "hind": 120},  "Istanbul" : {"kaugus": 2000,  "hind": 300},  "Madrid": {"kaugus": 2800, "hind": 220}},
    "Helsingi": {"Tallinn"  : {"kaugus": 90,   "hind": 100},  "London"  : {"kaugus": 1820,  "hind": 160},  "New York" : {"kaugus": 6500,  "hind": 2500}, "Kairo"    : {"kaugus": 7500,  "hind": 400}},
    "New York": {"London"   : {"kaugus": 5500, "hind": 2200}, "Helsingi": {"kaugus": 6500,  "hind": 2500}, "Tokyo"    : {"kaugus": 11000, "hind": 800},  "Sydney"   : {"kaugus": 15000, "hind": 1600}},
    "London":   {"Madrid"   : {"kaugus": 1200, "hind": 65},   "Tallinn" : {"kaugus": 1800,  "hind": 120},  "Helsinki" : {"kaugus": 1820,  "hind": 160},  "New York" : {"kaugus": 5500,  "hind": 2200}},
    "Madrid":   {"Pariis"   : {"kaugus": 1000, "hind": 70},   "London"  : {"kaugus": 1200,  "hind": 65},   "Tallinn"  : {"kaugus": 2800,  "hind": 220}},
    "Pariis":   {"Madrid"   : {"kaugus": 1000, "hind": 70},   "Tallinn" : {"kaugus": 1800,  "hind": 130},  "Kairo"    : {"kaugus": 3200,  "hind": 400},  "Sydney"   : {"kaugus": 17000, "hind": 900}},
    "Cairo":    {"Istanbul" : {"kaugus": 1200, "hind": 250},  "Pariis"  : {"kaugus": 7500,  "hind": 400},  "Helsinki" : {"kaugus": 7500,  "hind": 400}},
    "Istanbul": {"Cairo"    : {"kaugus": 1200, "hind": 250},  "Tallinn" : {"kaugus": 2000,  "hind": 300},  "Tokyo"    : {"kaugus": 9000,  "hind": 800},  "Sydney"   : {"kaugus": 15000, "hind": 700}},
    "Tokyo":    {"Sydney"   : {"kaugus": 8000, "hind": 1000}, "Istanbul": {"kaugus": 9000,  "hind": 900},  "New York" : {"kaugus": 11000, "hind": 800}},
    "Sydney":   {"Tokyo"    : {"kaugus": 8000, "hind": 1000}, "Istanbul": {"kaugus": 15000, "hind": 700},  "Pariis"   : {"kaugus": 17000, "hind": 900},  "New York" : {"kaugus": 18000, "hind": 1600}}
}

# Leia optimaalne tee kauguse pohjal
#optimaalne_tee_kauguse_pohjal = dijkstra(graaf, 'Tallinn', 'Kairo', kaal='kaugus')
#print("Optimaalne tee kauguse pohjal:", optimaalne_tee_kauguse_pohjal)

#optimaalne_tee_kauguse_pohjal = dijkstra(graaf, 'Tallinn', 'Kairo', kaal='hind')
#print("Optimaalne tee hinna pohjal:", optimaalne_tee_kauguse_pohjal)


aken = tk.Tk()
aken.title("Lennuteekonna planeerija")

aken.geometry(f"400x300+{700}+{100}")
aken.maxsize(400, 300)
aken.minsize(400, 300)

# Ülemine raam
Raam = ttk.Frame(aken, width = 398, height = 150, borderwidth = 10, relief = "groove")

# Algpunkti ja sihtpunkti muutumatu tekst
algpunkt = ttk.Label(Raam, text = "Algpunkt ✈️")
nool = ttk.Label(Raam, text = "---->")
sihtpunkt = ttk.Label(Raam, text = "Sihtpunkt ✈️")

# Combobox ning temast saadav muutuja
n = tk.StringVar()
n.set("Kaal")
kaal = ttk.Combobox(Raam, textvariable = n, values = ["Kaugus", "Hind"], state = "readonly", width = 10) 

# Algpunkti ja sihtpunkti sisend
algpunkt_sisend = tk.StringVar()
sihtpunkt_sisend = tk.StringVar()
algpunkt_sisestus = ttk.Entry(Raam, textvariable = algpunkt_sisend, width = 10)
sihtpunkt_sisestus = ttk.Entry(Raam, textvariable = sihtpunkt_sisend, width = 10)

olek = tk.StringVar()
olek2 = tk.StringVar()
olek.set("kaka")
olek2.set("toka")
tee_kuvar = ttk.Label(aken, textvariable = olek)
kulu_kuvar = ttk.Label(aken, textvariable = olek2)

# Saada nupu funktsioon
def saada():

    algpunkt = algpunkt_sisend.get()
    sihtpunkt = sihtpunkt_sisend.get()
    kaal = n.get()

    if algpunkt not in graaf or sihtpunkt not in graaf:
         
            olek.set("Selliseid linnu pole meie süsteemis")

    elif kaal == "" or kaal == "Kaal":
         
            olek.set("Vali kaal")

    else: 
         
         if kaal == "Kaugus":
              
             tee, kulu = dijkstra(graaf, algpunkt, sihtpunkt, kaal = "kaugus")

             ilus_tee = ""
             for i in tee:
                  
                  ilus_tee += f"{i} "
            

             olek.set(ilus_tee)
             olek2.set(f"{kulu} km")

         elif kaal == "Hind":
              
              tee, kulu = dijkstra(graaf, algpunkt, sihtpunkt, kaal = "hind")

              ilus_tee = ""
              for i in tee:
                  
                ilus_tee += f"{i} "
            

              olek.set(ilus_tee)
              olek2.set(f"{kulu} Є")
         

             


# Saada nupp
saada_nupp = ttk.Button(Raam, text = "Saada", state = "normal", command = saada)

# Kõikide widgetite asukoht plaanil
Raam.place(x = 1, y = 0)
algpunkt.place(x =  50, y = 10)
nool.place(x = 130, y = 10)
sihtpunkt.place(x = 170, y = 10)
kaal.place(x = 270, y = 25)
algpunkt_sisestus.place(x = 50, y = 35)
sihtpunkt_sisestus.place(x = 170, y = 35)
saada_nupp.place(x = 140, y = 90)
tee_kuvar.place(x = 120, y = 200)
kulu_kuvar.place(x = 140, y = 250)


aken.mainloop()

