import os
import requests
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_linkedin_url(name: str, keyword: str) -> str:
    query = f"{name} {keyword} site:linkedin.com/in"
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {TAVILY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "search_depth": "basic",
        "include_answer": False,
        "include_raw_content": False
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        for result in data.get("results", []):
            if "linkedin.com/in" in result.get("url", ""):
                return result["url"]
        return "No LinkedIn profile found in results."
    else:
        return f"Tavily API error: {response.status_code} - {response.text}"
