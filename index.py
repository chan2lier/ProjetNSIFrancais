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
    
def mots_importants(fichier):
    liste_mots = []
    for mot in range(len(txt.split())):
        liste_mots.append(mot)
    print (liste_mots[mot])

mots_importants(fichier)

#récupérer nombre de ligne
print("Nombre de ligne = ",nombre_occurence_mot("\n",txt))
#nombre de caractère
print("Nombre de caractère = ",nombre_occurence_mot("",txt))
#nombre de passage de ligne
print("Nombre de saut de ligne = ",nombre_occurence_mot("\n\n",txt))
#nombre de Tiret
print("Nombre de tiret = ",nombre_occurence_mot('"',txt))
#nombre de mot
print("Nombre de mot = ",len(txt.split()))

animaux = ["renard","corbeau","loutre","lion","cheval", "poisson","mouche","abeille","chien", "chat","tortue","loup","cygogne","rat","souris","lapin","pigeon","crevette"]

def test(fichier, liste):
    i=0
    while i<len(liste):
        if fichier.count(liste[i])>=1:
            print(liste[i], ':', fichier.count(liste[i]) )
        i+=1

test(txt, animaux)