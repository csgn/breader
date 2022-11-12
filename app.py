import os
import sys

from flask import Flask, abort, request
from flask_cors import CORS


from barcode import BarcodeDetector

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return abort(403)

@app.route('/barcode', methods=['POST'])
def barcode():
    if request.referrer != os.environ.get('REFERRER_URL'):
        return abort(403)

    file = request.files.get('file', None)

    if not file:
        return {"error": "file is not specified"}, 200

    return BarcodeDetector.decode(file), 200


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
        load_dotenv()

        app.run(host=os.environ.get('HOST'),
                port=os.environ.get('PORT', 5000),
                debug=os.environ.get('DEBUG', False))
    except Exception as e:
        sys.exit(1)

