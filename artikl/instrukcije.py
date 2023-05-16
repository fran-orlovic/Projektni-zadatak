from .artikl import Artikl
from .usluga import Usluga


class Instrukcije(Artikl, Usluga):
    def __init__(self, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)

    def cijena_po_satu(self):
        return float(self.cijena/30)

    def ispis(self):
        print(f"Informacije o instrukcijama:")
        print(f"\tNaslov: {self.naslov}")
        print(f"\tOpis: {self.opis}")
        print(f"\tCijena: {self.cijena}")
        print(f"\tCijena po satu: {self.cijena_po_satu()}")
