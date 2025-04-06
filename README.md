Travel Planner AI
Travel Planner AI is a web application built with Streamlit to provide personalized travel recommendations. It enables users to input their travel preferences such as city, travel style, budget, travel type, and duration, which the system then uses to generate custom travel suggestions. The app is also optionally extensible with FastAPI for future backend enhancements.

Key Features
1. Personalized Travel Recommendations
City-based travel preferences: Users can input a specific city or region to get destination suggestions.

Multiple travel styles: Choose from Beaches, Mountains, Nature, City Tours, and more.

Travel types: Solo, Couple, Family, and Friends.

Budget Options: Budget, Moderate, Luxury, and Premium options available.

2. Gemin AI Agent
Gemin AI Agent handles user input and intelligently provides personalized responses and destination suggestions.

It processes travel-related queries and adapts over time, improving the recommendations based on user interaction.

Provides a dynamic conversation flow, allowing users to ask follow-up questions for further details.

3. Destination Finder
Travel Advisor API is used to fetch destination data based on user preferences.

Suggestions are filtered and presented with essential details such as location, name, and geographical coordinates (latitude/longitude).

Includes links to Google Maps for each suggested destination for easy navigation.

4. Random Destination Images
Unsplash API is integrated to provide random images for each destination to enhance the user experience visually.

5. Travel Style Selection
Users can select from various travel styles to tailor their recommendations to their interests:

Nature

Mountains

Beaches

City Tours

And more...

6. Travel Duration
Duration selection: Users can input start and end dates, which helps in suggesting suitable travel destinations and activities.

7. Responsive User Interface
Built with Streamlit, the application features a responsive and user-friendly UI.

The design includes custom CSS styling and animations for a smooth user experience.

Project Structure
markdown
Copy
Edit
travel-planner-ai/
│
├── agent/
│   ├── __init__.py
│   ├── graph.py
│   ├── state.py
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── destination_finder.py
│   │   ├── followup_handler.py
│   │   ├── preference_extractor.py
│   │   └── response_generator.py
│   └── tools/
│       ├── __init__.py
│       ├── graph.py
│       ├── state.py
│       └── destination_db.py
│
├── data/
│   └── destinations.json
│
├── Frontend/
│   └── app.py
│
├── tests/
│   └── test_agent.py
│
├── main.py
├── README.md
└── requirements.txt
Technologies Used
Layer	Technology
Frontend	Streamlit
Backend	FastAPI (optional)
Image API	Unsplash API
Travel Data	Travel Advisor API
Maps Service	Google Maps URL API
API Reference
Unsplash API
Used to fetch random images for destinations.

Endpoint: https://api.unsplash.com/photos/random

Method: GET

Parameters:

query: Destination or theme keyword (e.g., Paris, Beach)

client_id: Your Unsplash API Access Key

orientation: landscape

Travel Advisor API (via RapidAPI)
Used to fetch travel destinations and related data.

Base URL: https://travel-advisor.p.rapidapi.com

Endpoints:

/locations/search: For destination suggestions based on user input.

/hotels/list: To fetch available hotels.

/restaurants/list: To fetch restaurant recommendations.

Authentication: Requires RapidAPI Key in headers.

Installation
Step 1: Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/travel-planner-ai.git
cd travel-planner-ai
Step 2: Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Step 3: Install the required dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the application
bash
Copy
Edit
streamlit run Frontend/app.py
Deployment
Deploy on Streamlit Cloud
Push the repository to your GitHub account.

Visit Streamlit Cloud.

Sign in with GitHub and link your repository.

Select the repository and deploy it.

Your app will be live with a public URL.

Requirements.txt
txt
Copy
Edit
streamlit
requests
fastapi
uvicorn
Optional Streamlit Configuration (.streamlit/config.toml)
toml
Copy
Edit
[theme]
base="dark"
primaryColor="#0052cc"
backgroundColor="#0f0f0f"
secondaryBackgroundColor="#1e1e1e"
textColor="#ffffff"
Screenshots


License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software with attribution.

Acknowledgements
Unsplash API for providing travel-related images: Unsplash API

Streamlit for building the web interface: Streamlit

FastAPI for backend API capabilities: FastAPI

Travel Advisor API for fetching travel data: Travel Advisor API

Google Maps for location queries: Google Maps

Author
Dhrumil Pawar
LinkedIn

