
class Vozilo:
    def __init__(self):
        pass

    @staticmethod
    def izracunaj_kw(konjske_snage):
        return konjske_snage * 0.745

    def cijena_osiguranja(self, konjske_snage):
        return self.izracunaj_kw(konjske_snage) * 15
