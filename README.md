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
└── requirements.txt

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MLI282/767Assignment.git
cd resturant_Afent
```

---

## 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\\Scripts\\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Required Libraries

```bash
pip install streamlit
pip install openai
pip install requests
pip install folium
pip install streamlit-folium
pip install streamlit-geolocation
```

Or directly install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Keys


The key we 
```python
api_key = "your_deepseek_api_key" in planner.py

GOOGLE_MAPS_API_KEY = "your_google_maps_api_key" in map_tools.py
```

---
Notice: I use my deepseek api key which cost money and it will keep utill the end of June,If you want Mass testing ,Please use your own key
## 5. Run the Application

```bash
streamlit run app.py
```

---

# Usage

1. Allow browser location access.
2. Enter a restaurant-related request such as:

```text
cheap korean bbq nearby
```

3. The system will:
- extract user preferences
- search nearby restaurants
- calculate travel distance
- rank recommendations
- evaluate recommendation quality
- display recommendations on an interactive map
