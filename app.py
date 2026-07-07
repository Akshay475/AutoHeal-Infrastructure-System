from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 AutoHeal Infrastructure System</h1>
    <h3>Application is Running Successfully</h3>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "AutoHeal",
        "version": "1.0.0",
        "environment": "development",
        "timestamp": datetime.now().isoformat()
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "AutoHeal Infrastructure System",
        "developer": "Akshay Roy",
        "framework": "Flask"
    })

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "error": "Page Not Found",
        "status": 404
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
