from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':'1',
    'title': 'Software Engineer',
    'location': 'remote',
    'salary': 'MAD11999'
  },
  {
    'id':'2',
    'title': 'Hardware Engineer',
    'location': 'remote',
  }
]

@app.route("/")
def listJobsHtml():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def listJobsApi():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)