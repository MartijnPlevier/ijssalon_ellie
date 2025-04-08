smaken = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = smaken["aardbei"]*0.8
#print(aanbieding)

reclame_tekst=f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
#print(reclame_tekst)

reclame_tekst2 = reclame_tekst[:63]
#print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2.upper()
#print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split()
#print(reclame_tekst4)


list = reclame_tekst4
#for el in list:
#    el = el.lower()
#    print(el)

for el in list:
    if len(el) >= 5:
        # Als het element 5 of meer tekens heeft, zet het om naar hoofdletters
        print(el.upper())
    else:
        # Als het element 4 of minder tekens heeft, zet het om naar kleine letters
        print(el.lower())