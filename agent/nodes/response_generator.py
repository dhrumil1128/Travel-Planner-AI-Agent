# Generates a final response message for the user based on the current state and it in state .
 
from agent.state import AgentState

# Generates a final response message for the user based on the current state
def generate_response(state: AgentState) -> AgentState:
    if not state.suggested_destinations:
        state.final_response = "Sorry, I couldn't find any destinations matching your preferences. Could you give me more details?"
        return state

    if state.itinerary:
        destination = state.suggested_destinations[0]["name"]
        response = f"Here’s a travel plan for your trip to {destination}:\n\n"

        for day in state.itinerary:
            response += f"Day {day['day']}: {day['activity']}\n"
        
        state.final_response = response
        return state

    # If no itinerary yet, just suggest destinations
    if state.is_followup:
        response = "Here are some new options based on your updated preferences:\n"
    else:
        response = "Based on your preferences, I suggest the following destinations:\n"

    for dest in state.suggested_destinations:
        response += f"- {dest['name']} ({dest['region']})\n"

    state.final_response = response
    return state  # ✅ Make sure this is returned!
