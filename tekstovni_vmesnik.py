import vislice

def izpis_igre(igra):
    preostali_poskusi = vislice.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()
    return ("====================================================================================== \n" +
    "Število preostalih poskusov: {}\n".format(preostali_poskusi) +
    "Pravilni del gesla: {}\n".format(igra.pravilni_del_gesla()) +
    "Neuspeli poskusi: {}\n".format(igra.nepravilni_ugibi()) +
    "=====================================================================================")

def izpis_zmage(igra):
    return "Yabadabadu! uganil si mojo superduper besedo {}".format(igra.geslo)

def izpis_poraza(igra):
    return "Jao, res si glup... Moja superduper beseda je bila {}".format(igra.geslo)  

def zahtevaj_vnos():
    return input("Črka: ")

def pozeni_vmesnik():
    igra = vislice.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == vislice.ZMAGA:
            print(izpis_zmage(igra))
            break

        elif stanje == vislice.PORAZ: 
            print(izpis_poraza(igra))
            break     


