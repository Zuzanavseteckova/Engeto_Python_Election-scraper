"""
main.py: třetí projekt do Engeto Online Python Akademie
author: Zuzana Všetečková
email: zuzanacervenkova@seznam.cz
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv


# Funkce pro načtení HTML

def nacti_html(url):
    r = requests.get(url)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


# Funkce pro získání obcí

def ziskej_obce_a_odkazy(soup):
    obce = []
    for td in soup.find_all("td", {"class": "cislo"}):
        a = td.find("a")
        if a and "href" in a.attrs:
            kod_obce = a.text.strip()
            odkaz = "https://www.volby.cz/pls/ps2017nss/" + a["href"]
            # název obce je ve vedlejším <td>
            nazev = td.find_next("td").text.strip()
            obce.append((kod_obce, nazev, odkaz))
    return obce


# Funkce pro získání výsledků obce

def zpracuj_obec(kod, nazev, url):
    soup = nacti_html(url)

    # Voliči, obálky, platné hlasy
    volici = soup.find("td", headers="sa2").text.strip().replace("\xa0", "")
    obalky = soup.find("td", headers="sa3").text.strip().replace("\xa0", "")
    platne = soup.find("td", headers="sa6").text.strip().replace("\xa0", "")

    # Hlasy pro strany
    strany = {}

    # tabulka 1
    for tr in soup.find_all("tr"):
        td_jmeno = tr.find("td", {"headers": "t1sa1 t1sb2"})
        td_hlasy = tr.find("td", {"headers": "t1sa2 t1sb3"})
        if td_jmeno and td_hlasy:
            jmeno_strany = td_jmeno.text.strip()
            hlasy = td_hlasy.text.strip().replace("\xa0", "")
            strany[jmeno_strany] = hlasy

    # tabulka 2
    for tr in soup.find_all("tr"):
        td_jmeno = tr.find("td", {"headers": "t2sa1 t2sb2"})
        td_hlasy = tr.find("td", {"headers": "t2sa2 t2sb3"})
        if td_jmeno and td_hlasy:
            jmeno_strany = td_jmeno.text.strip()
            hlasy = td_hlasy.text.strip().replace("\xa0", "")
            strany[jmeno_strany] = hlasy

    return {
        "kód obce": kod,
        "obec": nazev,
        "voliči v seznamu": volici,
        "vydané obálky": obalky,
        "platné hlasy": platne,
        **strany
    }

# Funkce pro uložení CSV

def uloz_do_csv(vysledky, nazev_souboru):
    if not vysledky:
        print("Žádná data k uložení.")
        return

    # všechny sloupce (hlavičky)
    hlavicky = vysledky[0].keys()

    with open(nazev_souboru, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=hlavicky, delimiter=",")
        writer.writeheader()
        for radek in vysledky:
            writer.writerow(radek)

    print(f"Výsledky uloženy do {nazev_souboru}")


# Hlavní část

def main():
    if len(sys.argv) != 3:
        print("Chyba: Zadejte URL územního celku a název výstupního souboru.")
        print("Příklad spuštění: python main.py <URL> <vystup.csv>")
        sys.exit(1)

    vstup_url = sys.argv[1]
    vystup_csv = sys.argv[2]

    soup = nacti_html(vstup_url)
    obce = ziskej_obce_a_odkazy(soup)

    print(f"Nalezeno {len(obce)} obcí. Zpracovávám...")

    vysledky = []
    for kod, nazev, odkaz in obce:
        print(f"-> {nazev}")
        data = zpracuj_obec(kod, nazev, odkaz)
        vysledky.append(data)

    uloz_do_csv(vysledky, vystup_csv)

if __name__ == "__main__":
    main()




