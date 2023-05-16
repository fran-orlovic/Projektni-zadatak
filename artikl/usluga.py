from abc import ABC, abstractmethod


class Usluga(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def cijena_po_satu(self):
        pass
