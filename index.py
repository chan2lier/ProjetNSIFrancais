linkfichier= input(' Localisation du fichier')

with open(linkfichier,"r") as fichier:
    txt = fichier.read()

def nombre_occurence_mot(mot,texte):
    compteur=0
    m = len(mot) 
    for i in range(len(texte)-m):
        j = 0
        while j<m and mot[j] == texte[i+j].lower():
            j+=1
        if j==m:
            compteur +=1
    return compteur

#récupérer nombre de ligne
print(nombre_occurence_mot("\n",txt))
#nombre de caractéer
print(nombre_occurence_mot("",txt))