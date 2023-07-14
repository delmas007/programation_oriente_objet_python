from connection_bd.connection import cursor,connection
from datetime import date

class Pret:
    
    def __init__(self):
        pass
    
    
    def insert_pret(self,inconnu,id_,id_Personne,date_formatee):
        date_pret = date.today()
        date_formate_pret = date_pret.strftime('%Y-%m-%d')
        
        rendu = False
        request = f"insert into pret(date_pret,date_retour,rendu,id_{inconnu.strip('')},id_Personne)values (%s, %s, %s, %s, %s)"
        params = (date_formate_pret,date_formatee,rendu,id_,id_Personne)
        cursor.execute(request,params)
        connection.commit()
        
    def retour_document(self,idp):
        valeur = True
        request =  "update pret set rendu = %s where id= %s"
        params = (valeur,idp)
        cursor.execute(request,params)
        connection.commit()
    
    def list_pret(self,inconnue,inconnuee):
        request = f"SELECT {inconnue.strip('')}.Titre, personne.nom, personne.prenom FROM {inconnue.strip('')} JOIN pret ON {inconnuee.strip('')}.id = pret.id_{inconnue.strip('')} JOIN personne ON personne.id = pret.id_Personne WHERE rendu=0 AND date_retour < CURDATE();"
        cursor.execute(request)
        donnee = cursor.fetchall()
        for i in donnee:
            print(i)
            