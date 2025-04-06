# Travel Assistant AI – Project Documentation

## Project Structure

```
travel-assistant-ai/
│
├── main.py                            # FastAPI entry point with CORS setup
├── agent/
│   ├── state.py                       # Agent state definition (holds user data and flow context)
│   └── nodes/
│       ├── preference_extractor.py   # Extracts user preferences (e.g., interest, region)
│       ├── destination_finder.py     # Finds travel destinations using external API
│       ├── itinerary_creator.py      # Builds travel itineraries based on destination
│       ├── followup_handler.py       # Handles user follow-up input
│       └── response_generator.py     # Generates final responses for the user
└── README.md                         # Project overview and instructions
```

---

## Project Overview

**Travel Assistant AI** is an intelligent travel planning assistant built with FastAPI and LangGraph. It interacts with users to:
- Understand their travel preferences,
- Suggest relevant destinations,
- Generate personalized itineraries,
- Handle follow-up questions,
- And respond in natural language.

### Key Features

- Conversational and context-aware interaction.
- Destination recommendations powered by RapidAPI’s Travel Advisor.
- Modular node-based architecture using LangGraph.
- Extendable state management using `AgentState`.
- Supports follow-up queries and dynamic conversation branching.

---

## Core Modules Explained

### 1. `main.py`

- Initializes the FastAPI application.
- Adds **CORS middleware** to allow frontend/backend communication.
- Loads and defines the LangGraph-powered flow (preference → destination → itinerary → response).

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 2. `agent/state.py`

Defines the `AgentState` class which maintains:
- User messages
- Extracted preferences
- Suggested destinations
- Generated itinerary
- Follow-up status

This shared state enables smooth transitions between nodes in a conversation.

---

### 3. `agent/nodes/`

Each file is a **node in the LangGraph**, processing and modifying the shared state.

#### `preference_extractor.py`
- Uses NLP to extract user interests and preferred regions.

#### `destination_finder.py`
- Sends a request to Travel Advisor API.
- Extracts and logs destination suggestions.
- Returns a list of destination objects with name, location, and coordinates.

####  `itinerary_creator.py`
- Creates a simple mock itinerary for selected destinations.
- Could be enhanced with dates, activities, etc.

#### `followup_handler.py`
- Checks if the user input is a follow-up or clarification.
- Branches flow accordingly.

#### `response_generator.py`
- Finalizes the conversation by crafting a user-friendly reply from the state data.

---

## External APIs

**Travel Advisor by RapidAPI**
- Endpoint: `https://travel-advisor.p.rapidapi.com/locations/search`
- Auth: Uses headers with `X-RapidAPI-Key`
- Query: Based on extracted `interest` and `region`

Make sure to secure and rotate your API keys in production environments.

---

## How It Works

1. **User sends a message**: "I want to visit mountains in Europe."
2. **Preferences are extracted**: `{interest: "mountains", region: "Europe"}`
3. **Destinations are fetched**: Top 5 places matching that interest.
4. **Itinerary is built**: Sample trip plan.
5. **Final response generated**: "Based on your interest in mountains in Europe, here’s a plan..."

---

## 📌 Installation & Setup

### 🔧 Requirements

- Python 3.9+
- FastAPI
- LangGraph
- `requests`

### 📦 Install dependencies

```bash
pip install fastapi uvicorn langgraph requests
```

### ▶️ Run the app

```bash
uvicorn main:app --reload
```

---

## 🧪 Example API Usage

### POST `/chat`

```json
{
  "messages": [
    {"role": "user", "content": "I want to visit beaches in Asia"}
  ]
}
```

### Response

```json
{
  "messages": [
    {"role": "assistant", "content": "Based on your interest in beaches in Asia, here are some great places..."}
  ]
}
```

---

## Extending the Project

- Add **authentication** and session management.
- Replace mock itinerary logic with real itinerary planning (e.g., flights, hotels).
- Use **OpenAI** or **LlamaIndex** for advanced preference extraction.
- Add frontend with React, Svelte, or Next.js.

---

## Security Notes

- Never hardcode your RapidAPI key.
- Use `.env` or a secure config store.
- Sanitize and validate user input to prevent misuse.

---

##  Questions or Contributions?

Feel free to contribute via pull requests or open issues!


