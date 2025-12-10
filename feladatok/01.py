"""Írj egy programot, amely a felhasználótól bekéri egy kutya nevét,
életkorát, fajtáját, és azt hogy rendelkezik-e érvényes oltással veszettség ellen! 
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!
"""

nev = input("enter the dog's name \n")
kor = input("enter the dog's age \n")
fajta = input("enter the dog's species \n")
oltas_valasz = input("is the dog vaccined for rabies \n")
oltas = oltas_valasz == "i" or oltas_valasz == "igen"

kutya = {}

kutya["nev"] = nev
kutya["kor"] = kor
kutya["fajta"] = fajta
kutya["oltas"] = oltas

for kulcs, ertek in kutya.items():
    print(f"{kulcs} {ertek}")