# juhuslike täisarvude genereerimine
from random import randint
# defineerime andmeid
sammud = [9366, 11421, 11426, 14903, 7169, 7529, 10612]
# küsime andmeid
sammu_pikkus_meetrites = float(input("Sisestage oma sammu pikkus meetrites:"))
# genereerime nädalapäevadeks tekitatud sammud juhuarvuna
tekitatud_samme = randint(5000, 15000)
# lisame need sammude nimekirja
sammud.append(tekitatud_samme)
# leiame sammud kilomeetrites
kilomeetrite_arv = (sammud * sammu_pikkus_meetrites)/ 1000
print(*kilomeetrite_arv, sep = "\n")

'''
# väljastame üks haaval
print (*sammud, sep = "\n")
'''