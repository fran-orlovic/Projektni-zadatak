# 5.projektni zadatak
from korisnik import unos_korisnika, ispis_svih_korisnika
from kategorija import unos_kategorije, ispis_svih_kategorija
from prodaja import unos_prodaje, ispis_svih_prodaja
from utilities import unos_intervala

running = True
korisnici = []
kategorije = []
prodaje = []
while running:
    print("---------------------")
    print("1.Unos novog korisnika")
    print("2.Unos nove kategorije")
    print("3.Unos nove prodaje")
    print("4.Ispis korisnika")
    print("5.Ispis kategorija")
    print("6.Ispis prodaja")
    print("7.Zaustavi program")
    print("---------------------")
    akcija = unos_intervala(1, 7)
    if akcija == 1:
        korisnici.append(unos_korisnika(len(korisnici) + 1))
    if akcija == 2:
        kategorije.append(unos_kategorije(len(kategorije) + 1))
    if akcija == 3:
        prodaje.append(unos_prodaje(korisnici.copy(), kategorije.copy(), len(prodaje) + 1))
    if akcija == 4:
        ispis_svih_korisnika(korisnici.copy())
    if akcija == 5:
        print("Popis svih kategorija:")
        ispis_svih_kategorija(kategorije.copy())
    if akcija == 6:
        print("Popis svih prodaja:")
        ispis_svih_prodaja(prodaje.copy())
    if akcija == 7:
        running = False
