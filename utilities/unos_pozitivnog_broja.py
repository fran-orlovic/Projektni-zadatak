from datetime import date


def unos_pozitivnog_cijelog_broja(poruka):
    while True:

        try:
            broj = int(input(f"{poruka} "))
            if broj < 0:
                raise Exception("Molim Vas unesite pozitivan cijeli broj!")

        except ValueError:
            print("Morate upisati cijeli broj!")

        except Exception as e:
            print(e)

        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):
    while True:

        try:
            broj = float(input(f"{poruka} "))
            if broj < 0:
                raise Exception("Molim Vas unesite pozitivan realan broj!")

        except ValueError:
            print("Morate upisati realan broj!")

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):
    print(f"{poruka} ")
    while True:
        try:
            dan = int(input("Unesite dan isteka prodaje: "))
            mjesec = int(input("Unesite mjesec isteka prodaje: "))
            godina = int(input("Unesite godinu isteka prodaje: "))

            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        else:
            return datum


def unos_emaila(poruka):
    while True:
        try:
            email = input(f"{poruka}")
            email.index('@')
        except ValueError:
            print("Molim Vas unesite email koji sadrži znak @")
        else:
            return email


def unos_intervala(x, y):
    while True:
        try:
            odabir = int(input(f"Unesite broj u intervalu {x}-{y}: "))
            if odabir < x or odabir > y:
                raise Exception("Molim Vas unesite broj unutar intervala!")
        except ValueError:
            print("Molim Vas unesite broj!")
        except Exception as e:
            print(e)
        else:
            return odabir
