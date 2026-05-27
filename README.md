# Intelligent Location Recommendation Agent

An intelligent software agent that provides personalized nearby restaurant recommendations using LLM reasoning, Google Maps APIs, memory, reflection, and interactive visualization.

---

# Features

- LLM-based planning and reasoning
- Personalized recommendations with memory
- Google Places API integration
- Google Routes API integration
- Interactive map visualization with Folium
- Reflection / self-correction agent
- Browser GPS location detection
- Streamlit-based UI
- Logging system for interaction tracing

---

# System Workflow

1. The user enters a restaurant-related request.
2. The **Planner Agent** extracts structured preferences using LLM reasoning.
3. The **Memory Module** provides historical user preferences.
4. The **Location Getter** retrieves the current GPS location.
5. The **Map Tool** searches nearby places using Google APIs.
6. The **Recommender Agent** ranks candidate places.
7. The **Reflection Agent** evaluates recommendation quality.
8. Results are displayed through the Streamlit UI with interactive maps.

---

# Technologies Used

- Python
- Streamlit
- DeepSeek API
- Google Places API
- Google Routes API
- Folium
- Streamlit Geolocation

---

# Project Structure

```text
project/
│
├── app.py
├── planner.py
├── maps_tool.py
├── recommender.py
├── reflection.py
├── memory.py
├── logger.py
├── config.py
└── requirements.txt
