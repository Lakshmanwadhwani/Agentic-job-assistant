
def extract_keywords(text):
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from collections import Counter
    ...
    # rest of function


    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if w not in stopwords.words("english")]
    return [kw for kw, _ in Counter(words).most_common(30)]

def match_keywords(resume_text, job_keywords):
    from nltk.tokenize import word_tokenize
    resume_words = set(word_tokenize(resume_text.lower()))
    matched = [kw for kw in job_keywords if kw in resume_words]
    missing = [kw for kw in job_keywords if kw not in resume_words]
    return matched, missing

def local_llm_summary(prompt):
    import requests
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "local-model",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 250
    }
    response = requests.post("http://localhost:1234/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

import streamlit as st


st.set_page_config(page_title="Agentic Resume Tailor", layout="centered")

st.title("🧠 Agentic Resume Tailor")
st.markdown("Tailor your resume to job descriptions using LLMs + keyword matching")

# User inputs
resume_text = st.text_area("📄 Paste your resume here", height=300)
job_description = st.text_area("💼 Paste job description here", height=200)

if st.button("Generate Tailored Advice"):
    if not resume_text or not job_description:
        st.warning("Please paste both your resume and job description.")
    else:
        job_keywords = extract_keywords(job_description)
        matched, missing = match_keywords(resume_text, job_keywords)

        prompt = f"""
        Job Description:
        {job_description}

        Resume:
        {resume_text}

        Matched: {matched}
        Missing: {missing}

        Suggest resume improvements to better align with the job description.
        """

        summary = local_llm_summary(prompt)
        st.subheader("🎯 Tailored Resume Suggestions")
        st.markdown(summary)

