from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    #return "Welcome to the Application!"
    return render_template('homepage.html')
