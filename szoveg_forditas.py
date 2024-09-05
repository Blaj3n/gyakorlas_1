# Feladat leírása: Írj egy programot, amely bekér egy sztringet a felhasználótól, majd kiírja a sztringet visszafelé.
#
# Példa bemenet:
#
# Adjon meg egy sztringet: alma
#
# Példa kimenet:
#
# Visszafelé: amla

szoveg = input("Adjon meg egy sztringet: ")

forditott_szoveg = ""  # fordított karakterek tárolása

for karakter in szoveg:
    forditott_szoveg = karakter + forditott_szoveg
print(f"Visszafelé: {forditott_szoveg}")

# A helyes megközelítés az lenne, ha a forditott_szoveg változót minden iterációban frissítenéd úgy, hogy hozzáadod a karaktert az elejére. A print helyett az új sztring forditott_szoveg változót szeretnéd frissíteni, és végül ezt kiírni.

# Magyarázat:
# 1. forditott_szoveg: Kezdetben üres sztring.
# 2. for karakter in szoveg: Iterál az összes karakteren.
# 3. forditott_szoveg = karakter + forditott_szoveg: Minden iterációban az aktuális karaktert hozzáadod a forditott_szoveg elejére, így a karakterek visszafelé épülnek.
# 4. print(f"Fordított sztring: {forditott_szoveg}"): A végén kiírod a visszafelé épített sztringet.