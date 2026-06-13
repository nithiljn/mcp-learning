from mcp.server.fastmcp import FastMCP
import os 
import httpx
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("WEATHER")
@mcp.tool()
async def get_weather(location:str):
    """ get the weather data from the method for given location"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url,params=params)
        if response.status_code != 200 :
            return f"Error Fetching weather:{response.text}"
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return (
            f"Weather in {location}:\n"
            f"- Condition: {weather}\n"
            f"- Temperature: {temp}°C\n"
            f"- Humidity: {humidity}%"
        )
    
if __name__ == "__main__":
    mcp.run(transport="streamable-http")