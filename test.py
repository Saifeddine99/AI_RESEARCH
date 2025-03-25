from google import genai

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access the API key
api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)