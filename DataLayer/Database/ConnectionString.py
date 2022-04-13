import sqlite3

class DB_Provider():
    def __init__(self):
        self.conn = sqlite3.connect(r'DataLayer\DataBase\database.db')
        self.cur = self.conn.cursor()

    def EXECUTE(self,sqlCommand):
        return self.cur.execute(sqlCommand)

    def COMMIT(self):
        return self.conn.commit()

    def GET(self):
        return(self.cur.fetchall())
