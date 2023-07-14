from connection_bd.connection import cursor,connection
from api.Parent import Parent

class filme(Parent):
    def __init__(self, nom=None, description=None, annee=None, auteur=None, duree = None, langue=None):
        super().__init__(nom, description, annee, auteur)
        self.duree = duree
        self.langue = langue
        
    # def liste_doc(self, table):
    #     return super().liste_doc(table)
    
    # def update_doc(self, premier, deux, trois, table):
    #     return super().update_doc(premier, deux, trois, table)
    
    # def delete_doc(self, table):
    #     return super().delete_doc(table)
    
    # def insert_doc(self):
    #     request = """insert into film
    #         (Titre,descrption,realisateur,annee_sortie,duree,langue)
    #         values (%s, %s, %s, %s, %s, %s)"""
    #     params = (self.nom,self.description,self.auteur,self.annee,self.duree,self.langue)
    #     cursor.execute(req uest,params)
    #     connection.commit()
    
    # def insert_doc(self):
    #     request = """insert into film
    #         (Titre,descrption,realisateur,annee_sortie,duree,langue)
    #         values (%s, %s, %s, %s, %s, %s)"""
    #     params = (self.nom,self.description,self.auteur,self.annee,self.duree,self.langue)
    #     return super().insert_doc(request, params)