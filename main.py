import os
from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class source(BaseModel):
    """schema for the source of the job posting"""

    url: str = Field(description="the url of the source")


class AgentResponse(BaseModel):
    """Schema for the response of the agent"""

    answer: str = Field(description="the agents answer to the query")
    sources: List[source] = Field(
        default_factory=list, description="the list of sources used to answer the query"
    )


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="search for 3 job posting for a software engineering intern in the San Francisco Bay Area on linkedin and list all of there details"
                )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
