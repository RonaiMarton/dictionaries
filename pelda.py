ures_szotar = {}

szemely = {
    "nev": "Kis Ferenc",
    "kor": 25,
    "varos": "Budapest"
}

print(szemely["nev"])
print(szemely["kor"])
print(szemely["varos"])



# print(szemely["telefon"])
print(szemely.get("telefon", "Nincs a szótárban ez a kulcs!"))


#érték megváltoztatása
szemely["kor"] = 26
print(szemely["kor"])


#kulcs-érték pár törlése
del szemely["varos"]
print(szemely.get("varos", "Nincs a szótárban ez a kulcs"))


#kulcs-érték pár hozzáadása
szemely["neme"] = "férfi"
print(szemely["neme"])


#in operator
if "nev" in szemely:
    print("A keresett kulcs megtalálható a szótárban")

if "bankszamla" not in szemely:
    print("A keresett kulcs nem található")


#az összes kulcs-érték pár elérése
for kulcs, ertek in szemely.items():
    print(f"{kulcs} {ertek}")