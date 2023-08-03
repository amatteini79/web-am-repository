from flask import Flask, render_template
from database import engine
from sqlalchemy import Text

app = Flask(__name__)

INFOS = [
    {
    "id" : "1",
    "title" : "To do for first",
    "worker" : "Tim",
},
    {
    "id" : "2",
    "title" : "To do for second",
    "worker" : "jim",
}
]

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dict = []
    for row in result.all():
        result_dict.append(row._asdict())

@app.route("/")
def HelloWorld():
    return render_template ('home.html', various=INFOS)

app.run(host='127.0.0.1', port=5000, debug=True)

