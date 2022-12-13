import re
from Pojistenec import Pojistenec

class Akce:

    def pridatPojistenneho(self):
        jmeno = input("Zadejte jméno pojištěnného:\n")
        prijmeni = input("Zadejte přijmení:\n")
        cislo = input("Zadejte telefonní číslo:\n")
        vek = input("Zadejte věk:\n")
        return Pojistenec(jmeno, prijmeni, cislo, vek)

    def vypsatPojistence(pojistenci):
        print("\n")
        for pojistenec in pojistenci:
            print(pojistenec)
        print("\n")

    def vyhledatPojistence(pojistenci):
        print("\n")
        jmeno = input("Zadejte jméno pojištěnného:\n")
        prijmeni = input("Zadejte přijmení:\n")
        for p in pojistenci:
            if re.search(jmeno, p.jmeno, re.IGNORECASE) and re.search(prijmeni, p.prijmeni, re.IGNORECASE):
                Akce.vypsatPojistence([p])



