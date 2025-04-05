# This File defines the flow of our travel planning AI agent.
#Importing state management, agent state, and all functional nodes used to build the travel planning conversational flow.

from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes.preference_extractor import extract_preferences
from agent.nodes.destination_finder import find_destinations
from agent.nodes.itinerary_creator import create_itinerary
from agent.nodes.followup_handler import check_followup
from agent.nodes.response_generator import generate_response


def build_graph():
    graph = StateGraph(AgentState)

    # Add each node representing a stage of the travel planning pipeline
    graph.add_node("extract_preferences", extract_preferences)           # reads what the user wants (node-1)
    graph.add_node("find_destinations", find_destinations)            # suggests matching places (node-2)
    graph.add_node("check_followup", check_followup)                    # plans a 3-day trip (node-3) 
    graph.add_node("create_itinerary", create_itinerary)                # checks if user asked for changes (node-4)
    graph.add_node("generate_response", generate_response)              #  builds a response message (node - 5)

    # Set where the graph starts
    graph.set_entry_point("extract_preferences")

    # Define the path through each node
    graph.add_edge("extract_preferences", "find_destinations")
    graph.add_edge("find_destinations", "check_followup")
    graph.add_edge("check_followup", "create_itinerary")
    graph.add_edge("create_itinerary", "generate_response")
    graph.add_edge("generate_response", END)
    
    #return
    return graph.compile()
