import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='firstbank', database='firstbank')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM testTB;")
for Cid, Name in cursor:
  print("Cid: {}, Name: {}").format(Cid,Name)
  
mariadb_connection.close()
