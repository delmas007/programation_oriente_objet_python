from connection_bd.connection import cursor,connection
from api.Parent import Parent

class Document(Parent):
    def __init__(self,nom=None,description=None,annee=None,auteur=None,maison_edition=None,ref_livre=None,premier=None,deux=None,trois=None,table=None):
        super().__init__(nom,description,annee,auteur)
        self.maison_edition = maison_edition 
        self.ref_livre = ref_livre
        self.premier = premier
        self.deux = deux
        self.trois = trois
        self.table = table
    
    # def liste_doc(self, table):
    #     return super().liste_doc(table)
    
    # def update_doc(self, premier, deux, trois, table):
    #     return super().update_doc(premier, deux, trois, table)
    
    # def delete_doc(self, table):
    #     return super().delete_doc(table)
    
    # def insert_doc(self):
    #     request = """insert into livre
    #         (Titre,description,auteur,date_parution,ref_livre,maison_edition)
    #         values (%s, %s, %s, %s, %s, %s)"""
    #     params = (self.nom,self.description,self.auteur,self.annee,self.ref_livre,self.maison_edition)
    #     cursor.execute(request,params)
    #     connection.commit()
    # def insert_doc(self):
    #     request = """insert into livre
    #     (Titre,description,auteur,date_parution,ref_livre,maison_edition)
    #     values (%s, %s, %s, %s, %s, %s)"""
    #     params = (self.nom,self.description,self.auteur,self.annee,self.ref_livre,self.maison_edition)
    #     return super().insert_doc(request, params)
    
   
        
