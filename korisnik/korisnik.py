from abc import ABC
from abc import abstractmethod


class Korisnik(ABC):
    def __init__(self, email, telefon):
        self.__email = email
        self.__telefon = telefon

    @property
    def email(self):
        return self.__email

    @property
    def telefon(self):
        return self.__telefon

    @abstractmethod
    def ispis(self):
        pass
