from connection_bd.connection import cursor,connection
class Parent():
    def __init__(self,nom=None,description=None,annee=None,auteur=None):
        self.nom = nom
        self.description = description
        self.annee = annee 
        self.auteur = auteur

    def liste_doc(self,table):
            request = f"SELECT * FROM {table.strip('')}"
            cursor.execute(request)
            donnee = cursor.fetchall()
            for i in donnee:
                print(i)
        

    def update_doc(self,premier,deux,trois,table):
        request =  f"update {table.strip('')} set {premier.strip('')}= %s where Titre= %s"
        params = (deux,trois)
        cursor.execute(request,params)
        connection.commit()
        print("Nombre de lignes mises à jour :", cursor.rowcount)
        
    def delete_doc(self,table):
        request =  f"delete from {table.strip('')} WHERE Titre = %s"
        params = (self.nom)
        cursor.execute(request,(params,))
        connection.commit()

    def insert_doc(self,request,params):
        cursor.execute(request,params)
        connection.commit()
        