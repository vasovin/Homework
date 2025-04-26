import csv
import os

FILE_NAME = 'jizdni_kola.csv'

def nacti_data():
    """Načte data z CSV souboru a vrátí seznam kol."""
    kola = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                kola.append(row)
    return kola

def uloz_data(kola):
    """Uloží seznam kol do CSV souboru."""
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['znacka', 'typ']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for kolo in kola:
            writer.writerow(kolo)

def pridej_kolo(kola):
    """Přidá nové kolo do seznamu."""
    znacka = input("Zadejte značku kola: ")
    typ = input("Zadejte typ kola: ")
    kola.append({"znacka": znacka, "typ": typ})
    print("Kolo bylo přidáno.")

def zobraz_vsechna_kola(kola):
    """Zobrazí všechna kola."""
    if not kola:
        print("Seznam kol je prázdný.")
        return
    print(f"{'Index':<6} {'Značka':<15} {'Typ'}")
    for index, kolo in enumerate(kola):
        print(f"{index:<6} {kolo['znacka']:<15} {kolo['typ']}")

def vyhledej_kolo(kola):
    """Vyhledá kolo podle názvu značky."""
    hledana_znacka = input("Zadejte značku kola k vyhledání: ")
    nalezeno = False
    for index, kolo in enumerate(kola):
        if hledana_znacka.lower() in kolo['znacka'].lower():
            print(f"Nalezeno na indexu {index}: {kolo['znacka']} - {kolo['typ']}")
            nalezeno = True
    if not nalezeno:
        print("Kolo se zadanou značkou nebylo nalezeno.")

def odstranit_kolo(kola):
    """Odstraní kolo ze seznamu podle indexu."""
    if not kola:
        print("Seznam kol je prázdný.")
        return
    try:
        index = int(input("Zadejte index kola, které chcete smazat: "))
        if 0 <= index < len(kola):
            smazane = kola.pop(index)
            print(f"Kolo {smazane['znacka']} - {smazane['typ']} bylo odstraněno.")
        else:
            print("Neplatný index.")
    except ValueError:
        print("Zadejte prosím číselnou hodnotu.")

def main():
    kola = nacti_data()
    while True:
        print("\n--- Správa jízdních kol ---")
        print("1. Přidat nové kolo")
        print("2. Zobrazit všechna kola")
        print("3. Vyhledat kolo podle značky")
        print("4. Odstranit kolo")
        print("5. Ukončit program a ulozit zaznamy do souboru csv")
        volba = input("Vyberte volbu (1-5): ")

        if volba == "1":
            pridej_kolo(kola)
        elif volba == "2":
            zobraz_vsechna_kola(kola)
        elif volba == "3":
            vyhledej_kolo(kola)
        elif volba == "4":
            odstranit_kolo(kola)
        elif volba == "5":
            uloz_data(kola)
            print("Data o kolech byla ulozena. Konec")
            break
        else:
            print("Neplatna volba, zvolte jinou moznost")

if __name__ == "__main__":
    main()
