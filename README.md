# Mentora
![Static Badge](https://img.shields.io/badge/MENTORA%20AI-8A2BE2)<BR>
![AI](https://img.shields.io/badge/AI-Study_Assistant-purple.svg) <br>
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Overview
**Mentora** is an AI-powered study assistant that helps students learn faster by combining dictionary lookup, web search, AI-generated explanations and text-to-speech output. It is designed to simplify learning and provide quick, clear, and interactive responses.

## Architecture Diagram 
<img width="904" height="428" alt="Screenshot 2026-04-24 at 1 04 36 AM" src="https://github.com/user-attachments/assets/3e0b82bd-283c-480b-ab5e-9dffd788ae7c" />

## Features
- Local dictionary-based definitions (JSON knowledge base)

- Web search / scraping for real-time information

- AI-powered response generation (LLM-based)

- Smart decision system (routes queries intelligently)

- Simplified explanations for students

- Text-to-Speech (TTS) for audio responses

- Interactive chat-based interface (Streamlit)

## How It Works
1. User enters a question in the chat UI  

2. `decision.py` analyzes and classifies the query  

3. System routes it to the appropriate module:

   - Dictionary (basic meanings)

   - Web (real-world data)

   - AI model (deep explanations)

4. Response is generated and returned  

5. TTS converts response into speech  

6. User receives both **text + audio output**

## Goal
To build a smart, lightweight AI study assistant that combines multiple knowledge sources with voice interaction for better learning experience.

## Project Structure

```
Mentora_AI/
│
├── app.py                          # Streamlit frontend
│
├── models/
│   ├── generator.py               # Groq response generator
│
├── logic/
│   ├── decision.py                # Routes: dictionary / scraper / AI
│
├── data/
│   ├── dictionary.json            # predefined knowledge base
│   ├── logs.txt                   # user history / cache
│
├── scraper/
│   ├── wiki_scraper.py            # Wikipedia fetch only
│
├── utils/
│   ├── tts.py                     # voice output
│   ├── memory.py                  # handles last queries cache
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
## Author
Built by **Muhammad Shaheer**  
Project: Mentora – AI Study Assistant


