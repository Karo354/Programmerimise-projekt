def tervitus():
    print('''Teretulemast!
    Alustate müstilist mängu nimega "MustLoss".
    Selles mängus olete teadmata kuidas
    sattunud müstilisse maailma ja ärkate vangitornis.
    Teie eesmärk on lahendada mõistatused
    ja pääseda lossist välja.
    Aga olge hoiatatud,
    müstilises maailmas võib juhtuda müstilisi asju.''')

def õpetus():
    print('''
    Käsud:
        Liikumine - 'mine'
        Objektid - 'võta'
        ''')

seljakott = []

praegune_asukoht = "Lossi teisel korrusel"
toad = {"Lossi kolmandal korrusel": "magamistoas",
    "Lossi teisel korrusel": {'vasakule': "vannitoas", 'objekt': 'mopp'},
    "Lossi esimesel korrusel": "köögis"}

võtmise_sõnastik = ("võta", "haara", "kraba")
võetavad_objektid_toas = {"Lossi kolmandal korrusel": {"magamistoas": "raamat"},
    "Lossi teisel korrusel": {'vannitoas': 'mopp'}, "Lossi esimesel korrusel": {"köögis": 'nuga'}}

objektide_sõnastik = {'raamat': 'raamatu', 'mopp': 'mopi', 'nuga': 'noa'}

tervitus()
õpetus()

while True:
    liigutus = input(">")
    liigutus = liigutus.split(' ', 1)
    
    if liigutus[0] in võtmise_sõnastik :
        if liigutus[1] in toad[praegune_asukoht]['objekt']:
            print(f"Sa leidsid '{liigutus[1]}'")
            seljakott.append(liigutus[1])
            toad[praegune_asukoht]['objekt'] = ''
        else:
            print(f"Siin puudub {liigutus[1]}")
    
    if liigutus[0] == 'mine':
        if liigutus[1] in toad[praegune_asukoht]:
            praegune_asukoht = toad[praegune_asukoht][liigutus[1]]
            print("Oled nüüd", praegune_asukoht)
        else:
            print("Sa ei saa sinna minna")
