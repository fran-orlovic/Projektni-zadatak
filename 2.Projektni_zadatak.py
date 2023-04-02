# 2. projektni zadatak

from datetime import date

# # KORISNICI # #
korisnici = []
broj_korisnika = int(input("Unesite broj korisnika: "))
for i in range(broj_korisnika):
    korisnik = {}
    j = i + 1
    korisnik['ime'] = input(f"Unesite ime {j}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {j}. korisnika: ").capitalize()
    korisnik['telefon'] = int(input(f"Unesite telefon {j}. korisnika: "))
    korisnik['email'] = input(f"Unesite email {j}. korisnika: ").strip()
    korisnici.append(korisnik)
# # # # #
# # KATEGORIJE # #
kategorije = []
broj_kategorija = int(input("Unesite broj kategorija: "))
for i in range(broj_kategorija):
    kategorija = {}
    k = i + 1
    kategorija['naziv'] = input(f"Unesite naziv {k}. kategorije: ").capitalize()
    # # ARTIKLI # #
    artikli = []
    broj_artikala = int(input(f"Unesite broj artikala za {k}. kategoriju: "))
    for j in range(broj_artikala):
        artikl = {}
        l = j + 1
        artikl['naslov'] = input(f"Unesite naslov {l}. artikla: ").capitalize()
        artikl['opis'] = input(f"Unesite opis {l}. artikla: ").capitalize()
        artikl['cijena'] = float(input(f"Unesite cijenu {l}. artikla: "))
        artikli.append(artikl)
    # # # # #
    kategorija['artikli'] = artikli.copy()
    kategorije.append(kategorija)
# # # # #
# # PRODAJE # #
prodaje = []
broj_prodaja = int(input("Unesite broj prodaja: "))
for i in range(broj_prodaja):
    prodaja = {}
    k = i + 1
    dan = int(input(f"Unesite dan isteka {k}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {k}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {k}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)
    print(f"Odaberite korisnika {k}. prodaje")
    for index, korisnik in enumerate(korisnici, start=1):
        print(f"\t{index}.{korisnik['ime']} {korisnik['prezime']}")
    odabir_korisnika = int(input(f"Odabrani korisnik: "))
    prodaja['korisnik'] = korisnici[odabir_korisnika-1]
    print(f"Odaberite kategoriju {k}. prodaje")
    for index, kategorija in enumerate(kategorije, start=1):
        print(f"\t{index}.{kategorija['naziv']}")
    odabir_kategorije = int(input(f"Odabrana kategorija: "))
    print(f"Odaberite artikl {k}. prodaje")
    for index, artikl in enumerate(kategorije[odabir_kategorije-1], start=1):
        print(f"\t{index}. {kategorije[odabir_kategorije-1]['artikli'][index-1]['naslov']}")
    odabir_artikla = int(input("Odabrani artikl: "))
    prodaja['artikl'] = kategorije[odabir_kategorije-1]['artikli'][odabir_artikla - 1]
    prodaje.append(prodaja)
# # # # #
for index, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {index}:")
    print("Informacije o korisniku:" +
          f"\n\tIme:{prodaja['korisnik']['ime']}" +
          f"\n\tPrezime:{prodaja['korisnik']['prezime']}" +
          f"\n\tTelefon:+{prodaja['korisnik']['telefon']}" +
          f"\n\tEmail:{prodaja['korisnik']['email']}")
    print("Informacije o artiklu:" +
          f"\n\tNaslov: {prodaja['artikl']['naslov']}" +
          f"\n\tOpis: {prodaja['artikl']['opis']}" +
          f"\n\tCijena: {prodaja['artikl']['cijena']}")
    print("Datum isteka:" +
          f"\n\tDan: {prodaja['datum'].day}" +
          f"\n\tMjesec: {prodaja['datum'].month}" +
          f"\n\tGodina: {prodaja['datum'].year}")
    print("----------------------------------------")
# # # # #
