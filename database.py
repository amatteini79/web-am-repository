import sqlalchemy
from sqlalchemy import create_engine, text




db_connection_string = "mysql+pymysql://andrea:Gramolazzo15@localhost/mysite?charset=utf8mb4"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),val=id)
    rows = result.all()
    if len(rows) == 0:
        return None
    else:
        return dict(rows[0])
        

