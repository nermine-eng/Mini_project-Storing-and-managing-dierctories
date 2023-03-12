def creer_compte():
    #l'objectif de cette fonction est de créer le compte de l'utilisateur
        nom = ""
        prenom = ""
        email = ""
        while (nom == "") or (prenom == "") or (email == ""):
            #le nom, prenom et email sont des champs obligatoires qu'il faut les remplir
            nom = input("donner le nom de l'utilisateur")
            print(nom)
            prenom = input("donner le prenom de l'utilisateur")
            print(prenom)
            email = input("donner l'email de l'utilisateur")
            print(email)
            numero = int(input("donner le numéro de telephone de l'utilisateur"))
            print(numero)
            adresse = int(input("donner l'adresse postale de l'utilisateur"))
            print(adresse)
            ligne = (nom + ';' + prenom + ';' + email + ';' + str(numero) + ';' + str(adresse))
            f = open('annuaire_de {}'.format (email), 'a')
            #on crée un annuaire pour chaque utilisateur
            f.write(ligne)
            print()
            f.close
            #on va creer aussi un fichier annuaire où on met tous ces comptes
            g=open("annuaire" , 'a')
            #Le fichier annuaire contiendra tous les comptes crées
            #chaque ligne présente un compte d'utilisateur
            g.write('\n'+ligne)
            g.close



#main
creer_compte()
#appel à la fonction




