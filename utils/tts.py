import asyncio
import edge_tts
import tempfile

VOICE = "en-US-AriaNeural"

async def _generate(text, path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(path)


def speak(text):
    fd, path = tempfile.mkstemp(suffix=".mp3")

    asyncio.run(_generate(text, path))

    return path  # return file for streamlit to play