"""Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút). 
A program a írja ki a képernyőre az adatszerkezet! 
A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie. 
A program végül írja ki a képernyőre a frissített adatszerkezetet!"""

szotar = {
    "szam": 4,
    "str": "alma",
    "bool": True
}

for kulcs, ertek in szotar.items():
    print(f"{kulcs} {ertek}")

key = input("adja meg, hogy milyen kulcsot ad meg (str) \n")
value = input("adja meg, hogy milyen erteket ad meg \n")
szotar[key] = value

for kulcs, ertek in szotar.items():
    print(f"{kulcs} {ertek}")