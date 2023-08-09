from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    jobs = load_jobs_from_db()
    return render_template ('home.html', various=jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    return render_template ('jobpage.html', single_job=job)

app.run(host='127.0.0.1', port=5000, debug=True)

