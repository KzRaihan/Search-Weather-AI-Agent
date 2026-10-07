# ==========================================
# IMPORTS
# ==========================================

import os
import requests
import certifi

import streamlit as st

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch


# ==========================================
# ENVIRONMENT CONFIGURATION
# ==========================================

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")


# ==========================================
# STREAMLIT PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic AI Assistant")
st.caption("Search + Weather AI Agent powered by LangChain")


# ==========================================
# TOOLS
# ==========================================

# Tavily web search tool
search_tool = TavilySearch(
    max_results=3
)


@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    if not WEATHERSTACK_API_KEY:
        return "Weather service is not configured."

    url = "http://api.weatherstack.com/current"

    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if "current" not in data:
            error_info = data.get("error", {})
            return (
                "Could not fetch weather data. "
                f"{error_info.get('info', 'Unknown API error')}"
            )

        current = data["current"]

        return (
            f"City: {city}\n"
            f"Temperature: {current.get('temperature')}°C\n"
            f"Weather: "
            f"{current.get('weather_descriptions', ['Unknown'])[0]}\n"
            f"Humidity: {current.get('humidity')}%"
        )

    except requests.RequestException as e:
        return f"Weather request failed: {str(e)}"


# Register all tools
tools = [
    search_tool,
    get_weather_data
]


# ==========================================
# LLM
# ==========================================

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.1
)


# ==========================================
# AGENT
# ==========================================

system_prompt = """
You are a helpful and reliable AI assistant.

Follow these rules:

1. Answer general knowledge questions directly when no external
   information is required.

2. Use the Tavily search tool when the user asks for current,
   recent, live, or web-based information.

3. Use the weather tool when the user asks about current weather
   conditions for a specific city.

4. Use multiple tools when the user's request requires information
   from multiple sources.

5. Do not use a tool unnecessarily.

6. Base your response on the information returned by the tools.

7. If a tool fails, clearly explain the problem instead of
   inventing information.

8. Provide a concise and accurate final answer.
"""

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)


# ==========================================
# USER INPUT
# ==========================================

user_query = st.text_input(
    "Enter your query:",
    placeholder=(
        "Example: Find the capital of India "
        "and the current weather in Delhi"
    )
)


# ==========================================
# RUN AGENT
# ==========================================

if st.button("Run Agent", type="primary"):

    if not user_query.strip():
        st.warning("Please enter a query.")

    else:

        with st.spinner("Agent is working..."):

            try:

                response = agent.invoke({
                    "messages": [
                        {
                            "role": "user",
                            "content": user_query
                        }
                    ]
                })

                # ==========================================
                # TOOL EXECUTION TRACE
                # ==========================================

                tool_used = False

                for message in response["messages"]:

                    if (
                        hasattr(message, "tool_calls")
                        and message.tool_calls
                    ):
                        tool_used = True

                        for tool_call in message.tool_calls:

                            st.info(
                                f"🔧 **Tool Used:** "
                                f"{tool_call['name']}\n\n"
                                f"**Arguments:** "
                                f"{tool_call['args']}"
                            )

                if not tool_used:
                    st.caption("ℹ️ No external tool was required.")

                # ==========================================
                # FINAL RESPONSE
                # ==========================================

                st.success("Response Generated")

                st.markdown("### Final Response")

                st.write(
                    response["messages"][-1].content
                )

            except Exception as e:

                st.error(
                    f"Agent execution failed: {str(e)}"
                )
# for run this 
# use-> streamlit run app.py