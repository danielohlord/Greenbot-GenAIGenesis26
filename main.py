import os
from google import genai
from PIL import Image


API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

prompt = input("Input your sustainability thing: ")

def amplify_input(prompt):  
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

def generate_image(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview"
        contents=prompt
    )
print(amplify_input(prompt))
