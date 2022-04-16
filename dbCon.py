import sqlite3
from datetime import datetime

class reviewsDb:


    conn = sqlite3.connect("reviews.db")
    c = conn.cursor()

    tablename = "reviews"

    def create_table(self):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.tablename} (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            username text NOT NULL,
            datatime text NOT NULL,
            language text NOT NULL,
            review text NOT NULL
            )""")
        self.conn.commit()


        print(f"Table {self.tablename} succesuly created")



    def insert_rewiews(self,username:str,datatime:str,language:str,review:str):
        
        username = username.replace('"',"")
        review = review.replace('"',"")

        sql = f"""INSERT  INTO {self.tablename} (username,datatime,language,review) VALUES ( 
            '{username}',
            '{datatime}',
            '{language}',
            '{review}'
            )
            """


        try:
            
            self.c.execute(sql)
            self.conn.commit()
            print("data succesuly iserted")

        except Exception as e:
            print(e)
            f = open("log.txt","a")
            f.write(f"{e} \n{sql}\n{datetime.now()}\n")

    def get_all_column(self):
        
        self.c.execute(f"SELECT  * FROM  {self.tablename}")
        return  self.c.fetchall()
        

    def filter_by_year_DESC(self):

        self.c.execute(f"SELECT * FROM {self.tablename} ORDER BY year DESC")
        return  self.c.fetchall()

    def filter_by_year_ASC(self):
        self.c.execute(f"SELECT * FROM {self.tablename} ORDER BY year ASC")

        return self.c.fetchall()
        
    def get_all_usernames(self):
        self.c.execute(f"SELECT username FROM {self.tablename}")

        return self.c.fetchall()
        



    
    def findUsernameById(self,id):
        self.c.execute(f"SELECT * FROM {self.tablename} WHERE id={id}")
        return self.c.fetchall()

 


    def close_db(self):
        self.conn.close()




class DublicateDb:

    conn = sqlite3.connect("reviews.db")
    c = conn.cursor()



    tablename = "dublicate"

    def create_table(self):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {self.tablename} (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            word text NOT NULL,
            count_word INT NOT NULL
            )""")
        self.conn.commit()


        print(f"Table {self.tablename} succesuly created")
    

    def insert_dublicate(self,word:str,count_word:int):
        
        word = word.replace("'","_").replace('"',"_").lower()

        sql = f"""INSERT  INTO {self.tablename} (word,count_word) VALUES ( 
            '{word}',
            '{count_word}'
            )
            """


        try:
            self.c.execute(sql)
            self.conn.commit()
            print(f"data succesuly iserted {word} {str(count_word)}")

        except Exception as e:
            print(e)
            f = open("log.txt","a")
            f.write(f"{e} \n{sql}\n{datetime.now()}\n")

    

    # def get_all_column(self):        
    #     self.c.execute(f"SELECT  * FROM  {self.tablename}")
    #     return  self.c.fetchall()
        
