def test(fichier):
    i=0
    while i<len(animaux):
        print(fichier.count(animaux[i], animaux[i])) 