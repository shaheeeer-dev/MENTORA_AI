import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
BASE_URL = st.secrets["BASE_URL"]
API_KEY = st.secrets["API_KEY"]


def ask_ai(prompt):
    url = f"{BASE_URL}/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {result}"
