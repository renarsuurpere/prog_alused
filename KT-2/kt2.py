#juhuslikke täisarvude genereerimine
from random import randint
# küsime andmed
koneminut = float(input("Sisestage kõneminuti hind:"))
koned = int(input("Sisestage kõnede koguarv:"))
#leiame suvalise kestvuse
kestvus = randint(1, 1000)
#arvutame maksumused
if kestvus > 610:
    kone_maksumus = 10 * koneminut
elif kestvus > 210:
    kone_maksumus = (koneminut / 60) * kestvus
elif kestvus > 30:
    kone_maksumus = 1 * koneminut
#mitu korda väljastada
for koned in range(1, koned +1):
    print("Kõne maksumus: " + str(kone_maksumus))


# ei oska panna et ta "koned" korda võtaks erinevalt, hetkel võtab "koned" korda ühte sama koned_maksumus