# Engeto_Python_Election-scraper

Tento projekt slouží ke stahování výsledků z oficiálních stránek https://www.volby.cz/, konkrétně pro výsledky voleb do Poslanecké sněmovny Parlamentu ČR v roce 2017 https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ a ukládání výsledků do CSV souboru.

## Instalace

1. Naklonujte si repozitář nebo stáhněte soubory projektu.
2. Vytvořte a aktivujte si virtuální prostředí (doporučeno):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / MacOS
   venv\Scripts\activate      # Windows
3. Nainstalujte potřebné knihovny ze souboru requirements.txt:
   pip install -r requirements.txt

## Spuštění

Skript main.py se spouští z příkazové řádky se dvěma argumenty:

1. URL adresa územního celku ze stránek volby.cz

2. Název výstupního souboru CSV

## Ukázka použití

Například pro okres Prostějov:

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"

## Ukázka průběhu stahování (zkráceno):
Nalezeno 97 obcí. Zpracovávám...
-> Alojzov
-> Bedihošť
-> Bílovice-Lutotín
-> Biskupice

## Ukázka výstupu

Po spuštění se v adresáři vytvoří soubor vysledky_prostejov.csv, který obsahuje:
- kód obce
- název obce
- počet voličů v seznamu
- počet vydaných obálek
- počet platných hlasů
- a následně počty hlasů pro všechny kandidující strany

## Autor
Projekt vznikl v rámci studia na ENGETO Python Akademii.

## Ukázka výstupu (zkráceno):
kód obce,obec,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Česká pirátská strana,ANO 2011,…
506761,Alojzov,205,145,144,29,18,32,…
589268,Bedihošť,834,527,524,51,34,140,…
589276,Bílovice-Lutotín,431,279,275,13,30,83,…

