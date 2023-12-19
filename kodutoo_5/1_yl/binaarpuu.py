""" Tegmist on objekt orienteeritud koodiga, mis teeb teatud ettevõtte ametite tähtsuse järgi
ettevõte ametipuu, mis on binary tree. Väga efektiivne rakendus see pole, kuid näitab ära, kuidas töötab binary tree"""



class tipp:
    
    def __init__(self, nimi, vanus):
        self.vasak = None
        self.parem = None
        self.nimi = nimi  
        self.vanus = vanus # Kasutan binary treesse lisamiseks ametitel "ametivanust"

    def sisesta(self, nimi, vanus):

    # Kui binary trees pole ühtegi elementi, siis lisa vaadeldav element puu tüveks
        if self.vanus is None:
            self.vanus = vanus
            self.nimi = nimi

    # Kui binary trees on tüveelement olemas, siis võrdle, kas see on suurem või väiksem tüveelemendist
        else:
            
    # Kui sisestatav sõlm on väiksem vaadeldavast sõlmest 
            if vanus < self.vanus:

    # Kui vasakpoolset sõlme pole, siis lisa see vasakule
                if self.vasak is None:
                    self.vasak = tipp(nimi, vanus)

    # Kui vasakpoolne sõlm on olemas, siis korda protsessi võttes olemasolev vasak sõlm vaadeldavaks tüveks
                else:
                    self.vasak.sisesta(nimi, vanus)
            elif vanus > self.vanus:

    # Kui parempoolset sõlm pole, siis lisa sõlm paremale
                
                if self.parem is None:
                    self.parem = tipp(nimi, vanus)

     # Kui vasakpoolne sõlm on olemas, siis korda protsessi võttes olemasolev vasak sõlm vaadeldavaks tüveks
                else:
                    self.parem.sisesta(nimi, vanus)

def printimine(tuvi):
    if tuvi is None:
        return
    else:
        print(f"Ametinimetus: {tuvi.nimi}") 
        printimine(tuvi.vasak)
        printimine(tuvi.parem)

if __name__ == "__main__":

    # Teen binary tree tüveks tegevjuhi ameti
    tuvi = tipp("Tegevjuht", 30)  

    # Lisan tegevjuhile ametivanuste abil juurde teised ametid
    tuvi.sisesta("Produktsioonijuht", 25)  
    tuvi.sisesta("Turundusjuht", 35)
    tuvi.sisesta("Tööde juhataja", 22)
    tuvi.sisesta("Müügijuht", 40)
    tuvi.sisesta("Tehasetööline", 24)
    tuvi.sisesta("Tehasetööline", 21)
    tuvi.sisesta("Müügitöötaja", 41)
    tuvi.sisesta("Müügitöötaja", 39)

printimine(tuvi)  
