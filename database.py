import sqlalchemy
from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://andrea:Gramolazzo15@localhost/mysite?charset=utf8mb4"
engine = create_engine(db_connection_string)


        

