# 🍜 Intelligent Location Recommendation Agent

An intelligent software agent that provides personalized nearby restaurant recommendations using LLM reasoning, Google Maps APIs, memory, reflection, and interactive visualization.

---

# ✨ Features

- 🧠 LLM-based planning and reasoning
- 💾 Personalized recommendations with memory
- 📍 Google Places API integration
- 🚗 Google Routes API integration
- 🗺 Interactive map visualization with Folium
- 🪞 Reflection / self-correction agent
- 🌍 Browser GPS location detection
- 💻 Streamlit-based UI
- 📜 Logging system for interaction tracing

---

# 🔄 System Workflow

1. The user enters a restaurant-related request.
2. The **Planner Agent** extracts structured preferences using LLM reasoning.
3. The **Memory Module** provides historical user preferences.
4. The **Location Getter** retrieves the current GPS location.
5. The **Map Tool** searches nearby places using Google APIs.
6. The **Recommender Agent** ranks candidate places.
7. The **Reflection Agent** evaluates recommendation quality and identifies possible improvements.
8. Results are displayed through the Streamlit UI with interactive maps.

---

# 🛠 Technologies Used

- Python
- Streamlit
- DeepSeek API
- Google Places API
- Google Routes API
- Folium
- Streamlit Geolocation

---

# 📂 Project Structure

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
```

---

# ⚙ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/MLI282/767Assignment.git
```

---

## 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Required Libraries

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

## 4️⃣ Configure API Keys

```python
api_key = "your_deepseek_api_key"   # planner.py

GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"   # maps_tool.py
```

⚠ Notice:

I currently use my own DeepSeek API key for demonstration purposes.  
The key will remain available until the end of June.

For large-scale testing or long-term usage, please use your own API key.

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Allow browser location access.
2. Enter a restaurant-related request such as:

```text
cheap korean bbq nearby
```

3. The system will:

- 🧠 Extract user preferences
- 📍 Search nearby restaurants
- 🚗 Calculate travel distance and duration
- ⭐ Rank recommendation results
- 🪞 Perform reflection and self-correction on recommendations
- 🗺 Display recommendations on an interactive map

---

# 🎯 Example Capabilities

- Nearby restaurant recommendation
- Personalized preference adaptation
- Reflection-based recommendation evaluation
- Interactive route-aware recommendations

---

# 📹 Demo Video

[Paste Demo Video Link Here]

---

# 🔗 GitHub Repository

https://github.com/MLI282/767Assignment

---

# 📚 Course Concepts Applied

This project applies several intelligent agent concepts covered in CS767, including:

- Planning and reasoning
- Tool-augmented agents
- Memory systems
- Reflection and self-correction
- Multi-module agent architecture
- Environment interaction through APIs
- Interactive visualization

---

# 🔮 Future Improvements

- Multi-agent collaboration
- Weather-aware recommendations
- User feedback learning
- Voice interaction
- Advanced recommendation scoring
