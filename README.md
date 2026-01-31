# 📊 ClassSense AI

**Track:** AI for Everyday Life – Task Simplification / Study Assistants

**ClassSense AI** is an AI-powered assistant that helps teachers and learners save time by automatically analyzing classroom chat to understand student confusion, urgency levels, and unanswered doubts.

In online classes and bootcamps, instructors often miss questions due to fast-moving chats, repeated doubts, and limited feedback tools.
**ClassSense AI reduces this cognitive load** by turning chaotic chat into structured insights and actionable teaching guidance.

---

## 💡 What It Does

* Analyzes classroom chat using natural language understanding
* Estimates overall student understanding (**Confused / Partial / Clear**)
* Detects **Class Urgency Level** (Low 🟢 / Medium 🟨 / High 🔴)
* Generates **Teaching Suggestions** based on confusion patterns
* Groups similar doubts so teachers address them once
* Highlights unique or easily missed questions
* Displays insights in a simple, teacher-friendly dashboard

---

## 🧠 How It Works

1. Teacher pastes chat text or uploads a `.txt` transcript (e.g., exported from Zoom / Google Meet)
2. The AI processes the chat using **Google Gemini**
3. The system performs **semantic analysis**, not keyword matching
4. Insights are rendered instantly in a clean Streamlit dashboard

Instead of polling or scanning hundreds of messages, instructors receive a **one-click engagement snapshot**.

---

## 🤖 Why Google Gemini

Google Gemini enables ClassSense AI to:

* Understand informal, real-world student language
* Detect meaning across differently worded questions
* Perform reasoning beyond simple keyword detection
* Provide **actionable suggestions**, not just summaries

---

## 🛠️ Tech Stack

* **Python** – Core backend logic
* **Streamlit** – Interactive dashboard UI
* **Google Gemini API** – Natural language reasoning & analysis

---

## 🚦 Key Features

### Engagement Snapshot

A quick overview of how well the class understood the topic.

### Urgency Indicator

Traffic-light system showing how critical the confusion level is:

* **Low (Green)** – Proceed
* **Medium (Yellow)** – Clarify briefly
* **High (Red)** – Pause & re-explain

### Teaching Suggestions

AI-generated next steps for instructors based on detected confusion.

### Doubt Clustering

Groups semantically similar questions into one representative doubt.

### Unique Doubts

Ensures rare but important questions are not missed.

---

## 🚀 Future Scope

* Windowed real-time integration with Zoom / Google Meet
* Adaptive teaching recommendations during lectures
* Student-side personalized revision feedback
* Exportable engagement summaries for teaching assistants

---

## 🏁 Status

Built as a **hackathon MVP** to demonstrate how AI can simplify everyday teaching workflows and improve learning efficiency without interrupting the natural teaching flow.

## 🧩 Why It Fits “AI for Everyday Life”

ClassSense AI is a **micro-optimization tool for daily teaching and learning**:

* Saves instructors time during live classes
* Reduces mental overload from large chat streams
* Provides clarity at natural teaching checkpoints
* Acts as a lightweight **AI study assistant**
* Converts noise into **actionable insight**

This directly aligns with **Task Simplification** and **Study Assistants** under **Track 1: AI for Everyday Life**.

---

**ClassSense AI — Turning classroom chaos into clarity.** ✨
