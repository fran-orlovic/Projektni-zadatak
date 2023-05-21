from iznimke import IznimkaPrazanTekst
from iznimke import IznimkaTelefon


def provjera_informacija(telefon, email):
    try:
        if len(telefon) < 1 or len(email) < 1:
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
