# Main Frontend UI Page : 
# Import libraries
import streamlit as st
import requests
import datetime

# --------------------- AgentState class ---------------------
class AgentState:
    def __init__(self, preferences=None):
        self.preferences = preferences or {}
        self.suggested_destinations = []

# --------------------- Destination Finder ---------------------
def find_destinations(state: AgentState) -> AgentState:
    preferences = state.preferences
    preferred_region = preferences.get("preferred_city", "")

    if not preferred_region:
        print("Preferred region not provided in preferences.")
        state.suggested_destinations = []
        return state

    query = preferred_region

    url = "https://travel-advisor.p.rapidapi.com/locations/search"
    headers = {
        "X-RapidAPI-Key": "56531449a5msha6825acbcb0c4d7p183678jsn99ace807947d",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    params = {
        "query": query,
        "limit": "15",
        "currency": "USD",
        "lang": "en_US"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        results = data.get("data", [])
        suggestions = []

        for place in results:
            result = place.get("result_object")
            if not result:
                continue

            name = result.get("name")
            location = result.get("location_string", "")
            lat = result.get("latitude")
            lon = result.get("longitude")

            if name and lat and lon and preferred_region.lower() in location.lower():
                suggestion = {
                    "name": name,
                    "region": location or "Unknown",
                    "latitude": lat,
                    "longitude": lon
                }
                suggestions.append(suggestion)

        state.suggested_destinations = suggestions
        return state

    except Exception as e:
        print("API error:", e)
        state.suggested_destinations = []
        return state

# --------------------- Streamlit UI ---------------------
st.set_page_config(page_title="Travel Planner AI", layout="wide")
UNSPLASH_ACCESS_KEY = "7_EKtKVpcR4ObamVZ2rlihklzXBPHBPjqNbPQl06qMI"

# CSS Styling
st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        background-color: #0f0f0f !important;
        color: #0f0f0f !important;
        border: none;
        padding: 1rem;
    }
    section[data-testid="stSidebar"] h2 {
        color: white !important;
    }
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] .stSelectbox label, 
    section[data-testid="stSidebar"] .stDateInput label {
        color: white !important;
    }
    .destination-card {
        border-radius: 12px;
        padding: 1rem;
        background-color: #1e1e1e;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    .destination-card:hover {
        background-color: #333333;
        transform: translateY(-5px);
    }
    .map-button {
        background-color: #111111;
        color: #ffffff;
        padding: 8px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        display: inline-block;
        box-shadow: 0px 4px 12px rgba(0, 82, 204, 0.5);
    }
    .map-button:hover {
        background-color: #00bfff;
        box-shadow: 0 0 12px 2px rgba(0, 191, 255, 0.7);
        color: white;
    }
    .find-button {
        background-color: #0052cc;
        color: white;
        font-weight: bold;
        padding: 10px 18px;
        border-radius: 10px;
        margin-top: 10px;
        transition: 0.3s ease;
    }
    .find-button:hover {
        background-color: #007bff;
        color: #ffffff;
        box-shadow: 0 0 8px rgba(0,123,255,0.5);
    }
    img {
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    .center-message {
        text-align: center;
        font-size: 18px;
        padding: 50px 0;
    }
</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
    <h1 style='text-align: center; color: white; font-size: 3em;'>🧳 Travel Planner AI</h1>
    <h4 style='text-align: center; color: #cccccc;'>Your Smart Companion for Personalized Trip Ideas</h4>
""", unsafe_allow_html=True)

# SIDEBAR FORM
st.sidebar.header("🧭 Travel Preferences")

city = st.sidebar.text_input("🌇️ Preferred City", placeholder="e.g. Paris")
start_date = st.sidebar.date_input("🗕️ Start Date", datetime.date.today())
end_date = st.sidebar.date_input("🗕️ End Date", datetime.date.today() + datetime.timedelta(days=3))

interest = st.sidebar.selectbox(
    "🌍 Travel Style",
    ["", "Beaches", "Mountains", "City Tours", "Nature Escapes", "Historical Places", "Luxury Resorts"],
    index=0,
    format_func=lambda x: "Select your travel style" if x == "" else x
)

budget = st.sidebar.selectbox(
    "💰 Budget",
    ["", "Budget", "Moderate", "Luxury", "Ultra Luxury", "Backpacker", "Mid-range"],
    index=0,
    format_func=lambda x: "Select your budget" if x == "" else x
)

travel_type = st.sidebar.selectbox(
    "🧳 Travel Type",
    ["", "Solo", "Couple", "Family", "Friends", "Group Tours"],
    index=0,
    format_func=lambda x: "Select travel type" if x == "" else x
)

show_result = st.sidebar.button("🔎 Find Destinations", key="find_button")

# Fetch an image from Unsplash
def get_image_url(destination_name):
    url = f"https://api.unsplash.com/photos/random?query={destination_name}&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["urls"]["regular"]
    return None

# MAIN RESULT PAGE
if show_result:
    if not all([city, interest, budget, travel_type]):
        st.warning("⚠️ Please fill in all travel preferences to continue.")
    else:
        # Get destination suggestions
        state = AgentState(preferences={"preferred_city": city})
        updated_state = find_destinations(state)

        st.markdown("### 📍 Suggested Destinations")
        if not updated_state.suggested_destinations:
            st.warning("No suggestions found for the selected city.")
        else:
            cols = st.columns(5)
            for i, dest in enumerate(updated_state.suggested_destinations):
                with cols[i % 5]:
                    st.markdown('<div class="destination-card">', unsafe_allow_html=True)
                    st.subheader(dest["name"])
                    image_url = get_image_url(dest["name"])
                    if image_url:
                        st.image(image_url, use_container_width=True)
                    st.markdown(f"**Region:** {dest['region']}")
                    map_query = dest["region"].replace(" ", "+")
                    map_url = f"https://www.google.com/maps/search/?api=1&query={map_query}"
                    st.markdown(f'<a href="{map_url}" target="_blank" class="map-button">📍 View Location</a>', unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 🗓️ Suggested Itinerary")
        trip_days = (end_date - start_date).days + 1
        for day in range(1, trip_days + 1):
            st.markdown(f"- 🗖️ **Day {day}**: Explore attractions, local food, and hidden gems in {city}")

        st.markdown("### 🎉 Events & Highlights")
        st.info("""
        - 🎭 Cultural shows & street festivals  
        - 🍷 Wine & food tastings  
        - 🎨 Local crafts markets  
        - 🎶 Evening beach DJ nights  
        """)
else:
    st.markdown("<div class='center-message'>🕵️‍♂️ Fill out your preferences in the sidebar and hit <b>'Find Destinations'</b> to see personalized results!</div>", unsafe_allow_html=True)
