Travel Planner AI
Travel Planner AI is a personalized travel recommendation web application designed to provide users with tailored travel suggestions based on their preferences. The platform is built with Streamlit for the frontend and FastAPI for optional backend extensibility. This app allows users to input their travel preferences such as city, travel style, budget, type of travel, and duration to generate custom destination suggestions, itineraries, and visual highlights.

New Features:

Gemin AI Agent: A core component of the platform that processes user input and provides personalized responses, enabling intelligent and dynamic travel suggestions.

Enhanced Destination Finder: Fetches travel destination data from the Travel Advisor API and uses Unsplash API for destination images.

Google Maps Integration: Links destinations to Google Maps for easy navigation.

Features
1. Personalized Travel Recommendations
Input city, travel style, budget, travel type, and duration to receive personalized destination suggestions.

Travel style options such as:

Beaches

Mountains

City Tours

Nature Escapes

Historical Places

2. Travel Preferences
City Selection: Users can input their preferred city for travel.

Start and End Dates: Select your travel dates.

Interest & Style: Choose the travel style based on personal preferences.

Budget: Select between Budget, Moderate, Luxury, and Premium budgets.

Travel Type: Choose the type of travel (Solo, Couple, Family, Friends).

3. AI-Powered Travel Assistant (Gemin AI Agent)
The Gemin AI Agent is integrated to enhance user interaction. The agent processes user input, generates personalized travel suggestions, responds dynamically to follow-up queries, and adapts to user preferences over time.

4. Destination Finder
Destination Suggestions: Provides tailored recommendations based on the user’s preferences using the Travel Advisor API.

Random Destination Image: Fetches beautiful destination images from Unsplash API.

Google Maps Integration: Each suggested destination has a link to view it on Google Maps for easy navigation.

5. Unsplash Image Integration
Fetches high-quality, destination-based images to enrich the user experience.

6. Google Maps Integration
Provides quick links to Google Maps for each destination for convenient access.

7. FastAPI Integration (Optional)
FastAPI is optionally integrated for the backend to handle complex API requests and ensure future scalability.

8. Fully Deployable
The app can be easily deployed on Streamlit Cloud and accessed via a public URL.

Gemin AI Agent
The Gemin AI Agent is the heart of the system that intelligently handles user interactions. It processes user input (city, travel style, etc.) and uses an internal algorithm to generate dynamic and personalized travel suggestions. It also responds to follow-up queries and adapts to user feedback to continuously refine the travel recommendations.

Key Features of Gemin AI Agent:
Personalization: Adjusts responses based on user preferences.

Dynamic Response Generation: Reacts to queries in real-time, ensuring a conversational and seamless interaction.

State Management: Tracks user inputs and maintains context across interactions.

The Gemin AI Agent makes the travel planning experience intuitive, engaging, and highly personalized.

Technologies Used
Layer	Technology
Frontend	Streamlit
Backend	FastAPI (optional)
Image API	Unsplash API
Travel Data	Travel Advisor API (via RapidAPI)
Map Service	Google Maps URL API
AI Engine	Gemin AI Agent
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
API Reference
Unsplash API
Used for fetching destination-based images dynamically.

Endpoint: https://api.unsplash.com/photos/random

Method: GET

Parameters:

query: Destination or theme keyword (e.g., city, landscape).

client_id: Your Unsplash API Access Key.

orientation: landscape (to fetch landscape-oriented images).

Travel Advisor API (via RapidAPI)
Used for fetching destination data, suggestions, hotels, and restaurants.

Base URL: https://travel-advisor.p.rapidapi.com

Endpoints Used:

/locations/search: Fetches destination suggestions based on user input.

/hotels/list: Returns hotels in the specified destination.

/restaurants/list: Returns restaurant suggestions in the area.

Authentication: Requires a RapidAPI key in the request headers.

Google Maps URL API
Provides quick access links for the destinations on Google Maps.

Base URL: https://www.google.com/maps/search/?api=1&query=

Parameters:

query: The destination or location to search in Google Maps.

Installation
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/dhrumil1128/Travel-Planner-AI-Agent.git
cd Travel-Planner-AI-Agent
Step 2: Create a Virtual Environment
(Optional but recommended for managing dependencies.)

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Step 3: Install Dependencies
Install the required dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the Application
Run the app with Streamlit:

bash
Copy
Edit
streamlit run Frontend/app.py
The app will be available at http://localhost:8501 by default.

Deployment
Deploy on Streamlit Cloud
Push your repository to GitHub.

Visit Streamlit Cloud.

Sign in with your GitHub account and link the repository.

Select the repository and click Deploy.

Your app will be live on a public URL.

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
Unsplash API for providing images.

Streamlit for building the UI framework.

FastAPI for enabling the backend API.

Travel Advisor API for offering travel data.

Google Maps for location queries.

Author
Dhrumil Pawar
LinkedIn
