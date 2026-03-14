import os
from google import genai

# Initialize client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_actions(topic: str) -> str:
    """
    Generates 3 actionable sustainability steps for a student based on a topic,
    using the Gemini 2.5 Flash model.
    """
    prompt = f"""
    Give 3 simple actions a student can take related to {topic} that help sustainability.
    Keep each action short.

    Include the following in Markdown format:
    ### Recommended Actions for {topic}
    1. [Action 1]
    2. [Action 2]
    3. [Action 3]

    **Why it matters:** [Brief explanation of the impact]
    
    **Source:** [Organization Name](URL)
    """

    try:
        # Using Gemini-2.5-flash as requested
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        if response.text:
            return response.text
        return "No content was generated."

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    topic = "plastic pollution"
    result = generate_actions(topic)

    print("\nGenerated Actions:\n")
    print(result)
