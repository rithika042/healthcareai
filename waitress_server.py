from waitress import serve
from test import app  # Import your Flask app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
