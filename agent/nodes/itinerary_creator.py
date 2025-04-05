# Create a basic 3-day trip plan itinerary for that place(Destination) and add it in sate.

from agent.state import AgentState
def create_itinerary(state: AgentState) -> AgentState:
    if not state.suggested_destinations:
        return state  # Nothing to plan

    destination = state.suggested_destinations[0]  # Pick the top one

    # Simple Basic 3-day itinerary
    itinerary = [
        {"day": 1, "activity": f"Explore local attractions in {destination['name']}"},
        {"day": 2, "activity": f"Visit famous landmarks of {destination['name']}"},
        {"day": 3, "activity": f"Relax and enjoy local food in {destination['name']}"},
    ]

    # Save it to state
    state.itinerary = itinerary
    return state
