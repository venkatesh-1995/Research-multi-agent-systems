from src.agents.agents import search_agent,read_agent,writer_chain,critic_chain

def research_pipeline(topic:str) ->dict:
    
    state={}
    
    # Step 1: Search for information
    print("\n"+"="*20)
    print("Step 1: Searching agent is working...")
    print("="*20)
    
    search_agent_info=search_agent()
    search_result = search_agent_info.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"Find recent, reliable and detailed information on the topic: {topic}"
            }
        ]
    }
)

    state["search_result"] = search_result["messages"][-1].content

    print("\nsearch result:\n",state["search_result"])
    
    # Step 2: Read and extract information
    
    
    print("\n"+"="*20)
    print("Step 2: read agent is working...")
    print("="*20)
    
    read_agent_extract=read_agent()
    reader_result = read_agent_extract.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Based on the search results about the topic: {topic}

Pick the most relevant URL and scrape its deeper content.

Search Result:
{state['search_result']}
"""
            }
        ]
    }
)

    state["reader_result"] = reader_result["messages"][-1].content

    print("\nreader result:\n", state["reader_result"])
    
    
    
#step 3 - writer chain 


    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)
    
    research_combined=f"""
        Search Result:{state['search_result']}
        reader scaped content:{state['reader_result']}
        """
    
    
    state["report"] =writer_chain.invoke({
        "topic":topic,
        "research_combined":research_combined
  }  )


    print("\n final report",state["report"])
    
    
    
    #critic report 

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)
    
    state["feedback"]=critic_chain.invoke({
        "report": state["report"]
    })
    
    print("\n critic report:",state["feedback"])
    
    return state
