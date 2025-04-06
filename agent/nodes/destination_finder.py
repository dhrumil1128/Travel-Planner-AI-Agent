# Importing the requests library for making HTTP requests.
import requests
from agent.state import AgentState

# This function finds travel destination suggestions based only on the preferred country or region.
def find_destinations(state: AgentState, api_key: str) -> AgentState:
    # Extract user preferences from state.
    preferences = state.preferences
    preferred_region = preferences.get("preferred_city", "")  # You can rename this key to 'preferred_region' if clearer

    # Ensure a region/country was provided
    if not preferred_region:
        print("Preferred region not provided in preferences.")
        state.suggested_destinations = []
        return state

    # Use the preferred region directly as the query
    query = preferred_region

    # Travel Advisor API endpoint
    url = "https://travel-advisor.p.rapidapi.com/locations/search"
    headers = {
        "X-RapidAPI-Key": api_key,  # Use the passed API key here
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"  # Host key
    }

    # Parameters for the API request
    params = {
        "query": query,
        "limit": "15",              # Increased to get more data to filter from
        "currency": "USD",   
        "lang": "en_US"
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Log raw response data for debugging
        print("API RAW DATA:\n", data)

        # Extract destination results from response
        results = data.get("data", [])
        suggestions = []

        for place in results:
            print("Raw entry:", place)

            result = place.get("result_object")
            if not result:
                print("no result_object")
                continue

            name = result.get("name")
            location = result.get("location_string", "")
            lat = result.get("latitude")
            lon = result.get("longitude")

            # Filter strictly by country/region match
            if name and lat and lon and preferred_region.lower() in location.lower():
                suggestion = {
                    "name": name,
                    "region": location or "Unknown",
                    "latitude": lat,
                    "longitude": lon
                }
                print(" Added suggestion:", suggestion)
                suggestions.append(suggestion)
            else:
                print("or missing info")

        # Update the state with the collected destination suggestions
        state.suggested_destinations = suggestions
        if not suggestions:
            print(" No destinations extracted after processing.")
        return state

    except Exception as e:
        # Handle any errors during the API call
        print("API error:", e)
        state.suggested_destinations = []
        return state
