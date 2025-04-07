import os
import requests
from dotenv import load_dotenv

load_dotenv()
PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")

def fetch_profile_data(linkedin_url: str) -> dict:
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {"Authorization": f"Bearer {PROXYCURL_API_KEY}"}
    params = {
        "url": linkedin_url,
        "use_cache": "if-present",
    }

    response = requests.get(api_endpoint, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Proxycurl API error: {response.status_code} - {response.text}"}
