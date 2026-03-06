from flask import Flask, request, jsonify, send_from_directory
from server import util
import os

app = Flask(__name__, static_folder='../UI')


@app.route('/')
def serve_index():
    return send_from_directory('../UI', 'app.html')


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../UI', path)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Celebrity Image Classification")
    util.load_saved_artifacts()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
