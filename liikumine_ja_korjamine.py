# Esialgne liikumise ja esemete üles korjamise programm
seljakott = []
praegune_asukoht = "Lossi kolmandal korrusel koridoris"

def õpetus():
    print("KÄSUD: ")
    print("Kui tahad eset võtta kirjuta kas 'võta ...', 'haara ...' või 'kraba ...', asendades '...' valitud esemega.")
    print("Kui soovid liikuda kirjuta 'mine ...' või 'pööra ...' asendades '...' valitud suunaga.")
    print("Käsk 'seljakott' näitab sulle su seljakoti sisu.")
    print("Käsk 'välju' lõpetab mängu.")

toad = {"Lossi kolmandal korrusel koridoris": {
    "suunad": {
        "alla": "Lossi teisel korrusel koridoris",
        "vasakule": "Suures toas"},
    "objekt": "raamat",
    "kirje": "Siit saad minna 'alla' või 'vasakule'. Siin on 'raamat'."},
    "Lossi teisel korrusel koridoris": {
        "suunad": {
            "üles": "Lossi kolmandal korrusel koridoris",
            "alla": "Lossi esimesel korrusel koridoris"},
        "objekt": "küünal",
        "kirje": "Siit saad minna 'alla' või 'üles'. Siin on 'küünal'."},
    "Lossi esimesel korrusel koridoris": {
        "suunad": {
            "üles": "Lossi teisel korrusel koridoris",
            "lõppu": "Väljapääsu juures"
            },
        "objekt": "võti",
        "kirje": "Siit saad minna koridori lõppu käsuga 'lõppu' või tagasi üles käsuga 'üles'. Siin on 'võti'."},
    "Suures toas": {
        "suunad": {"tagasi": "Lossi kolmandal korrusel koridoris"},
        "kirje": "See on tühi tuba, saad tagasi minna käsuga 'mine tagasi'."},
    "Väljapääsu juures": {
        "suunad": {"tagasi": "Lossi esimesel korrusel koridoris"},
        "kirje": "Uks on lukus ja võti ei tööta. Saad minna tagasi käsuga 'mine tagasi'."}
        }

õpetus()
print()

print("Oled", praegune_asukoht)
print(toad[praegune_asukoht]['kirje'])

võtmise_sõnastik = ("võta", "haara", "kraba")
liikumise_sõnastik = ("mine", "pööra")

objektide_sõnastik = {'raamat': 'raamatu', 'küünal': 'küünla', 'võti': 'võtme'}

while True:
    sisend = input("> ").lower()
    if not sisend:
        continue
    
    liigutus = sisend.split(' ', 1)
    käsk = liigutus[0].lower()

# Esemete üleskorjamine
    if käsk in võtmise_sõnastik :
        if len(liigutus) > 1:
            soovitud_ese = liigutus[1]
            if toad[praegune_asukoht].get("objekt") == soovitud_ese:
                if soovitud_ese in objektide_sõnastik:
                    print(f"Sa leidsid '{objektide_sõnastik[soovitud_ese]}'!")
                    seljakott.append(soovitud_ese)
                    toad[praegune_asukoht]['objekt'] = None
            else:
                print(f"Eset '{soovitud_ese}' pole siin.")
        else:
            print("Mida soovid võtta?")
# Liikumine tubade vahel        
    elif käsk in liikumise_sõnastik:
        if len(liigutus) > 1:
            suund = liigutus[1]
            if suund in toad[praegune_asukoht]["suunad"]:
                praegune_asukoht = toad[praegune_asukoht]["suunad"][suund]
                print("Oled nüüd", praegune_asukoht)
                print(toad[praegune_asukoht]["kirje"])
            else:
                print("Sa ei saa sinna minna")
        else:
            print("Kuhu sa minna soovid?")
            
    elif käsk == "seljakott":
        if seljakott:
            print(f"Sinu seljakotis on: {seljakott}")
        else:
            print(f"Sinu seljakott on tühi.")
    
    elif käsk == 'välju':
        print("Head aega!")
        break
    
    else:
        print("Tundmatu käsk. Proovi midagi muud.")
