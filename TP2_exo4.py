BASE=4
nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
fromage=800
eau=2
ail=2
pain=400

quantitefromage=(fromage * nbConvives / BASE)
quantiteeau=(eau * nbConvives / BASE)
quantiteail=(ail * nbConvives / BASE)
quantitepain=(pain * nbConvives / BASE)

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut : \n -",quantitefromage, "gr de fromage \n -",quantiteeau, "dl d'eau \n -",quantiteail, "gousse(s) d'ail \n -",quantitepain, "gr de pain")