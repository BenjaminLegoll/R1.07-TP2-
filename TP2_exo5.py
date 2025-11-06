nombre=int(input("Entrez un nombre :"))

if nombre == 0:
    print("Le nombre est zéro (et il est pair)")
elif nombre%2==0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")