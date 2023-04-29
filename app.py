from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru India',
    'salary': 'Rs 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Delhi India',
    'salary': 'Rs 15,00,000'
  },
  {
    'id': 3,
    'title': 'Web Developer',
    'location': 'Remote',
    'salary': 'Rs 9,50,000'
  },
  {
    'id': 4,
    'title': 'Blockchain Developer',
    'location': 'Florida, USA',
    'salary': '$ 110,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def jobs_list():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
