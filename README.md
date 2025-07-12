
# 🤖 Agentic Job Assistant

A modular, offline **Agentic AI system** to help users discover jobs, tailor resumes, and prepare for interviews — powered by local LLMs, NLP, and a user-friendly Streamlit interface.

---

## 🎯 Project Objective

> Build a system of intelligent agents that autonomously collaborate to:
- Discover job opportunities (Job Scout Agent)
- Tailor resumes to match job descriptions (Resume Tailor Agent)
- Generate interview questions and feedback (Interview Coach Agent – in progress)

---

## 🧠 Agents in the System

| Agent | Description |
|-------|-------------|
| 🔍 **Job Scout Agent** | Pulls job listings from RSS feeds or CSV and filters them by title, location, and keywords |
| 🧵 **Resume Tailor Agent** | Extracts job keywords, compares with your resume, and generates improvement tips using a local LLM |
| 🎤 **Interview Coach Agent** *(coming soon)* | Simulates mock interview questions and feedback using LLMs |

---

## 📂 Project Structure

agentic-job-assistant/
├── app.py # Streamlit app entry point
├── resume_tailor/ # Resume Tailor Agent code
│ └── tailor.py
├── job_scout/ # Job Scout Agent code
│ └── scout.py
├── interview_coach/ # Interview prep agent (coming soon)
│ └── coach.py
├── data/ # Resume + job description examples
│ ├── resume.txt
│ ├── job_description.txt
│ └── filtered_jobs.csv
├── notebooks/ # Jupyter notebooks (optional dev)
│ └── resume_tailor_agent.ipynb
├── images/ # UI visuals (banner, screenshots)
│ └── banner.png
├── requirements.txt # pip dependencies
├── architecture.txt # Design doc for system planning
└── README.md

yaml
Copy
Edit

---

## 🖥️ Demo UI

> Interactive web interface powered by [Streamlit](https://streamlit.io/):

- 📄 Paste your resume
- 💼 Paste a job description
- 🧠 Get LLM-generated advice
- 🗣️ [Coming soon] Simulate interviews

---

## 🚀 How to Run the App

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/agentic-job-assistant.git
cd agentic-job-assistant
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate  # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Launch the app
bash
Copy
Edit
streamlit run app.py
Open http://localhost:8501 to access the interface.

📦 Dependencies
txt
Copy
Edit
streamlit
nltk
requests
Run this to generate a fresh file if needed:

bash
Copy
Edit
pip freeze > requirements.txt
📌 Features at a Glance
✅ Keyword extraction with NLTK
✅ Resume-job alignment scoring
✅ LLM-powered improvement suggestions
✅ Interview simulation (coming soon)
✅ Offline/local LLM support (via Ollama, LM Studio, etc.)
✅ Built with modular Python code

🧠 Future Improvements
📝 Resume PDF upload & parser

📊 Application tracker & memory

🌍 Cloud deployment (optional)

🗣️ Real-time speech-to-text interview mode

💼 About the Author
Built by [Your Name]
LinkedIn Profile
GitHub

This project demonstrates hands-on experience in:

Agentic AI system design

Modular agent logic and orchestration

Local LLM integration

Streamlit front-end design
