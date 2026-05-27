Intelligent Location Recommendation Agent

An intelligent software agent that provides personalized nearby restaurant recommendations using LLM reasoning, Google Maps APIs, memory, reflection, and interactive visualization.

Features
LLM-based planning and reasoning
Personalized recommendations with memory
Google Places API integration
Google Routes API integration
Interactive map visualization with Folium
Reflection / self-correction agent
Browser GPS location detection
Streamlit-based UI
Logging system for interaction tracing
System Workflow
The user enters a restaurant-related request.
The Planner Agent extracts structured preferences using LLM reasoning.
The Memory Module provides historical user preferences.
The Location Getter retrieves the current GPS location.
The Map Tool searches nearby places using Google APIs.
The Recommender Agent ranks candidate places.
The Reflection Agent evaluates recommendation quality.
Results are displayed through the Streamlit UI with interactive maps.
Technologies Used
Python
Streamlit
OpenAI-Compatible DeepSeek API
Google Places API
Google Routes API
Folium
Streamlit Geolocation
Project Structure
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
Installation
1. Clone the Repository
git clone <your-github-repo-link>
cd <repo-name>
2. Install Dependencies
pip install -r requirements.txt
API Configuration

Create a config.py file:

OPENAI_API_KEY = "your_deepseek_api_key"

GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"
Run the Application
streamlit run app.py
Usage
Allow browser location access.
Enter a restaurant-related request such as:
cheap korean bbq nearby
The system will:
understand user preferences
search nearby restaurants
calculate travel distance
rank recommendations
evaluate recommendation quality
display results on an interactive map
Example Capabilities
Nearby restaurant recommendation
Personalized preference adaptation
Reflection-based recommendation evaluation
Interactive route-aware recommendations
Demo Video

[Paste Demo Video Link Here]

GitHub Repository

[Paste GitHub Repository Link Here]

Course Concepts Applied

This project applies several intelligent agent concepts covered in CS767, including:

Planning and reasoning
Tool-augmented agents
Memory systems
Reflection and self-correction
Multi-module agent architecture
Environment interaction through APIs
Interactive visualization
Future Improvements
Multi-agent collaboration
Weather-aware recommendations
User feedback learning
Voice interaction
Advanced recommendation scoring
