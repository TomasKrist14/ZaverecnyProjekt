from Akce import Akce

x = True
pojistenci = []

while x:
    print("------------------------------\n"
          "Evidence pojištěných\n"
          "------------------------------")
    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = int(input())

    if volba == 1:
        a = Akce()
        pojistenci.append(a.pridatPojistenneho())

    elif volba == 2:
        Akce.vypsatPojistence(pojistenci)

    elif volba == 3:
        Akce.vyhledatPojistence(pojistenci)

    elif volba == 4:
        input("Data byla uložena, pokračujte libovolnou klávesou...")
        break













