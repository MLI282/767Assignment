# app.py

import streamlit as st
import folium

from streamlit_folium import st_folium
from streamlit_geolocation import streamlit_geolocation

from planner import extract_preferences
from maps_tool import search_places
from recommender import rank_places
from reflection import reflect_recommendations
from memory import update_memory, get_memory


# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Intelligent Location Agent",
    page_icon="🍜",
    layout="wide"
)

# =====================================
# Session State
# =====================================

if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

if "preferences" not in st.session_state:
    st.session_state.preferences = None

if "reflection" not in st.session_state:
    st.session_state.reflection = None

if "searched" not in st.session_state:
    st.session_state.searched = False

# =====================================
# Title
# =====================================

st.title("🍜 Intelligent Location Agent")

st.write(
    "Find personalized nearby food recommendations."
)

# =====================================
# Browser GPS Location
# =====================================

st.subheader("📍 Location Access")

location = streamlit_geolocation()

lat = None
lng = None

if location:

    lat = location.get("latitude")
    lng = location.get("longitude")

# =====================================
# Stop if No Location
# =====================================

if lat is None or lng is None:

    st.warning(
        "Please allow browser location access."
    )

    st.stop()

# =====================================
# Show Location
# =====================================

st.success(
    f"Location detected: {lat}, {lng}"
)

# =====================================
# Memory Sidebar
# =====================================

st.sidebar.title("🧠 Memory")

st.sidebar.json(get_memory())

# =====================================
# User Input
# =====================================

user_input = st.text_input(
    "What are you looking for?"
)

# =====================================
# Search Button
# =====================================

if st.button("Search"):

    if not user_input:

        st.warning(
            "Please enter a request."
        )

    else:

        # =====================================
        # Planner Agent
        # =====================================

        with st.spinner(
            "Planner Agent understanding preferences..."
        ):

            preferences = extract_preferences(
                user_input,
                get_memory()
            )

            update_memory(preferences)

        # =====================================
        # Maps Tool
        # =====================================

        with st.spinner(
            "Searching nearby places..."
        ):

            candidate_places = search_places(
                preferences,
                lat,
                lng
            )

        # =====================================
        # No Results
        # =====================================

        if len(candidate_places) == 0:

            st.error("No places found.")

        else:

            # =====================================
            # Recommender Agent
            # =====================================

            with st.spinner(
                "Recommender Agent ranking places..."
            ):

                recommendations = rank_places(
                    candidate_places,
                    preferences
                )

            # =====================================
            # Reflection Agent
            # =====================================

            with st.spinner(
                "Reflection Agent evaluating results..."
            ):

                reflection = reflect_recommendations(

                    user_input,

                    preferences,

                    recommendations
                )

            # =====================================
            # Save Session State
            # =====================================

            st.session_state.recommendations = (
                recommendations
            )

            st.session_state.preferences = (
                preferences
            )

            st.session_state.reflection = (
                reflection
            )

            st.session_state.searched = True

# =====================================
# Display Results
# =====================================

if (
    st.session_state.searched
    and st.session_state.recommendations
):

    recommendations = (
        st.session_state.recommendations
    )

    preferences = (
        st.session_state.preferences
    )

    reflection = (
        st.session_state.reflection
    )

    # =====================================
    # Planner Output
    # =====================================

    st.subheader("🧠 Planner Agent")

    st.json(preferences)

    # =====================================
    # Reflection Agent
    # =====================================

    st.subheader("🪞 Reflection Agent")

    st.info(reflection)

    # =====================================
    # Success Message
    # =====================================

    st.success(
        f"Found {len(recommendations)} recommendations."
    )

    # =====================================
    # Interactive Map
    # =====================================

    st.subheader("🗺 Nearby Places Map")

    m = folium.Map(
        location=[lat, lng],
        zoom_start=14
    )

    # =====================================
    # User Marker
    # =====================================

    folium.Marker(

        [lat, lng],

        popup="You are here",

        tooltip="Current Location",

        icon=folium.Icon(
            color="blue",
            icon="user"
        )

    ).add_to(m)

    # =====================================
    # Restaurant Markers
    # =====================================

    for idx, place in enumerate(recommendations):

        if place.get("location"):

            place_lat = (
                place["location"]["lat"]
            )

            place_lng = (
                place["location"]["lng"]
            )

            popup_text = f"""
            <b>{idx+1}. {place['name']}</b><br>
            Rating: {place.get('rating')}<br>
            Distance: {place.get('distance_text')}<br>
            Duration: {place.get('duration_text')}
            """

            folium.Marker(

                [place_lat, place_lng],

                popup=popup_text,

                tooltip=place["name"],

                icon=folium.Icon(
                    color="red",
                    icon="cutlery"
                )

            ).add_to(m)

    # =====================================
    # Render Map
    # =====================================

    st_folium(
        m,
        width=1000,
        height=500,
        returned_objects=[]
    )

    # =====================================
    # Final Recommendations
    # =====================================

    st.subheader(
        "🍽 Final Recommendations"
    )

    for idx, place in enumerate(recommendations):

        st.markdown(
            f"## {idx+1}. {place['name']}"
        )

        # =====================================
        # Restaurant Image
        # =====================================

        if place.get("photo_url"):

            st.image(
                place["photo_url"],
                width=350
            )

        # =====================================
        # Restaurant Info
        # =====================================

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"⭐ Rating: "
                f"{place.get('rating')}"
            )

            st.write(
                f"📍 Distance: "
                f"{place.get('distance_text')}"
            )

            st.write(
                f"⏱ Duration: "
                f"{place.get('duration_text')}"
            )

        with col2:

            st.write(
                f"🏠 Address: "
                f"{place.get('address')}"
            )

            st.write(
                f"🧠 Score: "
                f"{place.get('score')}"
            )

        # =====================================
        # Google Maps Link
        # =====================================

        if place.get("location"):

            lat_place = (
                place["location"]["lat"]
            )

            lng_place = (
                place["location"]["lng"]
            )

            maps_link = (
                "https://www.google.com/maps/search/?api=1"
                f"&query={lat_place},{lng_place}"
            )

            st.markdown(
                f"[📍 Open in Google Maps]({maps_link})"
            )

        st.divider()