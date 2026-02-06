import httpx
from colorama import Fore, Style
import os

os.system('cls' if os.name == 'nt' else 'clear')

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
r = httpx.get(url)
lines = r.text.split('\n')

def dostupne_meny():
    seznam_kodu_men = []
    print("Dostupné měny:")
    for i in lines[2:]:
        if not i.strip():
            continue
        parts = i.split('|')
        seznam_kodu_men.append(parts[3])
    return seznam_kodu_men

def dostupne_meny_read_only():
    print("Dostupné měny:")
    for i in lines[2:]:
        if not i.strip():
            continue
        parts = i.split('|')
        print(f"{parts[3]} - {parts[0]}")
    
def najdi_menu(vybrana_mena):
    for i in lines:
        if vybrana_mena in i: 
            return i
    return None
def prevod_meny(castka, line_mena, pocet_desetinnych_mist, z_czk_nebo_do_czk):
    zakladni_castka_cizi_meny = float(line_mena.split('|')[2].replace(',', '.'))
    if z_czk_nebo_do_czk == 0:
        kurz = float(line_mena.split('|')[4].replace(',', '.'))
        prevod = float(castka / kurz) * zakladni_castka_cizi_meny
        return prevod.__round__(pocet_desetinnych_mist)
    elif z_czk_nebo_do_czk == 1:
        prevod = (float(line_mena.split('|')[4].replace(',', '.')) / zakladni_castka_cizi_meny) * castka
        return prevod.__round__(pocet_desetinnych_mist)

existujici_kody_men = dostupne_meny()

### Hlavní program ###
while True:
    vyber_typu_prevodu = input("Zadejte 0 pro převod z CZK do cizí měny, nebo 1 pro převod z cizí měny do CZK: ")
    if vyber_typu_prevodu == "0" or vyber_typu_prevodu == "1":
        break
    else:
        print(Fore.RED + "Neplatná volba. Zkuste to znovu." + Style.RESET_ALL)

if vyber_typu_prevodu == "0":
    while True:
        vyber_meny0 = input("Vyberte měnu pro převod z CZK (podle ISO 4217 standardu, 3 místný kód), pro zobrazení dostupných měn stiskněte Enter: ")
        konecna_mena0 = vyber_meny0.upper().strip()
        if konecna_mena0 == "":
            dostupne_meny_read_only()
        elif konecna_mena0 in existujici_kody_men:
            break
        else:
            print(Fore.RED + "Zadaná měna nebyla nalezena. Zkuste to znovu." + Style.RESET_ALL)

    line_mena = najdi_menu(konecna_mena0)
    while True:
        try:
            pocet_czk = float(input(f"Zadejte částku v CZK: "))
        except ValueError:
            print(Fore.RED + "Zadejte platné číslo." + Style.RESET_ALL)
            continue  

        if pocet_czk < 0:
            print(Fore.RED + "Částka nemůže být záporná." + Style.RESET_ALL)
        else:
            break

    prevod = prevod_meny(pocet_czk, line_mena, 2, 0)
    print(Fore.BLUE + f"{prevod} {konecna_mena0}" + Style.RESET_ALL)

elif vyber_typu_prevodu == "1":
    while True:
        vyber_meny1 = input("Vyberte měnu pro převod na CZK (podle ISO 4217 standardu, 3 místný kód), pro zobrazení dostupných měn stiskněte Enter: ")
        konecna_mena1 = vyber_meny1.upper().strip()
        if konecna_mena1 == "":
            dostupne_meny_read_only()
        elif konecna_mena1 in existujici_kody_men:
            break
        else:
            print(Fore.RED + "Zadaná měna nebyla nalezena. Zkuste to znovu." + Style.RESET_ALL)

    line_mena = najdi_menu(konecna_mena1)
    while True:
        try:
            pocet_cizi_meny = float(input(f"Zadejte částku v {konecna_mena1} pro převod do CZK: "))
        except ValueError:
            print(Fore.RED + "Zadejte platné číslo." + Style.RESET_ALL)
            continue

        if pocet_cizi_meny < 0:
                print(Fore.RED + "Částka nemůže být záporná." + Style.RESET_ALL)
        else:
            break
    prevod = prevod_meny(pocet_cizi_meny, line_mena, 2, 1)
    print(Fore.BLUE + str(prevod) + " Kč" + Style.RESET_ALL)
            