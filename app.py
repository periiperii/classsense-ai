import streamlit as st
from gemini_utils import analyze_chat
from prompts import ANALYSIS_PROMPT

st.set_page_config(page_title="ClassSense AI", layout="wide")

st.title("📊 ClassSense AI")
st.caption(
    "An AI assistant that helps teachers understand student confusion "
    "and unanswered doubts using natural language analysis (Powered by Google Gemini)."
)

st.markdown(
    "### 📥 Classroom Chat Input\n"
    "Paste the live class chat or upload a chat transcript. "
    "ClassSense AI will analyze student understanding and group similar doubts."
)


chat_input = st.text_area(
    "Paste classroom chat here:",
    height=250,
    placeholder=(
        "Student A: I understood completely\n"
        "Student B: I don’t understand how the example is relevant\n"
        "Student C: The example is confusing\n"
        "Student D: What is the topic?"
    )
)

uploaded_file = st.file_uploader("Or upload chat file (.txt)", type=["txt"])

if uploaded_file:
    chat_input = uploaded_file.read().decode("utf-8")
if not chat_input.strip():
    st.info(
        "👆 Paste classroom chat text above and click **Analyze Chat** to see insights.")
if st.button("Analyze Chat"):
    if not chat_input.strip():
        st.warning("Please provide chat text.")
    else:
        with st.spinner("Analyzing classroom understanding..."):
            result = analyze_chat(chat_input, ANALYSIS_PROMPT)
        if not isinstance(result, dict):
            st.error("AI response could not be processed.")
            st.code(result)
            st.stop()

        st.divider()
        st.markdown("## 🧠 Overall Student Understanding")
        st.write(
            "This section shows an estimated breakdown of how well students understood "
            "the topic, inferred from their messages in the chat."
        )
        st.bar_chart(result["understanding"])
        st.markdown("## 🎯 Teaching Suggestions")
        st.write(
            "Based on student confusion patterns, here are suggested next steps for the instructor."
        )

        for tip in result["teaching_suggestions"]:
            st.markdown(f"- {tip}")

        st.markdown("## ❓ Common Doubts (Grouped by Meaning)")
        st.write(
            "Students often ask the same question in different ways. "
            "ClassSense AI groups similar doubts together so the teacher can "
            "address them once instead of scanning the entire chat."
        )

        for cluster in result["doubt_clusters"]:
            st.markdown(
                f"**🔹 {cluster['topic']}**  \n"
                f"Asked by **{cluster['count']} students**  \n"
                f"> {cluster['representative_doubt']}"
            )
        st.markdown("## 🧩 Unique or Rare Doubts")
        st.write(
            "These questions appeared only once, but may still be important. "
            "This ensures that no student’s doubt is missed."
        )

        for doubt in result["unique_doubts"]:
            st.markdown(f"- {doubt}")
