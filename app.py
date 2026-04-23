from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Mini SaaS Task Manager</h1>
    <p>Your app is running.</p>
    <p>Next: add signup, login, and tenant logic.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
