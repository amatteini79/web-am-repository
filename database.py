import sqlalchemy
from sqlalchemy import create_engine, text, insert




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
        par = {'var' : id}
        result = conn.execute(text("select * from jobs where id = :var"),par)
        rows = result.all()
    if len(rows) == 0:
        return None
    else:
        return (rows[0]._asdict())
    
def add_application_to_db(id, data):
    with engine.connect() as conn:
        parameters = {'job_id' : id, 'full_name' : data['full_name'], 'email' : data['email']}
        print(parameters)
        stmt = text("INSERT INTO applications (job_id, full_name, email) VALUES (:job_id, :full_name, :email)")
        conn.execute(stmt, parameters)
        conn.commit()
