from DataLayer.SQL.sql_commands import mySQL

class Context():
    def __init__(self,DB):
        self.DB = DB
    def SQL(self,TableName,*header):
        return mySQL(TableName,header)