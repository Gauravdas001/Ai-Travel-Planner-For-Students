import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Use a model that YOUR API supports
model = genai.GenerativeModel("models/gemini-flash-latest")

def llm(prompt: str) -> str:
    system_prompt = f"""
You are an AI travel planner for students.

Rules:
- Return ONLY Markdown
- Use this format strictly:

### Day 1
- Morning: ...
- Afternoon: ...
- Evening: ...
💰 Total cost: $...

### Day 2
- Morning: ...
- Afternoon: ...
- Evening: ...
💰 Total cost: $...

{prompt}
"""
    response = model.generate_content(system_prompt)
    return response.text.strip()