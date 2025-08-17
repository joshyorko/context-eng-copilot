from langchain_sema4 import ActionServerToolkit
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig

from dotenv import load_dotenv
import os

# Load in the environment variables
load_dotenv()
model_choice = os.environ.get("MODEL_CHOICE")
email = os.environ.get("EMAIL")

# Initialize the tool manager and fetch tools

# Initialize Action Server Toolkit
toolkit = ActionServerToolkit(url="https://home-lab-actions.yorko.io", report_trace=True)
sema4ai_tools = toolkit.get_tools()

# Create a language model instance and bind it with the tools
model_ollama = ChatOllama(model="qwen2.5:3b", base_url="http://192.168.1.112:11434/", temperature=0)
model_with_tools = model_ollama.bind_tools(sema4ai_tools)


# Initialize the prebuilt tool node
tool_node = ToolNode(sema4ai_tools)



#### Workflow ####


# Function to invoke the model and get a response
async def call_agent(state: MessagesState, writer):
    messages = state["messages"]
    
    # Stream tokens using astream
    full_content = ""
    tool_calls = []
    
    async for chunk in model_with_tools.astream(messages):
        # Stream content tokens
        if chunk.content:
            writer(chunk.content)
            full_content += chunk.content
        
        # Accumulate tool calls
        if hasattr(chunk, 'tool_calls') and chunk.tool_calls:
            # Filter out tool calls with empty name attribute
            valid_tool_calls = [tc for tc in chunk.tool_calls if tc.get("name", "").strip()]
            tool_calls.extend(valid_tool_calls)
    
    # Create the full response message with accumulated content and tool calls
    response = AIMessage(content=full_content, tool_calls=tool_calls)
    
    # Return the updated message history
    return {"messages": [response]}


# Function to determine the next step in the workflow based on the last message
def should_continue(state: MessagesState):
    if state["messages"][-1].tool_calls:
        # No authorization logic, just proceed to tool execution
        return "tools"
    return END  # End the workflow if no tool calls are present


# Builds the LangGraph workflow with memory
def build_graph():
    # Build the workflow graph using StateGraph
    workflow = StateGraph(MessagesState)

    # Add nodes (steps) to the graph
    workflow.add_node("agent", call_agent)
    workflow.add_node("tools", tool_node)

    # Define the edges and control flow between nodes
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")

    # Set up memory for checkpointing the state
    memory = MemorySaver()

    # Compile the graph with the checkpointer
    graph = workflow.compile(checkpointer=memory)
    return graph


async def main():
    graph = build_graph()
    
    # Define the input messages from the user
    inputs = {
        "messages": [
            {
                "role": "user",
                "content": input("Enter your query for the agent: ")  # Prompt user for input,
            }
        ],
    }

    # Configuration with thread and user IDs for authorization purposes
    config = {"configurable": {"thread_id": "4", "user_id": email}}

    # Run the graph and stream the outputs
    async for chunk in graph.astream(inputs, config=config, stream_mode="values"):
        # Pretty-print the last message in the chunk
        chunk["messages"][-1].pretty_print()
        

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())