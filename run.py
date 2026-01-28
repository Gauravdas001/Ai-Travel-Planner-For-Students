# run.py
from workflow import app
from helper_func import clean_itinerary, clean_weather

preferences = {
    "destination": "Paris",
    "budget": 1000,
    "interests": ["art", "food"],
    "dates": "2026-01-01 to 2026-01-30"
}
result = app.invoke({"preferences": preferences})
result["itinerary"] = clean_itinerary(result["itinerary"])
result["weather"] = clean_weather(result["weather"])
print("Itinerary:\n", result["itinerary"])
print("Weather:\n", result["weather"])