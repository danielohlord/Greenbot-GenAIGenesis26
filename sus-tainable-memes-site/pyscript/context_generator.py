import os
from google import genai
from pyscript.action_generator import generate_actions


# Initialize the client
# Ensure GEMINI_API_KEY is set in your environment variables
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) #WHY SI THIS NOT WORKING FYM 2 ARGUMENTS

def generate_explanation(topic: str) -> str:

    """
    Generates a short educational explanation about a sustainability topic.
    """
    prompt = f"""
    Explain the sustainability issue behind '{topic}' in 2-3 simple sentences and explain both upsides and downsides.

    Give explanations for each of the following sections formatted in Markdown:
    - Explanation
    - Why it matters
    - **Source:** [Proper citation with Markdown link to url of information]
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