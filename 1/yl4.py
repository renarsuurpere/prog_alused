# kasutaja andmed
nimi = input("Sisesta oma nimi: ")
lubatudKiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelikKiirus = int(input("Sisestage tegelik kiirus (km/h): "))
# arvutus
trahv = (tegelikKiirus - lubatudKiirus) * 3
# arvestame, max 190
trahv = min(trahv, 190)
# väljastus
print(nimi + ", kiiruse ületamise eest on Teie trahv " + str(trahv) + " eurot.")
