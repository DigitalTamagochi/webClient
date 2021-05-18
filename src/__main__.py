from .init import app
import os
# from .config import FLASK_PORT, FLASK_DEBUG

FLASK_PORT = int(os.environ.get('PORT', 8000))
FLASK_DEBUG = True
SALT = b'$2b$12$IXLidDjhFEVpIIhSZoMp/.'

HOST = "0.0.0.0"


if __name__ == "__main__":
    app.run(host=HOST, port=FLASK_PORT, debug=FLASK_DEBUG, threaded=True)
