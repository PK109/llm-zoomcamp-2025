import asyncio
from fastmcp import Client

client = Client("weather_server.py")

async def call_tool():
    async with client:
        result = await client.list_tools()
        print(result)

asyncio.run(call_tool())