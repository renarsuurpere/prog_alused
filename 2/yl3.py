#juhuslikke täisarvude genereerimine
from random import randint
# sisestame soovitud täringute arv
soovitud_kord = int(input("Sisestage täringu visete arv: "))
# viskame täringut nii kaua, soovitud arv viske on tehtud
# paneme korrad lugema
kord = 1
while(kord <= soovitud_kord):
    #teeme viske
    taring = randint(1, 6)
#kontrollime palju tuli
    print(taring)
#liigume järgmisele viskele
    kord += 1
