from api.document import Document
from api.pret import Pret
from api.film import filme
def main():
    print(""" 
    Bienvenu(e) au Menu:
    \n 1-Gestion des articles
    \n 2-Gestion des prets
    \n 00-Quitter
    """)
    choix = int(input("Votre choix :"))

    while choix != 0:
        if choix == 1 :
            doc()
            choix=9
        elif choix == 2 :
            pret()
            choix=9
        else:
            print("Choix invalide. Veuillez réessayer.")
            print(""" 
            Bienvenu(e) au Menu:
            \n 1-Gestion des articles
            \n 2-Gestion des prets
            \n 0-Quitter
            """)
        choix = int(input("Votre choix :"))
    print('Merci ("_")')
    
    
def doc():
    print("""  
            ---------------------------
            Menu - Gestion des articles:
            ----------------------------
        """)
    print("""
        \n 1-Afficher la liste des articles
        \n 2-Ajouter un articles
        \n 3-Mettre à jour un articles
        \n 4-Supprimer un articles
        \n 5-Retour au menu principal
        \n 0-Quitter
        """)
    choix = int(input("Votre choix : "))
    while choix != 0:
        if choix == 1:
            print("""
                \n 1-Afficher la liste des livre
                \n 2-Afficher la liste des film
                  """)
            choi = int(input("Votre choix : "))
            if choi ==1 :
                livre = Document()
                livre.liste_doc(table="livre")
            if choi ==2 :
                film = filme()
                # film.liste_doc(table="film")
                film.liste_doc(table="film")
                
        elif choix == 2:
            print("""
                \n 1-Ajouter un livre
                \n 2-Ajouter un film
                  """)
            choi = int(input("Votre choix : "))
            if choi ==1 :
                Titre = input("Entrez le nom du livre :")
                description = input("Entrez la description :")
                auteur = input("Entrez le nom de l'auteur :")
                date_parution = input("Entrez la date de parution :")
                ref_livre = int(input("Entrez la ref du livre 5 chiffre svp :"))
                maison_edition = input("Entrez le nom de la maison d'edition :")
                livre = Document()
                request = """insert into livre
                 (Titre,description,auteur,date_parution,ref_livre,maison_edition)
                 values (%s, %s, %s, %s, %s, %s)"""
                params = (Titre,description,auteur,date_parution,ref_livre,maison_edition)
                livre.insert_doc(request=request,params=params)
                print("Enregistrement effectuer...")
            if choi == 2 :
                Titre = input("Entrez le nom du film :")
                description = input("Entrez la description :")
                realisateur = input("Entrez le nom du realisateur :")
                annee_sortie = input("Entrez la date de sortie :")
                duree = int(input("Entrez la duree du film :"))
                langue = input("Entrez la langue :")
                film = filme()
                request = """insert into film
                    (Titre,descrption,realisateur,annee_sortie,duree,langue)
                    values (%s, %s, %s, %s, %s, %s)"""
                params = (Titre,description,realisateur,annee_sortie,duree,langue)
                film.insert_doc(request=request,params=params)
                print("Enregistrement effectuer...")
                
                
        elif choix == 3:
            print("""
                \n 1-Mettre à jour un livre
                \n 2-Mettre à jour un film
                  """)
            choi = int(input("Votre choix : "))
            if choi ==1 :
                premier = input("Que vous voulez mettre a jour (description,auteur,date_parution,maison_edition) :")
                deux =  input("entrez la valeur :")
                trois = input("Entrez le Titre du livre :")
                livre = Document()
                livre.update_doc(premier=premier,deux=deux,trois=trois,table="livre")
                print('Mise a jour effectuer...')
            if choi ==2 :
                premier = input("Que vous voulez mettre a jour (description,realisateur,duree,annee_sortie,langue) :")
                deux =  input("entrez la valeur :")
                trois = input("Entrez le titre du film :")
                film = filme()
                film.update_doc(premier=premier,deux=deux,trois=trois,table="film")
                print('Mise a jour effectuer...')
                
                
        elif choix == 4:
            print("""
                \n 1-Supprimer un livre
                \n 2-Supprimer un film
                  """)
            choi = int(input("Votre choix : "))
            if choi ==1 :
                sup = str(input("Entrez le Titre du livre a supprimer :"))
                livre = Document(nom=sup)
                livre.delete_doc(table="livre")
                print('Suppression effectuer...')
            if choi ==2 :
                sup = str(input("Entrez le titre du film a supprimer :"))
                film =filme(nom=sup)
                film.delete_doc(table="film")
                print('Suppression effectuer...')
                
        elif choix == 5:
            main()
        else:
            print("Choix invalide. Veuillez réessayer.")
            choix = int(input("Votre choix : "))
        choix = int(input("Veillez entrez votre nouveau choix : "))
    print('Merci ("_")')
    
def pret ():
    print("""    
        -----------------------------
        Menu - Gestion des prets:
        ------------------------------
        """)
    print("""
        \n 1-Inserer un pret 
        \n 2-Retour d'article
        \n 3-List pret en retard
        \n 4-Retour au menu principal
        \n 0-Quitter
        """)
    
    choix = int(input("Votre choix : "))
    while choix != 0:
        if choix == 1:
            from datetime import date
            inconn = input("Est-ce un livre ou un film :")
            inconnu = inconn.title()
            if inconnu == "Livre":
                id_ = int(input("Entrez id du livre :"))
            if inconnu == "Film":
                id_ = int(input("Entrez id du Film :"))
            id_Personne = int(input("Entrez id de la personne :"))
            print("Veillez inserer la date retour")
            annee = 2023
            mois = int(input("Entrez le mois :"))
            jour = int(input("Entrez le jour :"))
            date_a_inserer = date(annee, mois, jour)
            date_formatee = date_a_inserer.strftime('%Y-%m-%d')
            pret = Pret()
            pret.insert_pret(id_=id_,id_Personne=id_Personne,date_formatee=date_formatee,inconnu=inconnu)
            print("Enregistrement effectuer...")
                
        elif choix == 2:
            idp = input("Id du pret :")
            pret = Pret()
            pret.retour_document(idp=idp)
            print('Mise a jour effectuer...')
                
        elif choix == 3:
            inc = input("Est-ce un livre ou un film :")
            ince = inc.title()
            pret = Pret()
            pret.list_pret(inconnue=inc,inconnuee=ince)
            print('...')
                
        elif choix == 4:
            main()
        else:
            print("Choix invalide. Veuillez réessayer.")
            choix = int(input("Votre choix : "))
        choix = int(input("Veillez entrez votre nouveau choix :"))
    print('Merci ("_")')
            
    
if __name__ == "__main__":
    main()
        