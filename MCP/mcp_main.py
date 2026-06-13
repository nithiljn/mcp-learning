from langchain_groq import ChatGroq 
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import os 
from dotenv import load_dotenv
load_dotenv()
import asyncio

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm_model = ChatGroq(model = "qwen/qwen3-32b" )

async def main():
    client  = MultiServerMCPClient(
       {
           "math":{
               "command":"python",
               "args":["/Users/apple/Documents/Learning/MCP/math.py"],
               "transport":"stdio"
           },
           "weather":{
               "url":"http://127.0.0.1:8000/mcp",
               "transport":"streamable_http"
           }
       }
    )
        
    tools =await client.get_tools()
    agent = create_agent(
          model = llm_model,
          tools=tools
    )
    config ={"configurable":{"thread_id":"test_1"}}
    res= await agent.ainvoke({"messages":"what is 33+31"},config=config)
    print(res["messages"][-1].content)
    result = await agent.ainvoke({"messages": "what is weather in chennai?"}, config=config)
    print(result["messages"][-1].content)
    
if __name__ == "__main__":
    asyncio.run(main())


