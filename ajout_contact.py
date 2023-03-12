def ajout_contact(email,mail):
#fonction permettant de rajouter un contact dans l’annuaire par l’utilisateur
#le mail est l'email recherché du contact à rajouter et l'email est l'email de l'utilisateur connecté
    g=open("annuaire",'r+')
    f=open('annuaire_de {}'.format (email), 'a')
    #on va rajouter le nouveau contact à l'annuaire de l'utilisateur
    for ligne in g:
        #recherche du contact à rajouter dans l'annuaire
        infos=g.readlines()
        for i in infos:
            info=i.split(';')
            #on sépare les éléments de chaque ligne pour pouvoir comparer les mails de chaque contact
            if info[2].lower()==mail.lower():
                print ("true")
                #on rajoute le contact si le mail correspond bien à celui recherché
                f.write('\n'+i)
                f.close()
    g.close()



#main
#appel à la fonction
mail=input("donner l'email de l'utilisateur recherché")
email=input("donner votre email")
ajout_contact(email,mail)
