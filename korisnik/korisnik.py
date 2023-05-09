
class Korisnik:
    def __init__(self, ime, prezime, email, telefon, zdravstvena):
        self.__ime = ime
        self.__prezime = prezime
        self.__email = email
        self.__telefon = telefon
        self.zdravstvena = zdravstvena

    def ispis(self):
        print("Infromacije o korisniku:")
        print(f"\tIme: {self.ime}")
        print(f"\tPrezime: {self.prezime}")
        print(f"\tTelefon: {self.telefon}")
        print(f"\tEmail: {self.email}")
        print("Infromacije o zdravstvenoj:")
        self.zdravstvena.ispis()

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def email(self):
        return self.__email

    @property
    def telefon(self):
        return self.__telefon
