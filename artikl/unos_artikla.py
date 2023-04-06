

def unos_artikla(index):

    artikl = {}

    artikl['naslov'] = input(f"Unesite naslov {index}. artikla: ").capitalize()
    artikl['opis'] = input(f"Unesite opis {index}. artikla: ").capitalize()
    artikl['cijena'] = float(input(f"Unesite cijenu {index}. artikla: "))

    return artikl
