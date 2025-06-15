from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel, set_tracing_disabled
import os

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
  api_key=os.getenv("GEMINI_API_KEY")
)

model = OpenAIChatCompletionsModel(
    model ="gemini-2.0-flash-exp",
    openai_client= provider
)

# web developer
web_dev = Agent(
    name="Web Developer",
    instructions="Build responsive and performant website usig latest framworks",
    model = model,
    handoff_description="handoff to web developer if the task related to it"
)

# app developer
app_dev = Agent(
    name = "App Developer",
    instructions= "Develop Cross-platform mobile apps for Android and iOS",
    model=model,
    handoff_description="handoff to App Developer if the task related to it"
)

# marketing agent
marketing = Agent(
    name="Marketing Agent",
    instructions="Craete and Execute marketing strategies for product Launches",
    model= model,
    handoff_description="handoff to Marketing Agent if the task related to it"
) 

async def my_agent(user_input):
    manager =Agent(
        name="Manager",
        instructions="You will chats with the user and delegate the task to specialized agent based on their request",
        model= model,
        handoff_description=[web_dev,app_dev,marketing]
    )

    reponse = await Runner.run(
    manager,
    input=user_input
)
    
    return reponse.final_output