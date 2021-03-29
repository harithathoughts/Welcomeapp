from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    #return "Welcome to the Application!"
    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
