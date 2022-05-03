import random
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke is None else crke

    def pravilne_crke(self):
        pravilne = []
        for crka in self.crke: 
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne    
           

    def napacne_crke(self):
        nepravilne = []
        for crka in self.crke: 
            if crka not in self.geslo:
                nepravilne.append(crka)
        return nepravilne    

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all([crka in self.crke for crka in self.geslo])

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK 

    def pravilni_del_gesla(self): 
        S = ""
        for crka in self.geslo:
            if crka in self.crke:
                S += crka + " "
            else:
                S += "_"
        return S.strip()    

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA

        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA

                else: 
                    return PRAVILNA_CRKA

            else:
                if self.poraz():
                    return PORAZ

                else: 
                    return NAPACNA_CRKA                  

with open("besede.txt", encoding="utf-8") as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))


                   