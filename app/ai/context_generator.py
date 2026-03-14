import os
from google import genai
from action_generator import generate_actions


# Initialize the client
# Ensure GEMINI_API_KEY is set in your environment variables
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_explanation(topic: str) -> str:

    """
    Generates a short educational explanation about a sustainability topic.
    """
    prompt = f"""
    Explain the sustainability issue behind '{topic}' in 2-3 simple sentences.

    Include the following in Markdown format:
    - A clear explanation
    - Why it matters
    - One credible source (URL or name)
    """

    try:
        # Using Gemini-2.5-flash
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        if response.text:
            return response.text
        return "No content was generated."

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def generate_context_package(topic):
    
    explanation = generate_explanation(topic)
    actions = generate_actions(topic)

    return {
        "explanation": explanation,
        "actions": actions
    }


if __name__ == "__main__":
    topic = "climate change"
    result = generate_context_package(topic)

    print("\n--- Generated Explanation ---")
    print(result["explanation"])
    print("\n--- Recommended Actions ---")
    print(result["actions"])