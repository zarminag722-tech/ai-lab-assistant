import os
import requests
import streamlit as st

# Secrets se OpenRouter API Key lein
api_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="AI Lab Assistant", page_icon="🧪", layout="wide")

st.title("🧪 AI Lab Assistant")
st.write("Welcome! Your AI assistant for university science and CS lab experiments, safety, and reports.")

SYSTEM_PROMPT = """
You are an expert AI Lab Assistant for university students.
Always follow this structured response format:
1. **Safety First & Equipment**: List precautions and apparatus needed.
2. **Step-by-Step Procedure**: Clear numbered instructions.
3. **Expected Observations & Troubleshooting**: What should happen and common mistakes.

Keep explanations clear, structured, and academic.
"""

# Guaranteed free models list on OpenRouter
FREE_MODELS = [
    "qwen/qwen-2.5-72b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "mistralai/mistral-7b-instruct:free",
    "google/gemma-2-9b-it:free"
]

def query_openrouter(prompt_text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    last_error = ""
    for model in FREE_MODELS:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt_text}
            ]
        }
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        else:
            last_error = f"API Error {res.status_code}: {res.text}"
            
    raise Exception(f"All free endpoints failed. Last error: {last_error}")

tab1, tab2 = st.tabs(["📋 Experiment Guide", "📑 Lab Report Generator"])

with tab1:
    st.header("Search Experiment Procedure")
    exp_name = st.text_input("Enter Experiment Name (e.g., 'Titration of Acid-Base' or 'Binary Search Tree in C++')")
    
    if st.button("Generate Guide"):
        if exp_name:
            if not api_key:
                st.error("API Key missing! Please set OPENROUTER_API_KEY in Streamlit Secrets.")
            else:
                with st.spinner("Generating detailed procedure..."):
                    try:
                        result = query_openrouter(f"Provide a lab guide for: {exp_name}")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error generating guide: {str(e)}")
        else:
            st.warning("Please type an experiment name.")

with tab2:
    st.header("Format Lab Report")
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Report Title")
        objective = st.text_area("Objective / Aim")
    with col2:
        observations = st.text_area("Observations / Raw Data")
        conclusion = st.text_area("Conclusion (Optional)")
        
    if st.button("Generate Final Report"):
        if title and objective:
            if not api_key:
                st.error("API Key missing!")
            else:
                with st.spinner("Formatting report..."):
                    try:
                        prompt = f"Format this into a clean academic lab report:\nTitle: {title}\nObjective: {objective}\nObservations: {observations}\nConclusion: {conclusion}"
                        result = query_openrouter(prompt)
                        st.markdown("---")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error generating report: {str(e)}")
        else:
            st.warning("Please fill Title and Objective.")
