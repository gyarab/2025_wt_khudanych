import httpx
from colorama import Fore, Style

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
r = httpx.get(url)
lines = r.text.split('\n')

vyber_meny = input("Vyberte měnu pro převod na CZK (podle ISO 4217 standardu, 3 místný kód), pro zobrazení dostupných měn stiskněte Enter: ")
if vyber_meny == "":
    print("Dostupné měny:")
    for i in lines[2:]:
        if i.strip() == "":
            continue
        parts = i.split('|')
        print(f"{parts[3]} ({parts[0]})")
    vyber_meny = input("Zadejte kód měny pro převod na CZK: ")
vybrana_mena = vyber_meny.upper()
line_mena = ""

for i in lines:
    if vybrana_mena in i: 
        parts = i.split('|')  
        line_mena = i
        break

castka = float(input(f"Zadejte částku v {vybrana_mena} pro převod na CZK: "))
castka_vybrane_meny = float(line_mena.split('|')[2].replace(',', '.'))
prevod = float(line_mena.split('|')[4].replace(',', '.')) / castka_vybrane_meny * castka
POCET_DESETINNYCH_MIST = 2
print(Fore.BLUE + str(prevod.__round__(POCET_DESETINNYCH_MIST)) + " CZK" + Style.RESET_ALL)