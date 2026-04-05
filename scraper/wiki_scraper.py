import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("WIKI_API")
headers = {
    "User-Agent": os.getenv("USER_AGENT")
}

def get_wiki_summary(title):
    title = title.replace(" ", "_")
    url = f"{BASE_URL}/page/summary/{title}"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None
        
        data = response.json()

        extract =  data.get("extract", "")

        if "may refer to" in extract.lower():
            return None

        if len(extract) < 30:
            return None

        return extract
    
    except:
        return None
