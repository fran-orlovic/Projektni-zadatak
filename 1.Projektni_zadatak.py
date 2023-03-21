#1. projektni zadatak

from datetime import date

korisnik = {}
artikl = {}
prodaja = {}

korisnik['ime'] = input("Unesite ime korisnika: ").capitalize()
korisnik['prezime'] = input("Unesite prezime korisnika:").capitalize()
korisnik['telefon'] = int(input("Unesite telefon korisnika:"))
korisnik['email'] = input("Unesite email korisnika:").strip()

artikl['naslov'] = input("Unesite naslov artikla:").capitalize()
artikl['opis'] = input("Unesite opis artikla:").capitalize()
artikl['cijena'] = float(input("Unesite cijenu artikla:"))

dan = int(input("Unesite dan isteka prodaje: "))
mjesec = int(input("Unesite mjesec isteka prodaje: " ))
godina = int(input("Unesite godinu isteka prodaje: "))

prodaja['datum'] = date(godina, mjesec, dan)
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl

print("Informacije o artiklu:")
print(f"\tNaslov:{prodaja['artikl']['naslov']}\n\tOpis:{prodaja['artikl']['opis']}\n\tCijena:{prodaja['artikl']['cijena']}")
print("Datum isteka prodaje:")
print(f"\tDan:{prodaja['datum'].day}\n\tMjesec:{prodaja['datum'].month}\n\tGodina:{prodaja['datum'].year}")
print("Informacije o korisniku:")
print(f"\t{prodaja['korisnik']['ime']} {prodaja['korisnik']['prezime']}\n\tTelefon:{prodaja['korisnik']['telefon']}\n\tEmail:{prodaja['korisnik']['email']}")
