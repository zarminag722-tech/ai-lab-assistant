import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Streamlit Page Setup
st.set_page_config(page_title="AI Lab Assistant", page_icon="🧪", layout="wide")

st.title("🧪 AI Lab Assistant")
st.write("Welcome! Your AI assistant for university science and CS lab experiments, safety, and reports.")

# System Prompt
SYSTEM_PROMPT = """
You are an expert AI Lab Assistant for university students.
Always follow this structured response format:
1. **Safety First & Equipment**: List precautions and apparatus needed.
2. **Step-by-Step Procedure**: Clear numbered instructions.
3. **Expected Observations & Troubleshooting**: What should happen and common mistakes.

Keep explanations clear, structured, and academic.
"""

# Navigation Tabs
tab1, tab2 = st.tabs(["📋 Experiment Guide", "📑 Lab Report Generator"])

with tab1:
    st.header("Search Experiment Procedure")
    exp_name = st.text_input("Enter Experiment Name (e.g., 'Titration of Acid-Base' or 'Binary Search Tree in C++')")
    
    if st.button("Generate Guide"):
        if exp_name:
            if not api_key:
                st.error("API Key missing! Please set GEMINI_API_KEY in Streamlit Secrets or .env file.")
            else:
                with st.spinner("Generating detailed procedure..."):
                    client = genai.Client(api_key=api_key)
                    prompt = f"{SYSTEM_PROMPT}\n\nProvide a lab guide for: {exp_name}"
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )
                    st.markdown(response.text)
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
                    client = genai.Client(api_key=api_key)
                    prompt = f"Format this into a clean academic lab report:\nTitle: {title}\nObjective: {objective}\nObservations: {observations}\nConclusion: {conclusion}"
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )
                    st.markdown("---")
                    st.markdown(response.text)
        else:
            st.warning("Please fill Title and Objective.")
