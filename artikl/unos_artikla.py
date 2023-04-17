from utilities import unos_pozitivnog_realnog_broja


def unos_artikla(index):

    artikl = {}

    artikl['naslov'] = input(f"Unesite naslov {index}. artikla: ").capitalize()
    artikl['opis'] = input(f"Unesite opis {index}. artikla: ").capitalize()
    artikl['cijena'] = unos_pozitivnog_realnog_broja(f"Unesite cijenu {index}. artikla: ")

    return artikl
