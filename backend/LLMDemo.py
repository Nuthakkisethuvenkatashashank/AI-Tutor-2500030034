import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("===== AI TUTOR USING GEMINI =====")

question = input("\nEnter your question: ")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )

    print("\n===== GEMINI RESPONSE =====")
    print(response.text)

except Exception as e:
    print("Error:", e)
