import sqlalchemy
from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://andrea:Gramolazzo15@localhost/mysite?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        first_row = dict(result_all[0])
        print(first_row)

