from flask import Flask
app = Flask(__name__)

import app.routes

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=None, load_dotenv=True)
