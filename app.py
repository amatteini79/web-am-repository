from flask import Flask, render_template
from database import engine
from sqlalchemy import Text

app = Flask(__name__)


def load_from_db():
with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
return jobs

@app.route("/")
def HelloWorld():
    jobs = load_from_db()
    return render_template ('home.html', various=jobs)

app.run(host='127.0.0.1', port=5000, debug=True)

