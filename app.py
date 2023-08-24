from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def Home():
    jobs = load_jobs_from_db()
    return render_template ('home.html', various=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "not found", 404
    return render_template ('jobpage.html', single_job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job)


app.run(host='127.0.0.1', port=5000, debug=True)

