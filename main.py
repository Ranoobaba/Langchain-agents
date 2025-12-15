from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

import os

load_dotenv()





llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    result =agent.invoke({"messages": [HumanMessage(content="search for 3 job posting for a software engineering intern in the San Francisco Bay Area on linkedin and list all of there details")]})
    print(result)


if __name__ == "__main__":
    main()
