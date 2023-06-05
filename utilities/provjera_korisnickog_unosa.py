from iznimke import IznimkaPrazanTekst
from iznimke import IznimkaTelefon


def provjera_korisnika(telefon, email, data1, data2):
    try:
        if len(telefon) < 1 or len(email) < 1 or len(data1) < 1 or len(data2) < 1:
            raise IznimkaPrazanTekst()

        if len(telefon) != 8:
            raise IznimkaTelefon()

        if int(telefon) is False:
            raise ValueError

    except IznimkaPrazanTekst as e:
        return str(e)

    except IznimkaTelefon as e:
        return str(e)

    except ValueError:
        return 'Telefon mora biti broj!'

    else:
        return None


def provjera_artikla(naslov, opis, cijena, data):
    try:
        if len(naslov) < 1 or len(opis) < 1 or len(cijena) < 1 or len(data) < 1:
            raise IznimkaPrazanTekst()

        if int(cijena) is False or int(data) is False:
            raise ValueError

    except IznimkaPrazanTekst as e:
        return str(e)

    except ValueError:
        return 'Podatak mora biti broj'

    else:
        return None


def provjera_prodaje(korisnik, prodaja):
    try:
        if len(korisnik) < 1 or len(prodaja) < 1:
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)
