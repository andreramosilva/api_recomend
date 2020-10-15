import mysql.connector
from mysql.connector import Error
from flask import jsonify


class Storage():
    def __init__(self):
         connection = mysql.connector.connect(host='localhost',
                                         database='dbuser_amigo_recomend',
                                         user='root',
                                         password='rootpassword')
    def show_all_users(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='dbuser_amigo_recomend',
                                         user='root',
                                         password='rootpassword')
   

            sql_select_Query = "select * from user_amigo"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            
   

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")    
        return(records)

    def populate(self,nome,amigo):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='dbuser_amigo_recomend',
                                         user='root',
                                         password='rootpassword')
   
            query = "INSERT INTO user_amigo (nome,amigo) VALUES('"+nome+"','"+amigo+")"
            sql_select_Query = "INSERT INTO user_amigo (nome,amigo) VALUES({nome},{amigo})"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            
   

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")    
        return("Cadastrado com sucesso.")

    def show_recomendation(self,nome):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='dbuser_amigo_recomend',
                                         user='root',
                                         password='rootpassword')

            query = "select * from (select nome from user_amigo where nome_amigo <> '"+nome+"' and nome <> '"+nome+"') nao_amigo left join  (select nome_amigo from user_amigo where nome = '"+nome+"') amigo on nome = nome_amigo where nome_amigo is null"
            print("#####")
            print(query)
            print("######")
            sql_select_Query = query
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            return(records)
            
   

        except Error as e:
            print("Error reading data from MySQL table", e)
            return e
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")    
        


    def show_all_friends(self,nome):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='dbuser_amigo_recomend',
                                         user='root',
                                         password='rootpassword')

            query = "select * from user_amigo where nome = '"+nome+"'"
            print(query)

            sql_select_Query = query
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            return(records)
            
   

        except Error as e:
            print("Error reading data from MySQL table", e)
            return e
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")    
        
 