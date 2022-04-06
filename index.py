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
#nombre de caractère
print(nombre_occurence_mot("",txt))
#nombre de passage de ligne
print(nombre_occurence_mot("\n\n",txt))
#nombre de Tiret
print(nombre_occurence_mot('"',txt))
print("Nombre de ligne = ",nombre_occurence_mot("\n",txt))
#nombre de caractère
print("Nombre de caractère = ",nombre_occurence_mot("",txt))
#nombre de passage de ligne
print("Nombre de saut de ligne = ",nombre_occurence_mot("\n\n",txt))
#nombre de Tiret
print("Nombre de tiret = ",nombre_occurence_mot('"',txt))




animaux = ["renard","corbeau","loutre","lion","cheval", "poisson","mouche","abeille","chien", "chat","tortue","loup","cygogne","rat","souris","lapin","pigeon","crevette"]