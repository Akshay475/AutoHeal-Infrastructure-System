from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AutoHeal Infrastructure System is Running Akshay!"
@app.route("/health")
def health():
    return "Application is Healthy!"
@app.route("/about")
def about():
    return "This project is built by Akshay for DevOps learning."
if __name__ == "__main__":
    app.run(debug=True)
