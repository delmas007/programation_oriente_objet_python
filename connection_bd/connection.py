import mysql.connector

connection  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "biblio_b"
)
cursor = connection.cursor()