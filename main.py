import os

from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(llm, tools)  # Creates an agent graph

chain = agent


def main():
    result = chain.invoke(
        {
            "messages": [("user", "find me 3 of the newest software engineering internships positions in the United States, you can only use twitter to find the information")]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
