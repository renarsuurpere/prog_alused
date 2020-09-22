# kasutaja andmed
inimesed = int(input("Sisestage inimeste arv: "))
kohad = int(input("Sisestage kohtade arv: "))
bussid = int(input("Sisestage busside arv: "))
kohadKokku = kohad * bussid
# arvutus
mahutavus = min(inimesed, kohadKokku)
jääk = inimesed - mahutavus #suurema arvudega (800 inimest, 40 kohta ja 5 bussi) jäägiga jagamine ei anna õiget tulemit
# väljastus
print("Kokku ootas bussi " + str(inimesed) + " inimest." " Peatusesse tuli " + str(bussid) + " bussi, igas bussis " + str(kohad) + " kohta. " "Kõikidesse bussidesse mahtus " + str(mahutavus) + " inimest." " Bussist jäi maha " + str(jääk) + " inimest.")
