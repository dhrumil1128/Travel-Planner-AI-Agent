# Travel Planner AI

Travel Planner AI is a personalized travel recommendation web application built with Streamlit and optionally extensible with FastAPI. Users input their travel preferences such as destination, travel style, budget, type of travel, and duration to generate custom destination suggestions. The app leverages the  AI Agent to intelligently refine recommendations and handle follow-up queries. It also includes Unsplash API integration for destination images and Google Maps for location insights. With the addition of real-time travel data from the Travel Advisor API, users can access suggestions for hotels, restaurants, and attractions. The app features a responsive UI, custom CSS styling, and animations. It can be deployed on Streamlit Cloud for easy access.

---

## Features

- City-based travel preference selection
- Start and end date input for travel duration
- Multiple travel styles (Beaches, Mountains, Nature, City Tours, etc.)
- Travel types including Solo, Couple, Family, and Friends
- Budget-friendly options including Budget, Moderate, Luxury, and Premium
- AI Agent handles user input and intelligently provides personalized responses and destination suggestions.
- Random destination image from Unsplash API
- Region-specific Google Maps location integration
- Responsive UI with custom CSS styling and animations
- Integrated with Travel Advisor API via RapidAPI
- Fully deployable on Streamlit Cloud

---

## Project Structure

```
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
│   │   ├── itinerary_creator.py
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
```

---

## Technologies Used

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | Streamlit          |
| Backend     | FastAPI (optional) |
| Image API   | Unsplash API       |
| Travel Data | Travel Advisor API (via RapidAPI) |
| Map Service | Google Maps URL API |
| Chatbot API | Gemin AI  API |


---

## API Reference

### Unsplash API
Used for fetching destination-based images dynamically.
- **Endpoint:** `https://api.unsplash.com/photos/random`
- **Method:** GET
- **Parameters:**
  - `query`: Destination or theme keyword
  - `client_id`: Your Unsplash API Access Key
  - `orientation`: landscape

### Travel Advisor API (via RapidAPI)
Used for fetching destination suggestions and travel data.
- **Base URL:** `https://travel-advisor.p.rapidapi.com`
- **Endpoints Used:**
  - `/locations/search`
  - `/hotels/list`
  - `/restaurants/list`
- **Authentication:** Requires RapidAPI key in headers

- **Base URL:**`http://geminai-agent.local (this is an example; replace with the actual URL if necessary)`
- **Endpoints Used:**
- `/process_input: Processes the user's travel preferences and queries.`
- `/get_suggestions: Retrieves personalized destination suggestions based on the processed input.`
- `/follow_up: Handles user follow-up queries and refines suggestions.`
- **Authentication:** Typically requires API key in the headers or authorization token for access.



---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/travel-planner-ai.git
cd travel-planner-ai
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the app:**
```bash
streamlit run Frontend/app.py
```

---

## Deployment

### Deploy on Streamlit Cloud

1. Push the repository to your GitHub account.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub and link your repository.
4. Select the repository and deploy.
5. Your app will be live with a public URL.

---

## Example Requirements.txt

```txt
streamlit
requests
fastapi
uvicorn
```

---

## Optional Streamlit Configuration (`.streamlit/config.toml`)

```toml
[theme]
base="dark"
primaryColor="#0052cc"
backgroundColor="#0f0f0f"
secondaryBackgroundColor="#1e1e1e"
textColor="#ffffff"
```

---

## Screenshots
## 1. Destination Finder 
![image](https://github.com/user-attachments/assets/6fc246eb-5b1d-4846-8a5c-9643cd87e3ad)
## 1. AI Travel Chat
![image](https://github.com/user-attachments/assets/0a242d74-4143-45f3-987d-f381d86e5304)



---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software with attribution.

---

## Acknowledgements

- [Unsplash API](https://unsplash.com/developers) for images
- [Streamlit](https://streamlit.io) for UI framework
- [FastAPI](https://fastapi.tiangolo.com) for backend API capabilities
- [Travel Advisor API](https://rapidapi.com/apidojo/api/travel-advisor) for travel data
- [Google Maps](https://developers.google.com/maps/documentation/urls/get-started) for location queries

---

## Author

**Dhrumil Pawar**  
[LinkedIn](https://www.linkedin.com/in/dhrumil-pawar/) 



