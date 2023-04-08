# 3.projektni zadatak
from korisnik import unos_korisnika
from kategorija import unos_kategorije
from prodaja import unos_prodaje, ispis_prodaje

korisnici = []
broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(broj_korisnika):
    korisnici.append(unos_korisnika(i + 1))

kategorije = []
broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(broj_kategorija):
    kategorije.append(unos_kategorije(i + 1))

prodaje = []
broj_prodaja = int(input("Unesite broj prodaja: "))
for i in range(broj_prodaja):
    prodaje.append(unos_prodaje(korisnici.copy(), kategorije.copy(), i + 1))

for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}:")
    ispis_prodaje(prodaja)
