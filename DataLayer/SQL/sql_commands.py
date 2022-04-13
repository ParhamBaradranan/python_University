class mySQL:
    def __init__(self,TableName,header):
        self.Table = TableName
        self.header = header

    def INSEART(self,*data):
        sql = f"INSERT INTO {self.Table} {self.header} VALUES {data};"
        return sql

    def UPDATE(self,ID,*data):
        text_list = []
        for n in range(len(data)):
            text_list.append(f"{self.header[n]} = '{data[n]}'")
        text = ",".join(text_list)
        sql = f"UPDATE {self.Table} SET {text} WHERE ID = {ID};"
        return sql

    def DELETE(self,ID):
        sql = f"DELETE FROM {self.Table} WHERE ID = {ID}"
        return sql

    def GetAll(self):
        sql = f"SELECT * FROM {self.Table}"
        return sql

    def GetByID(self,ID):
        sql = f"SELECT * FROM {self.Table} WHERE ID = {ID}"
        return sql

    def GetCustom(self,**karg):
        txt = ",".join(self.header)
        searchBy = ""
        for k,v in karg.items():
            searchBy += f"{k} = '{v}'"
        sql = f"SELECT {txt} FROM {self.Table} WHERE {searchBy}"
        return sql

    