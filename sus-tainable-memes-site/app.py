from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import main

app = Flask(__name__)
CORS(app) # Allow react frontend to call app

IMG_FILE = "generated_image.png"

@app.route("/generate", methods=["POST"]) # When localhost:5000/generate recieves POST, it runs the following function generate
def generate():
    data = request.json
    text_input = data.get("text", "")
    print("Received:", text_input)

    if(text_input.strip() == ""):
        return jsonify({"context": "",
                    "actions": ""})
    # Start getting images and stuff
    amplified_output = main.amplify_input(text_input)
    print(amplified_output)
    result = {"explanation": "Your question was flagged as inappropriate",
              "actions": "Please try a different prompt!"}
    # Inappropriate prompts are rejected
    if (amplified_output == "ERROR-101"):
        print("ERROR RECORDED")

        # Replace previous image with a placeholder since it's not appropriate 
        placeholder_image_path = os.path.join("./src/assets/placeholder.png")
        output_image_path = os.path.join(IMG_FILE)
        if os.path.exists(placeholder_image_path):
            with open(placeholder_image_path, "rb") as src, open(output_image_path, "wb") as dst:
                dst.write(src.read())
    else:
        print("Hello World")
        # Send the prompt to generate a bunch of extra context info
        result = main.generate_context_package(text_input)

        # Generate an image
        print("Image Generation has started")
        my_image = main.generate_image(amplified_output)

        if my_image:
           my_image.show()

    return jsonify({"context": result["explanation"],
                    "actions": result["actions"]})

@app.route("/generated_image.png")
def serve_image():
    return send_file(IMG_FILE)

if __name__ == "__main__":
    app.run(port=5000) # Host location: localhost:5000 DO NOT FORGET