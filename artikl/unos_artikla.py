from utilities import unos_pozitivnog_realnog_broja
from utilities import unos_pozitivnog_cijelog_broja
from utilities import unos_intervala
from .automobil import Automobil
from .stan import Stan
# from .instrukcije import Instrukcije
from .tip_artikla import TipArtikla


def unos_artikla(index):

    naslov = input(f"Unesite naslov {index}. artikla: ").capitalize()
    opis = input(f"Unesite opis {index}. artikla: ").capitalize()
    cijena = unos_pozitivnog_realnog_broja(f"Unesite cijenu {index}. artikla: ")

    print("Tipovi artikla")
    for i, tip_artikla in enumerate(TipArtikla, start=1):
        print(f"\t{i}. {tip_artikla.value}")

    odabir_tipa = unos_intervala(1, len(TipArtikla))
    if odabir_tipa == 2:
        kvadratura = unos_pozitivnog_realnog_broja(f"Unesite kvadraturu {index}. stana: ")
        artikl = Stan(naslov, opis, cijena, kvadratura)
    else:
        snaga = unos_pozitivnog_cijelog_broja(f"Unesite snagu {index}. automobila: ")
        artikl = Automobil(naslov, opis, cijena, snaga)
    # else:
        # artikl = Instrukcije(naslov, opis, cijena)

    return artikl
