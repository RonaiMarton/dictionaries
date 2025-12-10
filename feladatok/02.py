"""Írj egy programot, amely szótárban tárolja egy macska nevét, korát. 
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot. 
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa, 
végül írja ki a képernyőre a frissített adatszerkezetet!"""

macska = {
    "nev": "Cirmi",
    "kor": 4
}
kor_vagy_nev = input("adja meg, hogy a nevét vagy a korát változtatja meg (k/n) \n")
if kor_vagy_nev == "k":
    macska["kor"] = input("adja meg a macska korát \n")
elif kor_vagy_nev == "n":
    macska["nev"] = input("adja meg a macska nevét \n")
else:
    print("rossz értéket adott meg")

for kulcs, ertek in macska.items():
    print(f"{kulcs} {ertek}")