from multi_agents import my_agent
import chainlit as cl
import asyncio
@cl.on_chat_start
async def on_chat_start():
  await cl.Message(
    content="Welcome to the Multi Agent System. How I can assist you?"
  ).send()

@cl.on_message
async def main(message: cl.Message):
  user_input = message.content
  response = asyncio.run(my_agent(user_input))
  await cl.Message(
    content=f"{response}"
  ).send()