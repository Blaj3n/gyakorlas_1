# Feladat leírása: Írj egy programot, amely a felhasználótól bekér egy pozitív egész számot, majd kiszámolja és
# kiírja a következőket:
#
# Az 1 és a megadott szám közötti páros számok összegét.
# Az 1 és a megadott szám közötti páratlan számok összegét.
# Példa bemenet:
#
# Adjon meg egy pozitív egész számot: 10
#
# Példa kimenet:
#
# Páros számok összege: 30
# Páratlan számok összege: 25

szam = int(input("Adjon meg egy pozitív egész számot: "))

paros_szamok_osszege = 0
paratlan_szamok_osszege = 0

for i in range(1, szam+1):  # Számot is beleértjük
    if i % 2 == 0:
        paros_szamok_osszege += i
    else:
        paratlan_szamok_osszege += i

print(f"Páros számok összege: {paros_szamok_osszege}")
print(f"Páratlan számok összege: {paratlan_szamok_osszege}")

# HIBA MAGYARÁZATA
# EREDETI CIKLUS    for i in range(1, szam):
# A range(1, szam) egy olyan intervallumot hoz létre, amely az 1-től indul,
# de nem tartalmazza a szam értékét, tehát a ciklus az 1-től a szam - 1-ig terjed.
#
# Például, ha szam = 10, akkor a range(1, 10) a következő számokat adja: 1, 2, 3, 4, 5, 6, 7, 8, 9.
# A 10-et nem tartalmazza, mert a range utolsó értékét nem veszi bele.

# Összefoglalva:
# Eredeti ciklus: range(1, szam) -> nem tartalmazza szam-ot, csak szam - 1-ig megy.
# Javított ciklus: range(1, szam + 1) -> tartalmazza szam-ot is, így a helyes eredményt adja.
