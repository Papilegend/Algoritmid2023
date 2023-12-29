def dijkstra(graaf, algus, lopp, kaal='kaugus'):
    järjekord = [(0, algus, [])] # 0 - kulu, algus - algusõlm, [] - tühi tee
    külastatud = set()  # hoitakse kõlastatud sõlmede hulka

    while järjekord:
        järjekord.sort() # sorteeerib kõige väiksema kulu järgi
        (kulu, sõlm, tee) = järjekord.pop(0) # kulu - hetkene kuluarvestus käesoleval sõlmel, sõlm - hetkel uuritav sõlm, tee - hetkene tee algussõlmest käesoleva sõlmeni
                                             # pop(0) - tagab, et võetakse esimene element, mis on kõige väiksema kuluga
        if sõlm not in külastatud: #väldib korduvaid külastusi samale sõlmele
            külastatud.add(sõlm)
            tee = tee + [sõlm] #teekonna pikkus

            if sõlm == lopp: #välistab viimase sihtkoha 
                return tee, kulu

            if sõlm in graaf: #kui sülm on graafis
                for naaber, kaare_andmed in graaf[sõlm].items():
                    uus_kulu = kulu + kaare_andmed[kaal]
                    järjekord.append((uus_kulu, naaber, tee))

    return None

# Näite kasutamine:
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

# Leia optimaalne tee kauguse põhjal
optimaalne_tee_kauguse_põhjal = dijkstra(graaf, 'Tallinn', 'Kairo', kaal='kaugus')
print("Optimaalne tee kauguse põhjal:", optimaalne_tee_kauguse_põhjal)

optimaalne_tee_kauguse_põhjal = dijkstra(graaf, 'Tallinn', 'Kairo', kaal='hind')
print("Optimaalne tee hinna põhjal:", optimaalne_tee_kauguse_põhjal)



