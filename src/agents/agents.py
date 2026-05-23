from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search,scrape_url
from dotenv import load_dotenv
import os

load_dotenv()


llm=ChatOpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="gpt-4o-mini",
    temperature=0.3,    
    
)

# 1st agent: search agent
def search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="You are a helpful research assistant. Use the tools to gather information and answer the user's query."
    )
    

def read_agent():

    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt="""
        You are a helpful research assistant.

        Use the scrape_url tool to read webpage content
        and answer the user's query accurately.
        """
    )    


# Writer  chain 

writer_prompt=ChatPromptTemplate.from_messages(
    [("system", "You are an Expert research writer, write clear, structured and insightful reports;"),
     ("human", """write a detailed research report on the topic below
Topic:{topic}
Research gathered:{research_combined}
Structure the report as:
1. Introduction
2. key findings(minimum 3 well-explained points
3.Conclusion
4.Sources(list all URL's found in the research
                  
                  
be detailed,factual and Professional,""")])


writer_chain=writer_prompt | llm | StrOutputParser()


#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()