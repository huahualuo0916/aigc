from flask import Flask, request, jsonify
from text2img import text2img

app = Flask(__name__)


@app.route('/generate_image', methods=['GET'])
def generate_image():
    text = request.args.get('text')
    type = request.args.get('type')
    wait_seconds = request.args.get('wait', default=10, type=int)

    # Call your text to img function to get the image URL
    image_url = text2img(text, type, wait_seconds)

    # Return the image URL as JSON
    return jsonify({'image_url': image_url})


if __name__ == '__main__':
    app.run(debug=True)