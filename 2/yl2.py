ringide_arv = int(input("Sisestage ringide arv: "))
ringi_nr = 1
porgandite_arv = 0
while(ringi_nr <= ringide_arv):
  #  print(ringi_nr)
  # paarisarvu juures annab porgandeid
    if(ringi_nr % 2 == 0):
        #mitu porgandit paarisarv ringi juures annab
        porgandite_arv = porgandite_arv + ringi_nr
     #   print("said " + str(ringi_nr) + " porgandid")
     #   print("Kokku on hetkel " + str(porgandite_arv) + " porgandit.")
    ringi_nr += 1
print("Porgandite koguarv " + str(porgandite_arv))