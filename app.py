import streamlit as st
from datetime import datetime
import os

from logic.decision import get_response
from utils.memory import Memory, load_logs
from utils.tts import speak

# initial memory
memory = Memory()

# weekly chat history
current_week = memory.get_week()

if "active_week" not in st.session_state:
    st.session_state.active_week = current_week

active_week = st.session_state.active_week

#display function
def format_label(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%a %d/%m")

#sidebar
st.sidebar.title("MENTORA")

logs_data = load_logs()
weeks = list(logs_data.keys())

if not weeks:
    st.sidebar.info("No chat history yet.")
else:
    for week in weeks:

        # convert stored week → readable label
        try:
            # take first message day timestamp if needed later
            label = format_label(week)
        except:
            label = "Chat"

        # BUT better: use real first message day from logs
        first_msg = logs_data[week][0] if logs_data[week] else None

        if first_msg:
            # extract timestamp day name from content if needed
            label = first_msg.get("day_name", week)

        if st.sidebar.button(label, use_container_width=True):
            st.session_state.active_week = week
            st.rerun()

st.sidebar.info("Only current day is editable.")

#chat
with st.chat_message(name="ai"):
    st.write("Hello! How may I assist you.")
logs_data = load_logs()
session_messages = memory.get_messages(active_week)
old_messages = logs_data.get(active_week, [])

messages = old_messages + session_messages

for msg in messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

#chat in current day
if active_week == current_week:

    user_input = st.chat_input("Ask me anything...")

    if user_input:

        with st.chat_message("user"):
            st.write(user_input)

        cached = memory.get_cache(user_input)

        if cached:
            response = cached
        else:
            response = get_response(user_input)
            memory.set_cache(user_input, response)

        with st.chat_message("assistant"):
            st.write(response)
            st.session_state.last_response = response

        memory.add_message(active_week, "user", user_input)
        memory.add_message(active_week, "assistant", response)

else:
    st.info("You can only chat in the current week.")

if "last_response" in st.session_state:

    if st.button("🔊"):

        audio_file = speak(st.session_state.last_response)

        st.audio(audio_file)

        os.remove(audio_file)