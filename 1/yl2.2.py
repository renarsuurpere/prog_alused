nimi = str(input("Sisestage nimi:"))

if nimi[-2:] == "ne":
    print("Abielus")
elif nimi[-2:] == "te":
    print("Vallaline")
elif nimi[-1:] == "e":
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")

