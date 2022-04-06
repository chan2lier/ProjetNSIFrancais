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

def lister_tous_mots(fichier):
    symboles_indésirables = ['""','-',';',':']

#récupérer nombre de ligne
print("Nombre de lignes = ",nombre_occurence_mot("\n",txt))
#nombre de caractère
print("Nombre de caractères = ",nombre_occurence_mot("",txt))
#nombre de passage de ligne
print("Nombre de sauts de lignes = ",nombre_occurence_mot("\n\n",txt))
#nombre de Tiret
print("Nombre de tirets = ",nombre_occurence_mot('"',txt))
#nombre de mot
print(len(txt.split()))



théâtre = ["scène","acte","-","prologue","épilogue","“”"]
animaux = ["renard","corbeau","loutre","lion","cheval", "poisson","mouche","abeille","chien", "chat","tortue","loup","cygogne","rat","souris","lapin","pigeon","crevette"]

def line(fichier)->str
    pass

def liste_tous_mots(fichier)->list of str:
    pass

def liste_mots_importants(fichier,exceptions)-> list of str:
    pass

def occurences_mots(fichier,exceptions)->dico:
    pass

def nombre_lignes(texte):
    pass

def nombre_mots(texte):
    pass

def liste_mots_rangés(?):
    pass

def liste_mots_principaux(?):
    pass

def liste_noms_principaux(?):
    pass