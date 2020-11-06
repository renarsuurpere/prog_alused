# juhuslike täisarvude genereerimine
from random import randint
# küsime andmeid
sammu_pikkus_meetrites = float(input("Sisestage oma sammu pikkus meetrites:"))
# defineerime andmeid
sammud = [9366, 11421, 11426, 14903, 7169, 7529, 10612]
# genereerime nädalapäevadeks tekitatud sammud juhuarvuna
tekitatud_samme = randint(5000, 15000)
# lisame need sammude nimekirja
sammud.append(tekitatud_samme)
# väljastame üks haaval
sammude_arv = []
for sammude_arv in sammud:
    print("Sammude arv: " + str(sammude_arv))
# arvutame kilomeetriteks
kilomeetrite_arv = (sammude_arv * sammu_pikkus_meetrites)/ 1000
print("Kilomeetrite arv: " + str(round(kilomeetrite_arv,2)) + "km")
#hetkel saan vaid viimase randint-ga listatud km, otsin kuidas kõik saada