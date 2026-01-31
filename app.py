import streamlit as st
from gemini_utils import analyze_chat
from prompts import ANALYSIS_PROMPT

st.set_page_config(page_title="ClassSense AI", layout="wide")

st.title("📊 ClassSense AI")
st.caption(
    "AI-powered classroom understanding dashboard (Powered by Google Gemini)")

chat_input = st.text_area(
    "Paste classroom chat here:",
    height=250,
    placeholder="Student A: I didn't understand recursion...\nStudent B: Can you explain base case again?"
)

uploaded_file = st.file_uploader("Or upload chat file (.txt)", type=["txt"])

if uploaded_file:
    chat_input = uploaded_file.read().decode("utf-8")

if st.button("Analyze Chat"):
    if not chat_input.strip():
        st.warning("Please provide chat text.")
    else:
        with st.spinner("Analyzing classroom understanding..."):
            result = analyze_chat(chat_input, ANALYSIS_PROMPT)

        st.divider()
        st.markdown("### 🧠 Analysis Result")
        st.markdown(result)
