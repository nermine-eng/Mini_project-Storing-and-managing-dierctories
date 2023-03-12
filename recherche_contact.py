
def recherche_contact(mail,email):
#fonction permettant de rechercher un contact dans un annuaire d’un utilisateur
    if (len(mail)==0):
        print("le champ est vide")
        return 1
    else:
        f=open ('annuaire_de {}'.format (email), 'r')
        for ligne in f:
            infos=f.readlines()
            print(infos)
            for i in infos:
                info = i.split(';')
                #on sépare les élements de chaque ligne du fichier
                print(info)
                if info[2].lower() == mail.lower():
                    #on affiche les 3 champs obligatoires du contact recherché
                    print( "Nom : " , info[0],"; Prenom : ", info[1],"; Email : ",info[2])




#main
#appel à la fonction
mail=input("donner l'email de la personne cherchée")
email=input("donner votre email")
recherche_contact(mail,email)
