# kasutaja andmed
ainepunktid = int(input("Sisestage ainepunktide arv: "))
nädalad = int(input("Sisestage nädalate arv: "))
ajakulu = 26
# arvutus
vastus = (ainepunktid * ajakulu) / nädalad
# väljastus
print("Nädala ajakulu " + str(round(vastus)) + " tundi." )