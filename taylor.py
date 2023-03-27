from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain_prefect.plugins import RecordLLMCalls

from prefect import flow
from prefect.blocks.system import Secret

import os

#Needed Secrets Blocks
openai_api_key_block = Secret.load("open-ai-api-key")
openai_api_key = openai_api_key_block.get()

google_cse_id_block = Secret.load("tswift-cse-id")
google_cse_id = google_cse_id_block.get()

google_api_key_block = Secret.load("cse-api-key")
google_api_key = google_api_key_block.get()

#Open AI and Langchain configuration
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
tools = load_tools(
    ["google-search"], 
    llm=llm, 
    google_api_key=google_api_key, 
    google_cse_id=google_cse_id
)
agent = initialize_agent(tools, llm)

@flow
def my_flow():
    agent.run(
        "What are Taylor Swift's Top 10 songs"
        "Randomize these songs into a list"
    )

with RecordLLMCalls(tags={"agent"}):
    my_flow()