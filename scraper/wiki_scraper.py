import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("WIKI_API")
title = "Python programming language"

url = f"{BASE_URL}/page/summary/{title}"
headers = {
    "User-Agent": os.getenv("USER_AGENT")
}

response = requests.get(url, headers=headers)

print(response.status_code)
data = response.json()

print(data["title"])
print(data["extract"])