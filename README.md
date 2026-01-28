🧳 AI Travel Planner for Students

A Generative AI–powered travel planning application that helps students create personalized, budget-friendly, day-wise itineraries using real-time information and structured AI workflows.

⸻

✨ What this project does
	•	Takes destination, budget, interests, and travel dates
	•	Fetches real-time destination info & weather
	•	Uses Generative AI to create a student-friendly itinerary
	•	Presents results in a clean Streamlit web interface

Built to demonstrate practical GenAI + workflow orchestration, not just a single LLM call.

⸻

🧠 How it works (High-level)

User (Streamlit UI)
        ↓
Preferences Input
        ↓
LangGraph Workflow
   ├── Destination Info (Tavily API)
   ├── Itinerary Generation (Gemini LLM)
   └── Weather Check (Tavily API)
        ↓
Formatted Output
        ↓
Final Travel Plan


⸻

🚀 Features
	•	✅ Personalized itineraries
	•	✅ Budget-aware planning (student-focused)
	•	✅ Day-wise structure (Morning / Afternoon / Evening)
	•	✅ Real-time destination insights
	•	✅ Weather information
	•	✅ Modular, explainable AI workflow

⸻

🛠️ Tech Stack
	•	Python
	•	Streamlit – Web UI
	•	LangGraph – Workflow orchestration
	•	Google Gemini – Generative AI
	•	Tavily API – Search & weather data
	•	dotenv – Secure environment variables

⸻

📂 Project Structure

├── app.py              # Streamlit UI
├── workflow.py         # LangGraph workflow logic
├── llm.py              # Gemini LLM integration
├── state.py            # Shared workflow state
├── helper_func.py      # Output cleaning utilities
├── run.py              # CLI runner for testing
├── README.md           # Documentation


⸻

⚙️ Setup & Installation

1️⃣ Clone the repository

git clone <repository-url>
cd AI-Travel-Planner-For-Students


⸻

2️⃣ Create & activate a virtual environment

python -m venv .venv
source .venv/bin/activate   # macOS/Linux


⸻

3️⃣ Install dependencies

python -m pip install -r requirements.txt

You can also install dependencies from pyproject.toml if preferred.

⸻

4️⃣ Configure environment variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

⸻

5️⃣ Run the application

Web App (recommended)

streamlit run app.py

CLI test runner

python run.py


⸻

🧪 Example

Input
	•	Destination: Paris
	•	Budget: $1000
	•	Interests: Art, Food
	•	Dates: 2026-01-01 to 2026-01-30

Output
	•	Day-wise itinerary
	•	Budget-aware activities
	•	Weather summary

⸻

🎯 Use cases
	•	Students planning low-budget trips
	•	GenAI + workflow orchestration demos
	•	Internship / academic projects
	•	Learning LangGraph with real APIs

⸻

🔮 Future Improvements
	•	Hostel & hotel price prediction
	•	Public transport cost estimation
	•	Multi-language support
	•	User accounts & saved trips
	•	Mobile-friendly deployment

⸻

🤝 Contributing

Contributions are welcome!
	1.	Fork the repo
	2.	Create a feature branch
	3.	Commit your changes
	4.	Open a pull request

⸻

📄 License

This project is licensed under the MIT License.

⸻

👤 Author

Gauravdas001
AI / ML Internship – IBM SkillsBuild