from flask import Flask, render_template
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    jobs = load_jobs_from_db()
    return render_template ('home.html', various=jobs)

app.run(host='127.0.0.1', port=5000, debug=True)

