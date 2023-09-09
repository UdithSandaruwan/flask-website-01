from flask import Flask, render_template,jsonify

app = Flask(__name__)

Jobs =[
  {
    'name' :'sani 01',
    'age': 5,
    'salary':'lkr10000'
  },
  {
    'name' :'sani 01',
    'age': 5,
  },
  {
    'name' :'sani 01',
    'age': 5,
    'salary':'lkr10000'
  }
]


@app.route("/")
def Home():
  return render_template('home.html',jobs=Jobs)

@app.route("/hire-me")
def HireMe():
  return render_template('hire-me.html.html')

@app.route("/api/jobs")
def listJobs():
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)