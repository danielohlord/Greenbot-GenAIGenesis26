from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import time
import os
# import main

app = Flask(__name__)
CORS(app) # Allow react frontend to call app

IMG_FILE = "generated_image.png"

@app.route("/generate", methods=["POST"]) # When localhost:5000/generate recieves POST, it runs the following function generate
def generate():
    data = request.json
    text_input = data.get("text", "")
    print("Received:", text_input)

    # Placeholder: simulate Gemini API call
    print("Generating image...")
    # You would put your actual Gemini API logic here:
    # gemini_response = call_gemini_api(text_input)
    # save image to STATIC_DIR/generated_image.png

    # Simulate processing delay
    time.sleep(5)

    # For testing, copy or save some test image
    placeholder_image_path = os.path.join("./src/assets/placeholder.png")
    output_image_path = os.path.join(IMG_FILE)
    if os.path.exists(placeholder_image_path):
        with open(placeholder_image_path, "rb") as src, open(output_image_path, "wb") as dst:
            dst.write(src.read())

    return jsonify({"status": "done"})

@app.route("/generated_image.png")
def serve_image():
    return send_file(IMG_FILE)

if __name__ == "__main__":
    app.run(port=5000) # Host location: localhost:5000 DO NOT FORGET