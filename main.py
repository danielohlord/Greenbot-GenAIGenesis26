import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

prompt = "Which model AI are you? Also, explain the quantum convergence theroem"
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)
print(response.text)

print("Hello world")