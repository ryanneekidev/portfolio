from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderHomepage():
  return render_template('home.html')

@app.route("/about")
def renderAboutPage():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)