#juhuslikke täisarvude genereerimine
from random import randint
# küsime andmed
basseiniots_meetrites = int(input("Sisestage basseini pikkus meetrites:"))
#tekitan nimekirja
basseiniotsad = []
#tekitan suvaliselt 7 päeva basseiniotste arvud vahemikus 25-50 loendisse
for x in range(7):
    basseiniotsad.append(randint(25, 50))
#defineerin funktsiooni kalorite leidmiseks
def kalorid(basseiniotste_arv, basseini_pikkus):
    kalorite_arv = (basseiniotste_arv * basseini_pikkus / 1000) * 120
    return kalorite_arv
#arvutan palju iga päev kulutas ja kokku kulutas kaloreid
kaloreid_kokku = 0
for y in range(len(basseiniotsad)):
    kaloreid_paevas = round(kalorid(basseiniotsad[y], basseiniots_meetrites), 1)
    kaloreid_kokku += kaloreid_paevas
    print('Päevas kaotasid: ' + str(kaloreid_paevas) + ' kalorit')
print('Kokku kaotasid nädalas: ' + str(kaloreid_kokku) + ' kalorit')