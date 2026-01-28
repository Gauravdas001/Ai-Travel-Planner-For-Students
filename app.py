import streamlit as st
from workflow import app
from helper_func import clean_itinerary, clean_weather

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Travel Planner for Students",
    page_icon="🎒",
    layout="wide"
)

# --------------------------------------------------
# Header / Hero Section (Aligned with PPT)
# --------------------------------------------------
st.title("🎒 AI Travel Planner for Students")

st.markdown(
    """
    Smarter trips start here.
    AI-powered planning for students.
    """
)

st.divider()

# --------------------------------------------------
# Input Form Section
# --------------------------------------------------
st.subheader("🧭 Enter Your Travel Details")

with st.form("travel_form"):
    col1, col2 = st.columns(2)

    with col1:
        destination = st.text_input("📍 Destination", "Switzerland")
        dates = st.text_input(
            "📅 Travel Dates (YYYY-MM-DD to YYYY-MM-DD)",
            "2026-01-01 to 2026-01-03"
        )

    with col2:
        budget = st.number_input(
            "💰 Total Budget (USD)",
            min_value=100,
            value=1500,
            step=50
        )
        interests = st.multiselect(
            "🎯 Interests",
            ["Art", "Food", "History", "Nature", "Adventure", "Shopping", "Beach"],
            default=["Adventure", "History", "Food", ]
        )

    submitted = st.form_submit_button("✨ Generate My Travel Plan")

# --------------------------------------------------
# Processing & Output Section
# --------------------------------------------------
if submitted:
    with st.spinner("🧠 AI is planning your trip... please wait"):
        preferences = {
            "destination": destination,
            "budget": budget,
            "interests": interests,
            "dates": dates
        }

        try:
            result = app.invoke({"preferences": preferences})

            itinerary = clean_itinerary(
                result.get("itinerary", "No itinerary generated.")
            )
            weather = clean_weather(
                result.get("weather", "No weather data available.")
            )

            st.success("✅ Your personalized travel plan is ready!")

            st.subheader("📅 Generated Itinerary")
            st.markdown(itinerary)

            st.divider()

            st.subheader("🌦️ Weather Information")
            st.info(weather)

            st.warning(
                "💡 Note: Costs and activities are AI-generated estimates and may vary in real life."
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

# --------------------------------------------------
# Footer (Professional Touch)
# --------------------------------------------------
st.divider()
st.caption(
    "Built using Generative AI (Google Gemini), LangGraph workflow orchestration, "
    "Tavily real-time search, and Streamlit. Designed for students ❤️"
)