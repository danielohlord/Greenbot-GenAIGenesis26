import os
from google import genai
from PIL import Image

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"  # adjust path if needed
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY")

from pyscript.context_generator import generate_context_package


client = genai.Client(api_key=API_KEY)

def amplify_input(prompt):  
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Generate for me ONE, ONLY ONE image prompt that turns the following input into " \
            "something very funny MEME prompt where it be used for image generation. However, "
            "if the prompt is inappropriate, just output the new prompt as ERROR-101. Prompt: "+prompt
        )
        return response.text
    except Exception as e:
        print("Text Generation has failed")
        return prompt

def generate_image(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=["Generate this image:" +prompt]
        )
        
        # Image retrieval
        # Gemini doesn't send all of it at once, but instead in parts.
        # 1. Look at everything gemini sends back
        for part in response.parts:

            # If there is no data (filter, etc), then 
            if part.text is not None:
                print(part.text)

            # Gemini sends raw binary bytes. It checks te inline_data
            elif part.inline_data is not None:

                # Takes the raw numbers and wraps it into an image
                image = part.as_image()

                # Actually save the image to the project folder
                image.save("generated_image.png")

    except Exception as e:
        if "RESOURCE_EXHAUSTED" in str(e):
            print("You've hit your quota")
        else:
            print("Image generation has failed")
    return None

if(__name__ == "__main__"):
    prompt = input("Input your sustainability thing: ")
    amplified_output = amplify_input(prompt)
    print(amplified_output)

    # Inappropriate prompts are rejected
    if (amplified_output == "ERROR-101"):
        print("ERROR RECORDED")
    else:
        print("Image Generation has started")
        my_image = generate_image(amplified_output)

        if my_image:
            my_image.show()

    topic = "climate change"
    result = generate_context_package(topic)

    print("\n--- Generated Explanation ---")
    print(result["explanation"])
    print("\n--- Recommended Actions ---")
    print(result["actions"])