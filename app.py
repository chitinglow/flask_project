from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': "Singapore",
    'Salary': 50000
}, {
    'id': 2,
    'title': 'Data Science',
    'location': 'Singapore',
    'Salary': 60000
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Singapore',
    'Salary': 60000
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Singapore',
    'Salary': 60000
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
