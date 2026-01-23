import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
r = httpx.get(url)
lines = r.text.split('\n')

# Přeskočíme první 2 řádky (datum a hlavičku) a jdeme rovnou na data
for i in lines[2:]:
    if i:  # Kontrola, zda řádek není prázdný (na konci souboru bývá prázdný řádek)
        parts = i.split('|')  
        print(parts[0], parts[3], parts[4] + " CZK")