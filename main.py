from DataLayer.UnitOfWork.context import Context 
from DataLayer.Database.ConnectionString import DB_Provider


# instance of DataBase
cntx = Context(DB_Provider())
cntx.DB.EXECUTE(cntx.SQL('rigister','Email').GetCustom(UserName = 'ali'))
print(cntx.DB.GET())

print("---------------------")

cntx.DB.EXECUTE(cntx.SQL('rigister').GetAll())
print(cntx.DB.GET())