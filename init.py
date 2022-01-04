
from flask import Flask

app = Flask("note_service_backend")

@app.route("/ciao")
def home():
    return "ciao"

if __name__ == "__main__":
    app.run(host="192.168.0.100", port=5000)


