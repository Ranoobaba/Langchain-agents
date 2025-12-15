import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    information = """
    Zia Mohyeddin was born in Lyallpur, Punjab, British India (now Faisalabad, Pakistan) to a Punjabi family originally from Rohtak, Punjab, British India (now in Haryana, India).[5] His father, Khadim Mohyeddin, was a mathematician, musicologist, playwright, and lyricist associated with various theatre groups.[6]

Zia spent his early life in Lahore. He was trained at the Royal Academy of Dramatic Art in London from 1953 to 1955. After stage roles in Long Day's Journey into Night[4] and Julius Caesar,[7] he made his West End debut as Dr. Aziz in A Passage to India[8] on 20 April 1960 at the Comedy Theatre.[9] The production continued for 302 performances. He reprised this role in the 1965 BBC television adaptation as well. He made his film debut in Lawrence of Arabia (1962), playing the role of Tafas (the Arab guide who is shot by Omar Sharif for drinking water from the wrong well).[8] He then made numerous TV and film appearances. As an actor, he worked for nearly 47 years in the United Kingdom.[3]

His first wife was Sarwar Zemani with whom he had two sons,[8] Minos Ameer and Risha Ameen.[10]
    """


    summary_template = """
given the following information {information} I want you to create:
1. A short summary 
2. two interesting facts about the person
"""

    summary_prompt_template = ChatPromptTemplate.from_template(summary_template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
