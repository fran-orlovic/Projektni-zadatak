

def ispis_artikla(artikl):

    print(f"\tNaslov: {artikl['naslov']}")
    print(f"\tOpis: {artikl['opis']}")
    print(f"\tCijena: {artikl['cijena']}")


def get_artikl(index, artikl):
    return f"{index}. {artikl['naslov']}"