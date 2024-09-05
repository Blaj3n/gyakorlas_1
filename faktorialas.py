# Feladat leírása:  Készíts egy programot, amely bekér egy nem negatív egész számot a felhasználótól,
# és kiszámítja a szám faktoriálisát. A faktoriális n!, ahol n! = n × (n - 1) × (n - 2) × ... × 1, és 0! = 1.
#
# Példa bemenet:
#
# Adjon meg egy nem negatív egész számot: 5
#
# Példa kimenet:
#
# 5! = 120

szam = int(input("Adjon meg egy nem negatív egész számot: "))

fakt_szamok_osszege = 1

for i in range(1, szam+1):
    fakt_szamok_osszege *= i
print(f"{szam}! = {fakt_szamok_osszege}")

# HIBA MAGYARÁZATA
# 1. Hibás Szorzási Módszer:
#
# A kódodban a faktoriális kiszámításához a következő kifejezést használtad: fakt_szamok_osszege += fakt_szamok_osszege * i.
# Itt a += operátort használod, ami azt jelenti, hogy minden iterációban hozzáadod a fakt_szamok_osszege * i értéket a meglévő fakt_szamok_osszege értékhez.
# Ez nem faktoriálist számít, hanem egy sorozatos hozzáadást, ami nem adja a kívánt eredményt.

# 2. Javítás:
#
# A helyes módszer a faktoriális kiszámításához, ha minden iterációban szorozzuk a fakt_szamok_osszege értékét az aktuális i értékkel.
# fakt_szamok_osszege *= i
# Ezzel minden iterációban szorzunk a faktoriálison, nem hozzáadjuk az új értéket.