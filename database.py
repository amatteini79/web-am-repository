import sqlalchemy
from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://andrea:Gramolazzo15@localhost/mysite?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dict = []
        for row in result.all():
                result_dict.append(row._asdict())
        print(result_dict)

        

