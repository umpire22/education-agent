import streamlit as st
import datetime

st.set_page_config(page_title="Education AI Agent", page_icon="📘", layout="centered")

st.title("📘 Education AI Agent")
st.write("Plan your study schedule and get quick study prompts (no API keys needed).")

with st.form("study_form"):
    subject = st.text_input("Subject", placeholder="e.g., Mathematics")
    duration = st.number_input("Study duration (minutes)", min_value=10, max_value=180, value=30)
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
    start_time = st.time_input("Preferred study time", datetime.time(19, 0))
    submitted = st.form_submit_button("Generate Plan")

if submitted:
    prompt = f"""
📘 **Study Plan**
- Subject: {subject or "Your chosen subject"}
- Duration: {duration} minutes
- Level: {level}
- Time: {start_time.strftime('%H:%M')}

**Tips**
- Set a timer and remove distractions.
- Focus on 2–3 key concepts.
- Summarize the last 5 minutes.
- Review flashcards tomorrow.
"""
    st.success("Your plan is ready!")
    st.code(prompt, language="markdown")
