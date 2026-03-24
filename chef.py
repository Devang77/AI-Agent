from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from typing import Dict,Any
from dotenv import load_dotenv
import base64

load_dotenv()

tavily_client = TavilyClient()

@tool
def web_search(query:str)-> Dict[str,Any]:
    """Search the web for information"""
    return tavily_client.search(query)

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_base64 = encode_image("fridge.jpg")
system_prompt="""
You are a personal chef assistant.

The user will provide an image of their fridge.

Follow these STRICT steps:

Step 1: Identify ingredients
- Carefully analyze the image.
- List ONLY ingredients that are clearly visible.
- Do NOT guess or assume items.
- If unsure, label as "uncertain".

Step 2: Decide if web search is needed
- If you already know simple recipes, you may answer directly.
- Otherwise, use the web_search tool to find recipes.

Step 3: Suggest recipes
- Suggest 2-3 recipes using ONLY the identified ingredients.
- Do NOT include ingredients not seen in the image (except basic salt, oil, water).
- Keep recipes simple and realistic.

Output format:
1. Ingredients detected
2. Recipes
"""
agent = create_agent(
    model = "gpt-4o-mini",
    tools = [web_search],
    system_prompt= system_prompt
)
response = agent.invoke({"messages":[HumanMessage(content=[
            {"type": "text", "text": "What recipes can I make with these ingredients?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ])]})

print(response['messages'][-1].content)